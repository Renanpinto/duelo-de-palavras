---
version: alpha
name: Duelo de Palavras
description: Jogo de palavras em português com clima de placar noturno e destaque para o tabuleiro.
colors:
  primary: "#b7a0ff"
  secondary: "#f09bb0"
  background: "#0d1019"
  surface: "#151a28"
  surface-raised: "#20273a"
  text: "#f6f3ed"
  muted: "#a6adbd"
  border: "#30384d"
  success: "#52c995"
  warning: "#e3b95f"
  absent: "#3c4558"
  focus: "#d4c6ff"
typography:
  sans:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
  utility:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
rounded:
  sm: "0.5rem"
  md: "0.75rem"
  lg: "1rem"
  xl: "1.25rem"
spacing:
  page-max: "35rem"
  board-gap: "0.4375rem"
  control-gap: "0.625rem"
components:
  tile: { }
  key: { }
  button: { }
  dialog: { }
---

# Duelo de Palavras Design System

## Overview

### Creative North Star

The game should feel like a compact late-night word arena: a quiet ink-blue room, a framed letter board, and two expressive team colors. The board is the central artifact, like a small illuminated scoreboard rather than a generic app card.

### Product context and register

- **Audience and primary job:** Portuguese-speaking casual players who want to start a quick word challenge and understand each guess at a glance.
- **Target market(s) and evidence:** Brazil is the language context, based on `index.html` using `pt-BR`; no additional market behavior is assumed.
- **Locale(s) and language policy:** Brazilian Portuguese. Normalize diacritics for matching while displaying uppercase letters.
- **Usage scene:** Short, repeatable sessions on phones, with the same page also usable on desktop.
- **Register:** Casual product with a small amount of game-show energy.
- **Memorable signature:** A luminous, framed word grid with a lilac selection ring and green/gold result tiles.
- **Restraint:** Keep category and length controls, instructions, and statistics quiet so the active row stays dominant.
- **Anti-references:** Generic SaaS dashboards, excessive glass blur, decorative gradients on every control, and tiny low-contrast game tiles.
- **Token ownership/runtime mapping:** This file mirrors the CSS custom properties in `index.html`; inline application CSS remains canonical. Keep palette changes synchronized with `:root` and the visual overrides in that file. No generator or theme adapter is used.

## Colors

The ink background (`background`) keeps the board immersive. `surface` and `surface-raised` separate the board frame and controls. Lilac (`primary`) marks focus and the main action; rose (`secondary`) is a restrained brand accent. Green (`success`) and gold (`warning`) communicate letter feedback, while `absent` remains distinct from the page background. Text and muted copy maintain a clear hierarchy. Focus uses a light lilac outline, never color alone.

## Typography

Use the system sans stack for Portuguese copy and controls, with weight contrast for the title and letter tiles. Letter tiles are uppercase and centered. The utility monospace stack is reserved for compact numeric or diagnostic content. Keep body copy conversational and short; allow system fallback fonts to render accents.

## Layout

The game uses a centered column capped at 35rem, with the title and controls aligned to the board. The board width follows the selected word length and remains capped at 30rem; its grid uses equal columns. On narrow screens, reduce gaps and padding while preserving legible tile dimensions and reachable keys. The document scrolls naturally and respects device safe areas.

## Elevation & Depth

Use subtle tonal panels and one soft shadow around the board and primary action. Keep tiles mostly flat so green, gold, and gray feedback remains easy to read. Dialog backdrops may blur the page; ordinary panels should not.

## Shapes

Controls use rounded rectangles, the board frame uses a larger radius, and tiles use compact rounded corners. Selection is shown with a lilac border and glow. Keep outlines crisp against the dark surfaces.

## Components

### Foundational visual states

Buttons and selectable tiles have visible hover and focus-visible states, a pressed response, and stable dimensions. Reduced-motion preferences remove nonessential animation. Correct, present, and absent letters use the semantic green, gold, and slate tokens.

### Buttons and actions

The lilac gradient is reserved for the primary action. Secondary actions use a bordered raised surface. Keyboard keys are compact, high-contrast buttons; Enter and delete remain wider and visibly labeled.

### Navigation and data display

There is one game surface, no navigation shell. Statistics stay in four compact cards below the board. The board uses one equal-width column per letter and six attempt rows.

### Forms and overlays

Category and word length use native selects because the option sets are short and platform-owned selection is acceptable. Help and result states use native `dialog` elements with app-owned dark styling.

### Iconography

There is no icon library. Use text labels and the existing simple “D” brand mark; do not add decorative icons to letter feedback.

### Motion

Keep the existing brief tile pop and button press feedback. Respect `prefers-reduced-motion`; avoid ambient loops or motion that delays input.

### Content and data visualization

Use Brazilian Portuguese, sentence case, and plain action labels. Letter feedback always has both a color and a text legend. Statistics use tabular figures where supported.

## Do's and Don'ts

- **Do:** Keep the current row and its selected tile visually obvious.
- **Do:** Keep the board as the strongest element on every viewport.
- **Don't:** Use accent color as the only indication of a tile state.
- **Don't:** shrink the keyboard or tiles to fit long copy; let the page scroll instead.
