/**
 * RFQ form endpoint (Cloudflare Pages Function).
 *
 * POST /api/contact
 *   - validates the submission and drops honeypot spam
 *   - delivers the RFQ to the sales inbox
 *
 * Two delivery backends, tried in order:
 *
 * 1. Cloudflare Email Service (preferred, no third-party account):
 *    Requires the domain onboarded to Email Sending (Dashboard → Compute & AI
 *    → Email Service → Email Sending → Onboard Domain) and an API token with
 *    "Email Sending" permission:
 *      EMAIL_API_TOKEN           secret, wrangler pages secret put ...
 *      CLOUDFLARE_ACCOUNT_ID     optional, defaults to the FerruleX account
 *    Sender defaults to rfq@ferrulex.com (MAIL_FROM).
 *
 * 2. Plain SMTP over a Cloudflare TCP socket (fallback):
 *    SMTP_HOST / SMTP_USER / SMTP_PASS (+ optional SMTP_PORT, MAIL_FROM)
 *    e.g. smtp.gmail.com:465 with a Gmail app password.
 *
 * Recipient: RFQ_TO_EMAIL (default: the sender account / rfq@ferrulex.com).
 */

/// <reference path="./smtp.d.ts" />
import { connect, type Socket } from 'cloudflare:sockets';

interface Env {
  EMAIL_API_TOKEN?: string;
  CLOUDFLARE_ACCOUNT_ID?: string;
  SMTP_HOST?: string;
  SMTP_PORT?: string;
  SMTP_USER?: string;
  SMTP_PASS?: string;
  MAIL_FROM?: string;
  RFQ_TO_EMAIL?: string;
}

const ACCOUNT_ID = '035e67621098f43f3d1d0469fe2b6b7b';
const DEFAULT_FROM = 'rfq@ferrulex.com';
const DEFAULT_TO = 'sales@ferrulex.com';

const MAX_FIELD_LENGTH = 2000;
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const SMTP_TIMEOUT_MS = 20000;

function fieldValue(form: FormData, key: string): string {
  const value = form.get(key);
  return typeof value === 'string'
    ? value.trim().slice(0, MAX_FIELD_LENGTH)
    : '';
}

function respond(
  request: Request,
  status: number,
  message: string,
  ok = false
): Response {
  const acceptsJson = (request.headers.get('accept') ?? '').includes(
    'application/json'
  );
  if (acceptsJson) {
    return Response.json({ ok, message }, { status });
  }
  // Plain (no-JS) form post: bounce back to the page the visitor came from.
  const target = new URL(
    request.headers.get('referer') || '/contact/',
    request.url
  );
  target.searchParams.set('rfq', ok ? 'sent' : 'error');
  return Response.redirect(target, 303);
}

export const onRequestPost = async ({
  request,
  env,
}: {
  request: Request;
  env: Env;
}): Promise<Response> => {
  const form = await request.formData().catch(() => null);
  if (!form) {
    return respond(request, 400, 'Invalid form data.');
  }

  // Honeypot: invisible to visitors, bots fill it — accept and drop.
  if (fieldValue(form, 'website')) {
    return respond(request, 200, 'ok', true);
  }

  const name = fieldValue(form, 'name');
  const email = fieldValue(form, 'email');
  const company = fieldValue(form, 'company');
  const topic = fieldValue(form, 'topic');
  const details = fieldValue(form, 'message');

  const source = fieldValue(form, 'source');

  const emailService = !!env.EMAIL_API_TOKEN;
  const smtp = !!(env.SMTP_HOST && env.SMTP_USER && env.SMTP_PASS);
  if (!emailService && !smtp) {
    return respond(
      request,
      503,
      'The form is not connected to the inbox yet — please email sales@ferrulex.com directly.'
    );
  }

  const sendSubmission = async (subject: string, text: string) => {
    await sendMail(env, { subject, text, replyTo: email });
  };

  // Newsletter signup: only the email is required.
  if (source === 'newsletter') {
    if (!email || !EMAIL_PATTERN.test(email)) {
      return respond(request, 400, 'Please provide a valid email address.');
    }
    try {
      await sendSubmission(
        `Newsletter signup: ${email}`,
        `New newsletter subscriber: ${email}\nSubmitted: ${new Date().toISOString()}`
      );
    } catch (error) {
      console.error('Newsletter SMTP error:', error);
      return respond(
        request,
        502,
        'Signup failed on our side. Please email sales@ferrulex.com directly.'
      );
    }
    return respond(request, 200, 'ok', true);
  }

  if (!email || !EMAIL_PATTERN.test(email)) {
    return respond(request, 400, 'Please provide a valid email address.');
  }
  if (!details) {
    return respond(
      request,
      400,
      'Please add your size list so the factory can quote.'
    );
  }

  const displayName = name || 'RFQ visitor';
  const subject = `${topic || 'RFQ'} from ${displayName} <${email}>`;
  const text = [
    `Name: ${displayName}`,
    `Email: ${email}`,
    company ? `Company: ${company}` : null,
    topic ? `Topic: ${topic}` : null,
    '',
    'Message:',
    details,
    '',
    `Submitted: ${new Date().toISOString()}`,
  ]
    .filter(line => line !== null)
    .join('\n');

  try {
    await sendSubmission(subject, text);
  } catch (error) {
    console.error('RFQ SMTP error:', error);
    return respond(
      request,
      502,
      'Sending failed on our side. Please email sales@ferrulex.com directly — we reply in 1–2 business days.'
    );
  }

  return respond(request, 200, 'ok', true);
};

