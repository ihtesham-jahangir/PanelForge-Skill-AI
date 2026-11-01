# Design Intelligence Engine

## Selection procedure

Choose a primary visual language from product category, industry, brand personality, audience, information density, accessibility needs, responsive constraints, and technical feasibility. Choose at most one secondary visual influence. Bento Grid is a layout system, not a visual style, and may complement a primary style.

Produce a persistent design specification using [`templates/design-system.md`](../templates/design-system.md). Define tokens before components and reuse the same tokens across admin, user, and CRM surfaces.

## Style catalogue

| Style | Best fit | Implementation cautions |
|---|---|---|
| Skeuomorphism | specialized tools and physical-product metaphors | avoid decorative texture that harms contrast |
| Minimalism | focused SaaS and productivity | preserve hierarchy; do not remove useful context |
| Glassmorphism | premium portals and focused overlays | maintain opaque fallback and readable contrast |
| Claymorphism | friendly consumer workflows | control shadows and motion for performance |
| Neumorphism | small, low-density controls | insufficient contrast is a common failure |
| Neo-brutalism | expressive products and internal tools | use intentional hierarchy, not random borders |
| Bento Grid | analytics and modular summaries | define responsive stacking; do not force mosaic layouts |
| Retro Y2K | entertainment and youth brands | keep forms and navigation conventional |
| Liquid Glass | premium, motion-led experiences | provide reduced-motion and solid-color fallbacks |
| Flat Design | accessible enterprise and CRUD systems | use spacing, labels, and states instead of shadows |
| Material / Material You | Android-aligned and tokenized products | follow semantic color roles and platform behavior |
| Fluent | Microsoft ecosystem and enterprise | maintain keyboard and density consistency |
| Swiss / Editorial | content-heavy and data storytelling | verify small-screen reading order |
| Dark OLED | dark-mode focused products | avoid pure black text-on-dark contrast traps |
| Cyberpunk / retro-futurism | technical and entertainment products | constrain glow and animation |
| Organic UI / maximalism / aurora | expressive brand surfaces | keep task flows restrained |
| Data-dense enterprise | operations and CRM | prioritize scanability, filters, and keyboard use |
| Motion-first / AI-native | assistants and real-time workflows | motion cannot be the only feedback channel |

For every chosen style document philosophy, typography, palette, components, layout, interaction and motion, responsive behavior, accessibility, performance, and anti-patterns. Never mix incompatible shadows, radii, density, or type scales without a stated reason.
