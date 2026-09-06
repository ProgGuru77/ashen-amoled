# Discord Theme Architecture & Best Practices Specification

> **Reference Repository:** [Ash1421/Midnight-Ash](https://github.com/Ash1421/Midnight-Ash)  
> **Target Audience:** Theme Authors, Maintainers, and Client Mod Developers (Vencord, Equicord, BetterDiscord)  
> **Status:** Authoritative Specification & Practical Handbook

---

## 1. Architectural Philosophy: Modular Stacking vs. Self-Contained

Modern client-mod theming balances two primary architectural approaches:

```
+-----------------------------------------------------------------------------------+
| APPROACH A: Modular Composition (Midnight-Ash Model)                              |
|   - Base CSS framework (@import refact0r/midnight)                                |
|   - Addon Layering (RadialStatus, SettingsModal, HorizontalServerList, AppleEmoji) |
|   - Declarative Variable Configuration (User controls layout & color tokens)      |
+-----------------------------------------------------------------------------------+
| APPROACH B: Autonomous High-Specificity Engine (Ashen AMOLED Model)               |
|   - Single self-contained stylesheet with local decoupled assets                  |
|   - Direct `#app-mount` specificity overrides (1-1-0)                             |
|   - Resilient DOM matching with zero external runtime dependencies                 |
+-----------------------------------------------------------------------------------+
```

### 1.1 When to Use Each Model
- **Use Modular Composition (Approach A)** when building an ecosystem theme where users mix-and-match community addons (e.g., custom emoji sets, radial status rings, modal settings).
- **Use Autonomous Engine (Approach B)** when building high-performance, offline-first, or pure AMOLED themes that must guarantee 100% style stability without being subject to third-party CDN downtime or breaking changes in upstream imports.

---

## 2. Color Engineering: Perceptually Uniform Palettes with OKLCH & `color-mix()`

### 2.1 The Flaw of Traditional Hex / HSL in Dark Themes
Standard Hex (`#111111`) and standard `hsl()` suffer from perceptual non-uniformity: two colors with identical saturation/lightness numbers can appear dramatically different in perceived brightness to the human eye. In pure AMOLED themes, this leads to muddy greys, glaring highlights, and illegible text contrast.

### 2.2 The OKLCH Color Scale Standard (Learned from Midnight-Ash)
Establish 5-step uniform scales for each accent hue using `oklch(lightness chroma hue)`:

```css
:root {
  /* Red Ramp: Hue 0deg */
  --red-1: oklch(75% 0.12 0deg);
  --red-2: oklch(70% 0.12 0deg);
  --red-3: oklch(65% 0.12 0deg);
  --red-4: oklch(60% 0.12 0deg);
  --red-5: oklch(55% 0.12 0deg);

  /* Purple Ramp: Hue 310deg */
  --purple-1: oklch(75% 0.11 310deg);
  --purple-2: oklch(70% 0.11 310deg);
  --purple-3: oklch(65% 0.11 310deg);
  --purple-4: oklch(60% 0.11 310deg);
  --purple-5: oklch(55% 0.11 310deg);

  /* Green Ramp: Hue 170deg */
  --green-1: oklch(75% 0.11 170deg);
  --green-2: oklch(70% 0.11 170deg);
  --green-3: oklch(65% 0.11 170deg);
  --green-4: oklch(60% 0.11 170deg);
  --green-5: oklch(55% 0.11 160deg);
}
```

### 2.3 Dynamic Alpha Blending with `color-mix()`
Avoid hardcoded RGBA / Hex alpha values (e.g., `rgba(255, 42, 75, 0.12)`). Use CSS `color-mix()` to derive translucent overlays directly from parent tokens:

```css
/* Smooth mention background fade */
--mention: linear-gradient(
  to right,
  color-mix(in hsl, var(--accent-crimson), transparent 90%) 40%,
  transparent
);

--mention-hover: linear-gradient(
  to right,
  color-mix(in hsl, var(--accent-crimson), transparent 95%) 40%,
  transparent
);
```

---

## 3. Discord Native Token Exploitation (Zero-Selector Theming)

One of the most powerful techniques in `Midnight-Ash` is overriding Discord's compiled Design System Tokens directly on `:root` and `.theme-dark`. By supplying tokens, you restyle hundreds of components **without writing a single class selector**.

### 3.1 Essential Token Dictionary

| Category | Token Variable | Purpose in Discord |
| :--- | :--- | :--- |
| **Interactive Modifiers** | `--background-modifier-hover` | Channel items, member list items hover background |
| | `--background-modifier-active` | Selected channel, pressed button states |
| | `--background-modifier-selected` | Currently active DM / channel background |
| | `--background-modifier-accent` | Category indicators and divider highlights |
| **Message Stream** | `--background-message-hover` | Message line hover effect |
| | `--card-primary-bg` | Pinned messages, thread preview cards |
| **Modals & Cards** | `--modal-background` | Dialog popup backgrounds |
| | `--modal-footer-background` | Modal action button footers |
| **Scrollbars** | `--scrollbar-auto-thumb` | Scroller handle color |
| | `--scrollbar-thin-thumb` | Compact sidebar scroller handles |
| **Presence States** | `--online`, `--idle`, `--dnd`, `--streaming` | Avatar status indicator dots and rings |

### 3.2 Implementation Example
```css
:root,
.theme-dark,
#app-mount {
  /* Modifier tokens */
  --background-modifier-hover: hsl(0deg 0% 100% / 3%);
  --background-modifier-active: hsl(0deg 0% 100% / 6%);
  --background-modifier-selected: hsl(0deg 0% 100% / 8%);
  
  /* Modal tokens */
  --modal-background: #080808;
  --modal-footer-background: #030303;

  /* Presence tokens */
  --online: oklch(70% 0.11 170deg);
  --idle: oklch(75% 0.11 90deg);
  --dnd: oklch(70% 0.12 0deg);
  --streaming: oklch(70% 0.11 310deg);
}
```

---

## 4. Specificity Engineering & The "Zero `!important`" Rule

### 4.1 The Specificity Cascade Hierarchy
1. **Level 1 (Tokens):** `:root` and `.theme-dark` tokens handle 70% of colors. Specificity: `0-1-0`.
2. **Level 2 (Prefixing):** `#app-mount [class*="component_"]` provides specificity `1-1-0`. Discord's internal component rules are `0-1-0`. This guarantees your theme wins naturally without `!important`.
3. **Level 3 (Legitimate `!important`):** Reserved strictly for:
   - Defeating React inline `style=""` tags.
   - Forcing browser vendor resets (`scrollbar-width: thin !important;`).
   - Discord's hardcoded badge counts.

### 4.2 The Cascade Shorthand Trap (Anti-Pattern)
**Never** declare a general shorthand after a specific property:

```css
/* BROKEN: 'border' shorthand wipes out 'border-left-color' */
#app-mount [class*="embedFull_"] {
  border-left-color: var(--accent);
  border: 1px solid var(--subtle); /* Resets border-left-color! */
}

/* CORRECT: General shorthand first, specific accent second */
#app-mount [class*="embedFull_"] {
  border: 1px solid var(--subtle);
  border-left: 3px solid var(--accent);
}
```

---

## 5. Resilient Selector Targeting: Surviving Discord Updates

Discord uses dynamic CSS Modules that append ephemeral 5–7 character hashes to class names (e.g., `.chatContent_a7d72e`).

### 5.1 Selector Guidelines
1. **Never use exact class names:** `.chatContent_a7d72e` will break upon Discord's next release.
2. **Always use wildcard prefix matching:** `[class*="chatContent_"]`.
3. **Compound selectors for precision:** When two elements share a prefix, combine them:
   ```css
   /* Targets the title container without affecting other containers */
   #app-mount [class*="title_"][class*="container_"] { ... }
   ```
4. **Scope navigation elements:** Never target `[class*="scroller_"]` globally. Always qualify with its parent landmark:
   ```css
   #app-mount nav[class*="guilds_"] [class*="scroller_"] { ... }
   ```

---

## 6. Stream & Video Overlay Shielding (The "Black Box" Bug)

A widespread issue in dark/AMOLED themes is floating stream tiles or participant cameras becoming occluded by solid black boxes.

### 6.1 The Root Cause
Discord's video call participant strip uses the layout class `none_` on its floating scroller. Themes applying global background resets to `[class*="none_"]` or unscoped scrollers inadvertently render an opaque box over the video feed.

### 6.2 The Universal Shield Rule
Always include an explicit zero-opacity shield for all video and call containers:

```css
#app-mount [class*="callContainer_"],
#app-mount [class*="wrapper_"][class*="video_"],
#app-mount [class*="videoWrapper_"],
#app-mount [class*="streamWrapper_"],
#app-mount [class*="focusedVideo_"],
#app-mount [class*="videoGrid_"],
#app-mount [class*="videoGridWrapper_"],
#app-mount [class*="tileChild_"],
#app-mount [class*="participantsWrapper_"],
#app-mount [class*="participantsWrapper_"] [class*="scrollerBase_"],
#app-mount [class*="participantsWrapper_"] [class*="scroller_"],
#app-mount [class*="verticalScroller_"],
#app-mount [class*="videoControls_"],
#app-mount [class*="topControls_"],
#app-mount [class*="gradientContainer_"],
#app-mount [class*="bottomControls_"] {
  background: transparent;
  background-color: transparent;
}
```

---

## 7. Declarative Configuration & Feature Flags

As demonstrated by `Midnight-Ash`, top-tier themes provide human-readable toggles at the top of the stylesheet for easy user customization:

```css
:root {
  /* Layout & Sizing */
  --gap: 12px;
  --divider-thickness: 4px;
  --border-thickness: 1px;
  --top-bar-height: var(--gap);

  /* Feature Toggles: 'on' or 'off' */
  --animations: on;
  --custom-window-controls: on;
  --panel-blur: off;
  --blur-amount: 12px;

  /* Transitions */
  --list-item-transition: 0.2s ease;
  --border-hover-transition: 0.2s ease;
}
```

---

## 8. Asset Independence & CSP (Content Security Policy) Compliance

1. **Standalone Font Assets:** Never embed massive Base64 data strings into theme CSS. Extract WOFF2 binaries into `fonts/` and link via `fonts.css` with `@font-face`.
2. **CSP Safety:** Discord client mods restrict loading external assets from unapproved domains. Local relative paths (`./fonts/font.woff2`) or trusted domain paths (GitHub raw / custom domains) ensure zero font-blocking errors.
3. **SVG Icons:** Prefer CSS mask icons or clean SVG data-URIs over heavy icon libraries.

---

## 9. Quality Assurance & Continuous Verification Pipeline

Every production theme repository should maintain automated pre-flight testing scripts:

1. **AST & Hash Linting:** Assert that zero brittle build hashes (`_[a-z0-9]{5,7}\b`) exist in the theme file.
2. **Specificity & `!important` Gate:** Automated test enforcing that `!important` count remains strictly capped (e.g., `< 10`).
3. **Stream Shield Audit:** Automated assertion confirming all stream transparency selectors are intact.
4. **Stylelint Standard (`.stylelintrc.json`):** Standardize formatting, vendor prefixing, and color syntax across contributions.
5. **Release Packaging (`scripts/package_release.py`):** Automatically run all pre-flight checks, verify assets, and bundle the theme into a versioned zip with SHA-256 integrity checksums.
