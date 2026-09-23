import ogImageSrc from '@images/social.png';

export const SITE = {
  title: 'FerruleX',
  tagline: 'Factory Stainless Steel Valves & Fittings — Fast Delivery',
  description:
    'FerruleX is a Nanjing, China factory for stainless steel compression fittings, ball valves, needle valves, check valves and corrugated hose. For many years we have supplied export OEM and project RFQs — SS304 / SS316 / SS316L, stocked sizes ship in 5–7 days.',
  description_short:
    'China factory for stainless steel fittings and valves — compression, ball, needle, hose. Export RFQ. Stocked sizes ship fast.',
  url: 'https://ferrulex.com',
  author: 'FerruleX',
  email: 'sales@ferrulex.com',
  /** E.164 without + for wa.me; display uses phoneDisplay */
  phone: '+8613814034409',
  phoneDisplay: '+86 138 1403 4409',
  whatsappUrl: 'https://wa.me/8613814034409',
  /** Public factory / courier address */
  address: 'No. 212, Lantian Road, Lukou District, Jiangning, Nanjing, China',
  addressParts: {
    street: 'No. 212, Lantian Road, Lukou District, Jiangning',
    locality: 'Nanjing',
    region: 'Jiangsu',
    postalCode: '',
    country: 'CN',
  },
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
    'Nanjing factory for stainless steel compression fittings, ball valves, needle valves and corrugated hose. Stocked sizes ship fast — request a quote.',
  image: ogImageSrc,
};

