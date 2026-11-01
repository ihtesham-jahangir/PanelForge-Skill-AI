# Design System Generation

Generate and persist:

- Semantic color tokens with light/dark values and contrast checks.
- Typography families, sizes, weights, line heights, and truncation rules.
- Spacing scale, container widths, grid, breakpoints, radius, borders, and elevation.
- Component contracts and states: default, hover, focus, active, selected, disabled, loading, success, error, and empty.
- Interaction and motion durations with reduced-motion behavior.
- Responsive rules for navigation, tables, forms, charts, dialogs, and dense content.

Prefer the host project's token mechanism. Otherwise use namespaced CSS custom properties such as `--pf-color-surface` and `--pf-space-4`. Keep semantic tokens separate from raw palette values so themes can change without rewriting components.
