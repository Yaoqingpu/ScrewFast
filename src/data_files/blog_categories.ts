export type BlogCategoryDef = {
  slug: string;
  title: string;
  shortTitle: string;
  description: string;
  keyword: string;
};

/** Blog categories — hub /blog/{slug}/ ; posts are flat /blog/{post}/ */
export const BLOG_CATEGORIES: BlogCategoryDef[] = [
  {
    slug: 'materials-grades',
    title: 'Materials & Grades',
    shortTitle: 'Materials',
    description:
      'SS304 vs SS316 and SS316L for stainless fittings, valves and hose: corrosion resistance, cost and when each grade ships from FerruleX factory stock.',
    keyword: 'SS304 vs SS316 fittings',
  },
  {
    slug: 'threads-standards',
    title: 'Threads & Standards',
    shortTitle: 'Threads',
    description:
      'NPT, G (BSP), ZG(R) BSPT and metric thread guides for stainless steel fittings and valve buyers — identify the thread before you send a factory RFQ.',
    keyword: 'NPT vs BSP stainless fittings',
  },
  {
    slug: 'installation-guides',
    title: 'Installation Guides',
    shortTitle: 'Installation',
    description:
      'How to install double-ferrule compression fittings, ball valves and corrugated hose — tube insertion, ferrule order, torque and leak checks from the factory.',
    keyword: 'compression fitting installation',
  },
  {
    slug: 'industry-applications',
    title: 'Industry Applications',
    shortTitle: 'Applications',
    description:
      'Where FerruleX stainless steel fittings and valves work: petrochemical skids, OEM instrument panels, food equipment, marine lines and HVAC jumps.',
    keyword: 'instrumentation fittings applications',
  },
  {
    slug: 'factory-export',
    title: 'Factory & Export',
    shortTitle: 'Factory / Export',
    description:
      'How the FerruleX factory quotes RFQs, stocks common stainless fitting and valve sizes, packs export cartons and ships stocked sizes in 5–7 days.',
    keyword: 'stainless steel fittings manufacturer',
  },
];

export function getBlogCategory(slug: string): BlogCategoryDef | undefined {
  return BLOG_CATEGORIES.find(c => c.slug === slug);
}

export function blogCategoryPath(slug: string): string {
  return `/blog/${slug}/`;
}

export function blogPostPath(_category: string, slug: string): string {
  return `/blog/${slug}/`;
}

export function blogHubPath(): string {
  return '/blog/';
}
