import sharp from 'sharp';

// Optimization pipeline for video frames (1280x720 source):
// trim dark/uniform edges, correct cast, lift exposure, gentle sharpen.
const jobs = [
  {
    src: 'public/tmp-view/best-f10.png',
    out: 'public/tmp-view/final-f10.jpg',
    // group shot on cloth: keep full width, trim loose top/bottom slightly
    crop: { left: 40, top: 40, width: 1200, height: 640 },
    tune: { brightness: 1.06, saturation: 0.92, linear: [1.08, -12] },
    resize: 1200,
  },
  {
    src: 'public/tmp-view/best-f15.png',
    out: 'public/tmp-view/final-f15.jpg',
    // single valve turntable: center square-ish crop
    crop: { left: 280, top: 0, width: 720, height: 720 },
    tune: { brightness: 1.05, saturation: 0.94, linear: [1.06, -10] },
    resize: 860,
  },
];

for (const j of jobs) {
  const { width, height } = j.resize
    ? j.crop.width >= j.crop.height
      ? { width: j.resize, height: Math.round((j.resize * j.crop.height) / j.crop.width) }
      : { width: Math.round((j.resize * j.crop.width) / j.crop.height), height: j.resize }
    : j.crop;
  await sharp(j.src)
    .extract(j.crop)
    .modulate({ brightness: j.tune.brightness, saturation: j.tune.saturation })
    .linear(j.tune.linear[0], j.tune.linear[1])
    .normalise({ lower: 1, upper: 99 })
    .sharpen({ sigma: 0.8 })
    .resize(width, height, { kernel: 'lanczos3' })
    .jpeg({ quality: 90, mozjpeg: true })
    .toFile(j.out);
  console.log(j.out, width + 'x' + height);
}
