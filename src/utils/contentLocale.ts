/** Normalize Astro content entry ids (Windows may use `\`). */
export function contentId(id: string): string {
  return id.replace(/\\/g, '/');
}

/**
 * Blog/product glob entries use frontmatter `slug` as `id`, so locale lives in
 * `filePath` (e.g. src/content/blog/en/post-1.md). Always prefer filePath.
 */
export function isEnContent(id: string, filePath?: string): boolean {
  const path = contentId(filePath || id);
  if (/(^|\/)en(\/|$)/.test(path)) return true;
  const bare = contentId(id);
  return !bare.includes('/');
}
