import ogImageSrc from '@images/social.png';

export const SITE = {
  title: 'FerruleX',
  tagline: 'Factory Stainless Steel Valves & Fittings — Fast Delivery',
  description:
    'FerruleX is a China stainless steel fittings factory for export buyers. We manufacture and stock compression fittings, ball valves, needle valves and corrugated hose. Fast delivery on common sizes — request a quote.',
  description_short:
    'Factory-direct stainless steel fittings with fast delivery for OEM and project RFQs.',
  url: 'https://ferrulex.com',
  author: 'FerruleX',
};

export const SEO = {
  title: SITE.title,
  description: SITE.description,
  structuredData: {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    inLanguage: 'en-US',
    '@id': SITE.url,
    url: SITE.url,
    name: SITE.title,
    description: SITE.description,
    isPartOf: {
      '@type': 'WebSite',
      url: SITE.url,
      name: SITE.title,
      description: SITE.description,
    },
  },
};

export const OG = {
  locale: 'en_US',
  type: 'website',
  url: SITE.url,
  title: `${SITE.title}: Factory Stainless Fittings — Fast Delivery`,
  description:
    'China factory for stainless steel compression fittings, ball valves and corrugated hose. Fast delivery on stocked sizes — request a quote.',
  image: ogImageSrc,
};