/** Minimal SMTP client over a Cloudflare TCP socket (port 465 or 587). */
class SmtpError extends Error {}

class SmtpClient {
  private reader: ReadableStreamDefaultReader<Uint8Array>;
  private writer: WritableStreamDefaultWriter<Uint8Array>;
  private buffered = '';
  private readonly decoder = new TextDecoder();
  private readonly encoder = new TextEncoder();

  constructor(private socket: Socket) {
    this.reader = socket.readable.getReader();
    this.writer = socket.writable.getWriter();
  }

  async expect(code: string): Promise<void> {
    // Replies can span several lines: "250-..." continues, "250 " ends.
    for (;;) {
      const line = await this.readLine();
      if (line.startsWith(code) && line.charAt(3) === ' ') return;
      if (!/^\d{3}[- ]/.test(line)) {
        throw new SmtpError(`Unexpected SMTP reply: ${line}`);
      }
    }
  }

  async send(line: string, expectCode?: string): Promise<void> {
    await this.writer.write(this.encoder.encode(`${line}\r\n`));
    if (expectCode) await this.expect(expectCode);
  }

  private async readLine(): Promise<string> {
    for (;;) {
      const end = this.buffered.indexOf('\r\n');
      if (end >= 0) {
        const line = this.buffered.slice(0, end);
        this.buffered = this.buffered.slice(end + 2);
        return line;
      }
      const { value, done } = await withTimeout(this.reader.read());
      if (done) throw new SmtpError('SMTP connection closed unexpectedly.');
      this.buffered += this.decoder.decode(value, { stream: true });
    }
  }

  async startTls(): Promise<void> {
    // Release the plaintext-side locks BEFORE upgrading; the new socket
    // requires fresh readers/writers (and locks its own streams).
    this.writer.releaseLock();
    this.reader.releaseLock();
    this.socket = this.socket.startTls();
    this.reader = this.socket.readable.getReader();
    this.writer = this.socket.writable.getWriter();
    this.buffered = '';
  }
}

function withTimeout<T>(promise: Promise<T>): Promise<T> {
  return Promise.race([
    promise,
    new Promise<T>((_, reject) =>
      setTimeout(
        () => reject(new SmtpError('SMTP server did not respond in time.')),
        SMTP_TIMEOUT_MS
      )
    ),
  ]);
}

function utf8ToBase64(value: string): string {
  const bytes = new TextEncoder().encode(value);
  let binary = '';
  bytes.forEach(byte => {
    binary += String.fromCharCode(byte);
  });
  return btoa(binary);
}

function encodeHeader(value: string): string {
  // Encode as RFC 2047 only when non-ASCII characters are present.
  return /[^\x20-\x7E]/.test(value)
    ? `=?UTF-8?B?${utf8ToBase64(value)}?=`
    : value;
}

