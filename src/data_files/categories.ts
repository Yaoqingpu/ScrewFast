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

/**
 * Category order follows the Shengquan selection-manual series
 * (corrugated hose → compression → quick-screw → plugs/barbs → adapters/weld →
 *  ball → needle → check → tubing → push-to-connect → cast → custom).
 */
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
    slug: 'compression-fittings',
    intro:
      'Measure tube OD exactly (metric or inch). A double-ferrule joint is sized by tube, so the OD plus the port thread decides the part.',
    title: 'Stainless Steel Compression Fittings',
    shortTitle: 'Compression Fittings',
    h1: 'Stainless Steel Compression Fittings (Double Ferrule)',
    description:
      'Double-ferrule connectors, elbows, tees, unions, bulkheads, ground-finish and forged series. Metric and inch tube. NPT, G and metric threads.',
    keyword: 'stainless steel compression fittings',
    match: [
      'compression',
      'ground finish',
      'forged',
      'cylinder connector',
      'bulkhead union',
    ],
  },
  {
    slug: 'quick-screw-fittings',
    intro:
      'Quick-screw fittings speed panel work with a nut-and-ferrule bite on soft or hard tube. Confirm OD and thread gender on the RFQ.',
    title: 'Stainless Steel Quick-Screw Fittings',
    shortTitle: 'Quick-Screw',
    h1: 'Stainless Steel Quick-Screw Tube Fittings',
    description:
      'Quick-screw straight, female, union, elbow, tee and bulkhead connectors for air and light fluid lines. Separate from push-to-connect series.',
    keyword: 'quick screw fittings',
    match: ['quick-screw', 'push-in quick-screw'],
  },
  {
    slug: 'plugs-and-barbs',
    intro:
      'Plugs close unused ports; barb ends take hose. List every thread standard in the BOM so the blank matches the manifold.',
    title: 'Stainless Steel Plugs & Barb Fittings',
    shortTitle: 'Plugs & Barbs',
    h1: 'Stainless Steel Plugs, Caps & Barb Hose Fittings',
    description:
      'Hex plugs, flanged plugs, square plugs, compression plug kits, ferrules, barb hose connectors, silencers and throttle valves.',
    keyword: 'stainless steel plug fitting',
    match: ['plug', 'barb', 'silencer', 'throttle', 'ferrule'],
  },
  {
    slug: 'adapters-and-weld',
    intro:
      'Adapters and weld ends finish mixed-thread manifolds. Send both end standards when the two sides differ.',
    title: 'Stainless Steel Adapters & Weld Fittings',
    shortTitle: 'Adapters & Weld',
    h1: 'Stainless Steel Thread Adapters & Weld Connectors',
    description:
      'Male-female adapters, elbows, tees, weld straight connectors and Y/T branch fittings for instrumentation manifolds.',
    keyword: 'stainless steel adapter fitting',
    match: [
      'adapter',
      'male-female',
      'weld straight',
      'female threaded tee',
      'y-type',
      'tee fitting',
    ],
  },
  {
    slug: 'ball-valves',
    intro:
      'Pick the end first (compression, female thread or weld), then the flow pattern. Pressure class and seat material are confirmed on the quote, not assumed.',
    title: 'Stainless Steel Ball Valves',
    shortTitle: 'Ball Valves',
    h1: 'Stainless Steel Ball Valves & Manifolds',
    description:
      'Shutoff valves with compression, female thread or weld ends — straight, angle, 3-way, mini, high-pressure and valve manifolds. Confirm the pressure class on the quote.',
    keyword: 'stainless steel ball valve',
    match: ['ball valve', 'valve manifold'],
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
    slug: 'push-to-connect',
    intro:
      'Push-to-connect is for compatible tube OD and hardness — typically air and light utilities, not steam. Confirm OD before ordering.',
    title: 'Stainless Steel Push-to-Connect Fittings',
    shortTitle: 'Push-to-Connect',
    h1: 'Stainless Steel Push-to-Connect (Push-In) Fittings',
    description:
      'Push-in straight, elbow, union and bulkhead fittings for rapid tube changes on pneumatic and utility lines. Separate series from quick-screw.',
    keyword: 'push to connect stainless fitting',
    match: ['push-to-connect', 'push-in'],
  },
  {
    slug: 'cast-fittings',
    intro:
      'Investment-cast bodies suit general process connections. Tell us the casting size and port style; machining tolerance is confirmed at RFQ.',
    title: 'Stainless Steel Cast Fittings',
    shortTitle: 'Cast Fittings',
    h1: 'Investment Cast Stainless Steel Fittings',
    description:
      'Investment-cast stainless elbows, tees, straights, unions, caps and cast ball valves for general process connections. SS304 / SS316.',
    keyword: 'investment cast stainless fitting',
    match: ['investment cast'],
  },
  {
    slug: 'custom-fittings',
    intro:
      'Non-standard parts from the custom page of the factory manual. Send a drawing or photo with size, grade and quantity for a manufacturability review.',
    title: 'Custom & Non-Standard Fittings',
    shortTitle: 'Custom / Non-Standard',
    h1: 'Custom & Non-Standard Stainless Steel Fittings',
    description:
      'Factory custom and non-standard stainless fittings — special elbows, tees, valve bodies and machined parts beyond the stocked catalog lines.',
    keyword: 'custom stainless steel fittings',
    match: ['custom', 'non-standard', 'nonstandard'],
  },
];

export function categoryFromTitle(title: string): CategoryDef {
  const t = title.toLowerCase();
  for (const cat of PRODUCT_CATEGORIES) {
    if (cat.match.some(m => t.includes(m))) return cat;
  }
  return PRODUCT_CATEGORIES.find(c => c.slug === 'adapters-and-weld')!;
}

export function getCategory(slug: string): CategoryDef | undefined {
  // Legacy slugs from earlier IA — keep bookmarks working
  const aliases: Record<string, string> = {
    'tube-fittings': 'quick-screw-fittings',
    'pipe-fittings': 'adapters-and-weld',
  };
  const resolved = aliases[slug] ?? slug;
  return PRODUCT_CATEGORIES.find(c => c.slug === resolved);
}

/** Flat product URL: /products/{slug}/ — category stays in breadcrumbs, not the path. */
export function productPath(_category: string, slug: string): string {
  return `/products/${slug}/`;
}

export function categoryPath(slug: string): string {
  const aliases: Record<string, string> = {
    'tube-fittings': 'quick-screw-fittings',
    'pipe-fittings': 'adapters-and-weld',
  };
  return `/products/${aliases[slug] ?? slug}/`;
}

export function productsHubPath(): string {
  return '/products/';
}
