const navBarLinks = [
  { name: 'Home', url: '/' },
  { name: 'Products', url: '/products/' },
  { name: 'About', url: '/about/' },
  { name: 'Services', url: '/services/' },
  { name: 'Blog', url: '/blog/' },
  { name: 'Contact', url: '/contact/' },
];

const footerLinks = [
  {
    section: 'Catalog',
    links: [
      { name: 'All Categories', url: '/products/' },
      {
        name: 'Compression Fittings',
        url: '/products/compression-fittings/',
      },
      { name: 'Ball Valves', url: '/products/ball-valves/' },
      { name: 'Needle Valves', url: '/products/needle-valves/' },
      { name: 'Check Valves', url: '/products/check-valves/' },
      {
        name: 'Corrugated Hose',
        url: '/products/corrugated-hose/',
      },
      { name: '2-Piece Ball Valve', url: '/2-piece-ball-valve/' },
      { name: 'Downloads', url: '/downloads/' },
    ],
  },
  {
    section: 'Company',
    links: [
      { name: 'About the Factory', url: '/about/' },
      { name: 'Delivery', url: '/delivery/' },
      { name: 'Quality', url: '/quality/' },
      { name: 'OEM & Custom', url: '/oem/' },
      { name: 'Applications', url: '/applications/' },
      { name: 'Services', url: '/services/' },
      { name: 'FAQ', url: '/faq/' },
      { name: 'Contact / RFQ', url: '/contact/' },
      { name: 'Blog', url: '/blog/' },
      { name: 'Privacy', url: '/privacy/' },
    ],
  },
];

const socialLinks = {
  facebook: '#',
  x: '#',
  google: '#',
};

export default {
  navBarLinks,
  footerLinks,
  socialLinks,
};