async function sendMail(
  env: Env,
  mail: { subject: string; text: string; replyTo: string }
): Promise<void> {
  if (env.EMAIL_API_TOKEN) {
    return sendViaEmailService(env, mail);
  }
  return sendSmtpMail(env, mail);
}

/** Cloudflare Email Service REST API — no SMTP, no third-party account. */
async function sendViaEmailService(
  env: Env,
  mail: { subject: string; text: string; replyTo: string }
): Promise<void> {
  const accountId = env.CLOUDFLARE_ACCOUNT_ID || ACCOUNT_ID;
  const response = await fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/email/sending/send`,
    {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.EMAIL_API_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        to: env.RFQ_TO_EMAIL || DEFAULT_TO,
        from: {
          address: env.MAIL_FROM || DEFAULT_FROM,
          name: 'FerruleX Website',
        },
        subject: mail.subject,
        text: mail.text,
        reply_to: mail.replyTo,
      }),
    }
  );

  if (!response.ok) {
    const detail = await response.text().catch(() => '');
    throw new SmtpError(
      `Email Service send failed: ${response.status} ${detail.slice(0, 200)}`
    );
  }

  const result = (await response.json()) as {
    result?: { permanent_bounces?: unknown[] };
  };
  if (result.result?.permanent_bounces?.length) {
    throw new SmtpError('Email Service reported a permanent bounce.');
  }
}

async function sendSmtpMail(
  env: Env,
  mail: { subject: string; text: string; replyTo: string }
): Promise<void> {
  const port = Number(env.SMTP_PORT || 465);

  if (port !== 587) {
    return smtpSession(env, port, mail, false);
  }

  // 587 with STARTTLS. workerd has an open startTls() bug
  // (cloudflare/workerd#2712) — if the upgrade fails, retry on 465
  // implicit TLS before giving up.
  try {
    await smtpSession(env, 587, mail, true);
  } catch (starttlsError) {
    console.warn('STARTTLS failed, retrying on port 465:', starttlsError);
    try {
      await smtpSession(env, 465, mail, false);
    } catch {
      throw starttlsError;
    }
  }
}

async function smtpSession(
  env: Env,
  port: number,
  mail: { subject: string; text: string; replyTo: string },
  useStartTls: boolean
): Promise<void> {
  const from = env.MAIL_FROM || env.SMTP_USER!;
  const to = env.RFQ_TO_EMAIL || env.SMTP_USER!;

  // String-address form: workerd ignores secureTransport when the address is
  // passed as a dictionary (its startTls() then throws) — cloudflare/workerd#2712.
  const socket = connect(`${env.SMTP_HOST}:${port}`, {
    secureTransport: useStartTls ? 'starttls' : 'on',
  });
  const smtp = new SmtpClient(socket);

  try {
    await smtp.expect('220');
    await smtp.send(`EHLO ferrulex.com`, '250');

    if (useStartTls) {
      await smtp.send('STARTTLS', '220');
      await smtp.startTls();
      await smtp.send(`EHLO ferrulex.com`, '250');
    }

    await smtp.send('AUTH LOGIN', '334');
    await smtp.send(btoa(env.SMTP_USER!), '334');
    await smtp.send(btoa(env.SMTP_PASS!), '235');

    await smtp.send(`MAIL FROM:<${from}>`, '250');
    await smtp.send(`RCPT TO:<${to}>`, '250');
    await smtp.send('DATA', '354');

    // Base64 body: immune to CRLF and dot-stuffing edge cases.
    const message = [
      `From: FerruleX Website <${from}>`,
      `To: ${to}`,
      `Subject: ${encodeHeader(mail.subject)}`,
      `Date: ${new Date().toUTCString()}`,
      `Reply-To: ${mail.replyTo}`,
      'MIME-Version: 1.0',
      'Content-Type: text/plain; charset=utf-8',
      'Content-Transfer-Encoding: base64',
      '',
      utf8ToBase64(mail.text),
    ].join('\r\n');
    await smtp.send(`${message}\r\n.`, '250');

    await smtp.send('QUIT');
  } finally {
    socket.close();
  }
}
