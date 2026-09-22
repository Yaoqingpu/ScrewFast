export type CategoryDef = {
  /** Short SEO path segment, e.g. compression-fittings */
  slug: string;
  /** Short buyer-facing intro shown under the h1 on category pages */
  intro: string;
  title: string;
  shortTitle: string;
  description: string;
  keyword: string;
  h1: string;
  match: string[];
};

export const PRODUCT_CATEGORIES: CategoryDef[] = [
  {
    slug: 'corrugated-hose',
    intro:
      'Start from the hose OD and the two end connections. If the media is steam or the run crosses a hot zone, tell us the temperature — bellows material and braid change with it.',
    title: 'Corrugated Stainless Steel Hose',
    shortTitle: 'Corrugated Hose',
    h1: 'Corrugated Stainless Steel Hose & Expansion Joints',
    description:
      'Corrugated hose for vibration and thermal movement: male/female thread, flange, tri-clamp, quick coupling and KF. SS304 or SS316. Length and ends on the RFQ.',
    keyword: 'corrugated stainless steel hose',
    match: ['corrugated hose', 'expansion joint', 'kf flexible', 'corrugated tube'],
  },
  {
    slug: 'ball-valves',
    intro:
      'Pick the end first (compression, female thread or weld), then the flow pattern. Pressure class and seat material are confirmed on the quote, not assumed.',
    title: 'Stainless Steel Ball Valves',
    shortTitle: 'Ball Valves',
    h1: 'Stainless Steel Ball Valves',
    description:
      'Shutoff valves with compression, female thread or weld ends. Straight, angle, 3-way and high-pressure styles. Confirm the pressure class on the quote.',
    keyword: 'stainless steel ball valve',
    match: ['ball valve'],
  },
  {
    slug: 'check-valves',
    intro:
      'These valves are direction-sensitive. Mark flow direction and cracking pressure on the RFQ so the factory sets the spring or disc correctly.',
    title: 'Stainless Steel Check Valves',
    shortTitle: 'Check Valves',
    h1: 'Stainless Steel Check Valves & Inline Filters',
    description:
      'One-way valves in compression, female thread and split-body styles, plus inline filters. Mark flow direction on the order.',
    keyword: 'stainless steel check valve',
    match: ['check valve', 'inline filter'],
  },
  {
    slug: 'needle-valves',
    intro:
      'Needle valves meter flow — they are not shutoff valves. Send the orifice size and the gauge or sampler it feeds, and we match the Cv.',
    title: 'Stainless Steel Needle Valves',
    shortTitle: 'Needle Valves',
    h1: 'Stainless Steel Needle & Globe Valves',
    description:
      'Needle and globe valves for metering, sampling and gauge isolation. Compression or female thread. Not a substitute for a ball valve on full-flow shutoff.',
    keyword: 'stainless steel needle valve',
    match: ['needle valve', 'globe valve'],
  },
  {
    slug: 'compression-fittings',
    intro:
      'Measure tube OD exactly (metric or inch). A double-ferrule joint is sized by tube, so the OD plus the port thread decides the part.',
    title: 'Stainless Steel Compression Fittings',
    shortTitle: 'Compression Fittings',
    h1: 'Stainless Steel Compression Fittings (Double Ferrule)',
    description:
      'Double-ferrule connectors, elbows, tees, unions and bulkheads. Metric and inch tube. NPT, G and metric threads.',
    keyword: 'stainless steel compression fittings',
    match: [
      'compression',
      'ferrule',
      'ground finish',
      'forged',
      'cylinder connector',
      'bulkhead',
    ],
  },
  {
    slug: 'tube-fittings',
    intro:
      'Quick-screw and push-in fittings speed up panel assembly. Confirm media and pressure — push-to-connect suits air, not steam.',
    title: 'Stainless Steel Tube Fittings',
    shortTitle: 'Quick-Screw Fittings',
    h1: 'Stainless Steel Quick-Screw & Push Tube Fittings',
    description:
      'Quick-screw, push-to-connect and barb stainless steel tube fittings for air and light fluid lines. Fast install without flaring.',
    keyword: 'stainless steel tube fittings',
    match: ['quick-screw', 'push-in', 'push-to-connect', 'barb'],
  },
  {
    slug: 'pipe-fittings',
    intro:
      'These complete the manifold: plugs, adapters, tees, silencers and throttle valves. List every thread standard in the BOM, not just one.',
    title: 'Stainless Steel Pipe Fittings & Plugs',
    shortTitle: 'Adapters & Plugs',
    h1: 'Stainless Steel Adapters, Plugs & Threaded Fittings',
    description:
      'Threaded adapters, plugs, caps, silencers, throttle valves and Y/T tees to complete stainless instrumentation manifolds.',
    keyword: 'stainless steel fittings',
    match: [
      'plug',
      'adapter',
      'male-female',
      'female threaded tee',
      'weld straight',
      'silencer',
      'throttle',
      'y-type',
      'tee fitting',
    ],
  },
  {
    slug: 'instrumentation-tubing',
    intro:
      'Tube and clamps go with the compression series. State wall thickness and finish (BA, annealed, or standard) with the OD.',
    title: 'Stainless Steel Instrumentation Tubing',
    shortTitle: 'Tube & Clamps',
    h1: 'Stainless Steel BA Tube, Coil Tube & Clamps',
    description:
      'BA tube, precision tube, coil tube and tube clamps for instrumentation tubing runs. Pair with FerruleX compression fittings.',
    keyword: 'instrumentation fittings',
    match: ['ba tube', 'precision tube', 'coil tube', 'tube clamp'],
  },
  {
    slug: 'cast-fittings',
    intro:
      'Investment-cast bodies suit general process connections. Tell us the casting size and port style; machining tolerance is confirmed at RFQ.',
    title: 'Stainless Steel Cast Fittings',
    shortTitle: 'Cast Fittings',
    h1: 'Investment Cast Stainless Steel Fittings',
    description:
      'Investment-cast stainless elbows, tees and caps for general process connections. SS304 / SS316 options.',
    keyword: 'stainless steel fittings',
    match: ['investment cast'],
  },
];

export function categoryFromTitle(title: string): CategoryDef {
  const t = title.toLowerCase();
  for (const cat of PRODUCT_CATEGORIES) {
    if (cat.match.some(m => t.includes(m))) return cat;
  }
  return PRODUCT_CATEGORIES.find(c => c.slug === 'pipe-fittings')!;
}

export function getCategory(slug: string): CategoryDef | undefined {
  return PRODUCT_CATEGORIES.find(c => c.slug === slug);
}

/** Flat product URL: /products/{slug}/ — category stays in breadcrumbs, not the path. */
export function productPath(_category: string, slug: string): string {
  return `/products/${slug}/`;
}

export function categoryPath(slug: string): string {
  return `/products/${slug}/`;
}

export function productsHubPath(): string {
  return '/products/';
}
