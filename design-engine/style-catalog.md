# Design Style Catalog

Every style follows the same contract: philosophy; visual, typography, and color guidance; components/layout; interaction/motion; CSS approach; responsive behavior; accessibility/performance; anti-pattern.

## Styles

| Style | Philosophy and visual language | Type / color | Components, layout, interaction, CSS | Responsive, accessibility, performance, anti-pattern |
|---|---|---|---|---|
| Skeuomorphism | Familiar physical metaphors and tactile surfaces | Humanist sans; material neutrals | Textured controls, layered panels, CSS gradients/shadows; direct manipulation | Simplify texture on mobile, preserve labels/contrast, avoid raster-heavy decoration |
| Minimalism | Reduce noise and emphasize task hierarchy | Neutral sans; restrained semantic palette | Whitespace, clear cards, CSS tokens and borders; purposeful transitions | Keep hierarchy explicit, support zoom/focus, avoid hiding useful context |
| Glassmorphism | Translucent depth and layered context | Geometric sans; strong opaque text roles | Backdrop blur with solid fallback, floating surfaces; restrained fade | Stack surfaces on small screens, verify contrast without blur, cap blur layers |
| Claymorphism | Soft, friendly dimensional objects | Rounded sans; warm pastels | Large radius, soft shadows, tokenized surfaces; gentle scale | Reduce shadows on small devices, visible focus, avoid low-contrast pastel controls |
| Neumorphism | Inset/extruded single-surface controls | Clear sans; high-contrast accents | Paired shadows and solid fallback; tactile press states | Add borders and labels, reduce shadow cost, never rely on shadow alone |
| Neo-brutalism | Deliberate raw structure and strong contrast | Display plus readable sans; bold blocks | Thick borders, offset shadows, grid; direct hover states | Stack blocks, maintain target sizes, avoid arbitrary decoration |
| Bento Grid | Modular information grouping (layout system) | Product-appropriate sans; semantic roles | CSS grid, named areas, bounded cards; progressive disclosure | Collapse to ordered list, preserve reading order, avoid forced mosaics |
| Retro Y2K | Optimistic digital nostalgia | Display type with fallback; bright chrome/neon | CSS gradients, badges, pixel accents; playful motion | Keep navigation conventional, reduce animation, avoid illegible novelty |
| Liquid Glass | Fluid premium surfaces and motion | Variable sans; translucent accents with opaque roles | Blur/gradient tokens, transform motion, solid fallback | Reduced-motion path, contrast fallback, limit GPU-heavy filters |
| Flat Design | Clear hierarchy without ornamental depth | Accessible sans; semantic contrast | Color, spacing, borders, CSS variables; direct feedback | Strong focus and labels, low rendering cost, avoid ambiguous color-only states |
| Material Design | Evidence-based surfaces and roles | Roboto-like sans; semantic roles | Elevation, components, responsive grid; state transitions | Follow keyboard/platform semantics, use token roles, avoid arbitrary elevation |
| Material You | User-adaptive expressive theming | Variable sans; dynamic semantic palette | Shape/color tokens, adaptive components; contextual motion | Contrast-test generated themes, reduce motion, keep stable structure |
| Fluent Design | Depth, light, and enterprise clarity | Segoe-like sans; neutral semantic roles | Reveal/focus, acrylic fallback, responsive layout | Preserve keyboard affordances, cap effects, avoid acrylic-only legibility |
| Swiss Style | Rational grid and typographic clarity | Grotesk sans; limited accent | Grid, alignment, typography, CSS layout; measured transitions | Reflow grid, preserve reading order, avoid tiny type |
| Editorial Design | Storytelling and hierarchy for content | Serif/sans pairing; contextual palette | Columns, pull quotes, CSS grid; scroll cues | Single-column fallback, semantic headings, avoid dense decorative imagery |
| Brutalism | Raw directness and anti-polish | Monospace/display; high contrast | Native controls, borders, minimal CSS; abrupt states | Keep semantics and focus, low cost, avoid hostile usability |
| Dark OLED | Dark-first power-efficient surfaces | Readable sans; near-black semantic layers | CSS dark tokens, limited borders; subtle transitions | Offer light mode, avoid pure-black low contrast, minimize glow and repaint |
| Cyberpunk | High-energy technical identity | Display/mono pairing; neon accents | Glows, grids, CSS gradients; purposeful motion | Static fallback, contrast-test neon, avoid constant animation and blur |
| Retro-futurism | Historical future imagined through technology | Geometric display; muted metallic accents | Panels, grids, CSS shapes; staged transitions | Maintain familiar controls, reduce decorative layers, avoid skeuomorphic clutter |
| Organic UI | Natural shapes and calm rhythm | Humanist rounded type; earthy palette | Irregular radius, fluid CSS shapes; gentle motion | Ensure predictable focus/order, constrain filters, avoid decorative ambiguity |
| Maximalism | Intentional abundance and expressive layering | Strong display plus utility sans; broad palette | Layered tokens, dense composition; choreographed motion | Establish hierarchy, reduced-motion mode, avoid overload and low contrast |
| Gradient Mesh | Atmospheric color fields supporting content | Neutral type; accessible semantic overlays | CSS gradients or optimized assets; restrained transitions | Use solid fallback, check contrast over every region, avoid large animated meshes |
| Aurora UI | Soft luminous ambient emphasis | Clean sans; cool semantic accents | Gradient backgrounds, glass fallback; slow ambient motion | Disable animation, cap blur, never use glow as status communication |
| Data-dense Enterprise UI | Fast scanning and operational accuracy | Compact readable sans; semantic status colors | Tables, split panes, filters, CSS density tokens; immediate feedback | Responsive column strategy, keyboard-first, avoid decorative whitespace loss |
| Motion-first UI | Motion communicates state and continuity | Variable sans; high-contrast roles | Transform/opacity with CSS/WAAPI; choreographed transitions | Reduced-motion equivalent, avoid layout thrash, motion never sole feedback |
| AI-native Interfaces | Transparent collaboration and controllability | Readable sans/mono for data; calm semantic palette | Prompt/work queues, citations, streaming states; progressive disclosure | Keyboard and screen-reader status, bounded streaming, avoid anthropomorphic deception |

Use [`README.md`](./README.md) for selection constraints and [`combinations.md`](./combinations.md) for compatibility rules.
