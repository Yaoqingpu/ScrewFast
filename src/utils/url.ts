/** Ensure internal paths always end with `/` (except `#` / external / empty). */
export function withSlash(path: string): string {
  if (!path || path === '/' || path.startsWith('#') || path.startsWith('http')) {
    return path || '/';
  }
  if (path.includes('?') || path.includes('#')) {
    // rare for our static site; leave as-is
    return path.endsWith('/') ? path : `${path}/`;
  }
  return path.endsWith('/') ? path : `${path}/`;
}

export function absoluteUrl(site: string, path: string): string {
  const base = site.replace(/\/$/, '');
  const p = withSlash(path.startsWith('/') ? path : `/${path}`);
  return `${base}${p}`;
}
