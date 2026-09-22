import sharp from 'sharp';
import { statSync } from 'node:fs';

const kb = f => Math.round(statSync(f).size / 1024);

// 1) hero-plant.jpg: 1920x3413 portrait -> 3:2 landscape pre-crop.
//    Take the band from ~18% to ~66% of height (upper-middle: the analyzer
//    located the densest piping runs there), then resize to 1800x1200.
const hero = 'src/images/apps/hero-plant.jpg';
const meta = await sharp(hero).metadata();
const cropTop = Math.round(meta.height * 0.18);
const cropHeight = Math.round(meta.width * 1.5); // 3:2 of full width
await sharp(hero)
  .extract({ left: 0, top: cropTop, width: meta.width, height: Math.min(cropHeight, meta.height - cropTop) })
  .resize(1800, 1200, { fit: 'cover' })
  .jpeg({ quality: 82, mozjpeg: true })
  .toFile('src/images/apps/hero-plant-landscape.jpg');
console.log(
  'hero:',
  meta.width + 'x' + meta.height,
  kb(hero) + 'KB -> ',
  '1800x1200',
  kb('src/images/apps/hero-plant-landscape.jpg') + 'KB'
);

// 2) Order-facts banner: reuse app-instrument.jpg (1800x1200) as-is;
//    Astro will AVIF-encode it at build. Nothing to preprocess — just log.
const banner = 'src/images/apps/app-instrument.jpg';
const bm = await sharp(banner).metadata();
console.log('banner (app-instrument):', bm.width + 'x' + bm.height, kb(banner) + 'KB — ready');
