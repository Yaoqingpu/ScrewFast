import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  // https://docs.astro.build/en/guides/images/#authorizing-remote-images
  site: 'https://ferrulex.com',
  // Links on the site use a trailing slash (SEO_URL.md hard rule #5).
  // `always` builds and serves only the slashed form; the previous `ignore`
  // setting let /products and /products/ both return 200 (duplicate URLs).
  trailingSlash: 'always',
  image: {
    domains: ['images.unsplash.com'],
  },
  prefetch: true,
  integrations: [
    sitemap({
      i18n: {
        defaultLocale: 'en', // All urls that don't contain language prefix will be treated as default locale
        locales: {
          en: 'en', // The `defaultLocale` value must present in `locales` keys
        },
      },
    }),
    mdx(),
  ],
  experimental: {
    clientPrerender: true,
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
