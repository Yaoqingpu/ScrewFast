/**
 * Minimal ambient types for Cloudflare's TCP socket API.
 * Avoids pulling in the full @cloudflare/workers-types package.
 */
declare module 'cloudflare:sockets' {
  export interface Socket {
    readable: ReadableStream<Uint8Array>;
    writable: WritableStream<Uint8Array>;
    /** Upgrades an insecure connection to TLS (for SMTP STARTTLS). */
    startTls(): Socket;
    closed: Promise<undefined>;
    close(): void;
  }

  export function connect(
    address: string,
    options?: { secureTransport?: 'off' | 'on' | 'starttls' }
  ): Socket;
  export function connect(options: {
    hostname: string;
    port: number;
    /** 'on' = implicit TLS (465), 'starttls' = plaintext, upgrade later (587). */
    secureTransport?: 'off' | 'on' | 'starttls';
  }): Socket;
}
