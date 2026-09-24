/**
 * RFQ form handler.
 * Submits forms marked with [data-rfq-form] to their action endpoint
 * via fetch, and surfaces success / error messages inline.
 */
function initRfqForms() {
  document.querySelectorAll('[data-rfq-form]').forEach(form => {
    if (form.dataset.rfqBound === 'true') return;
    form.dataset.rfqBound = 'true';

    const status =
      form.querySelector('[data-form-status]') ??
      form.parentElement?.querySelector('[data-form-status]');
    const button = form.querySelector('button[type="submit"]');

    const showStatus = (message, isError) => {
      if (!status) return;
      status.textContent = message;
      status.classList.toggle('hidden', false);
      status.classList.toggle('text-red-600', isError);
      status.classList.toggle('dark:text-red-400', isError);
      status.classList.toggle('text-blue-600', !isError);
      status.classList.toggle('dark:text-blue-400', !isError);
    };

    form.addEventListener('submit', async event => {
      event.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      const successMessage =
        status?.dataset.successMessage ||
        'Thanks — your RFQ is in the inbox. We reply in 1–2 business days.';
      const fallbackError =
        'Something went wrong. Please email sales@ferrulex.com directly.';

      if (button) button.disabled = true;
      showStatus('Sending…', false);

      try {
        const response = await fetch(form.action, {
          method: 'POST',
          headers: { Accept: 'application/json' },
          body: new FormData(form),
        });
        const data = await response.json().catch(() => null);
        if (response.ok && data?.ok) {
          showStatus(successMessage, false);
          form.reset();
        } else {
          showStatus(data?.message || fallbackError, true);
        }
      } catch {
        showStatus(fallbackError, true);
      } finally {
        if (button) button.disabled = false;
      }
    });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initRfqForms);
} else {
  initRfqForms();
}
