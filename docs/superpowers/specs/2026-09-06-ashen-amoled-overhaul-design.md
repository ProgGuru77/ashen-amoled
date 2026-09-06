# Ashen AMOLED (v2.0) — Technical Design Specification

## Overview
Overhaul of the **Ashen AMOLED** Vencord/Discord CSS theme. The goal is to eliminate redundant `!important` declarations, decouple heavy Base64 font data into standalone font assets, fix video stream overlay occlusion (the "black box" bug), and structure the stylesheet into clean, hash-resilient modules using **Approach 2: High-Specificity ID Prefixing (`#app-mount`)**.

---

## 1. Architectural Strategy

### 1.1 High-Specificity ID Prefixing (`#app-mount`)
* Discord components use standard class selectors (e.g., `.chatContent_a7d72e` with specificity `0-1-0`).
* By anchoring rules with `#app-mount [class*="target_"]`, specificity increases to `1-1-0` (or `1-2-0` for compound selectors).
* This naturally supersedes Discord's compiled rules in the CSS cascade without requiring `!important`.
* `!important` is preserved exclusively for:
  - Overriding inline HTML `style=""` attributes injected dynamically by React.
  - Native browser scrollbar overrides (`scrollbar-width`).
  - Scoped pseudo-elements that fight high-priority Discord CSS animations.

### 1.2 Font Decoupling & Asset Management
* **Decoded Font Binaries:** Decode the provided Base64 strings into:
  - `fonts/Cinzel-SemiBold.woff2` (Weight 600)
  - `fonts/Cinzel-Bold.woff2` (Weight 700)
* **Modular Font Stylesheet (`fonts.css`):**
  - Defines `@font-face` rules for `Cinzel` referencing the local font files with format `woff2`.
  - Also includes fallback data URIs so the theme works seamlessly both locally and if packaged as a standalone bundle.
* **Main Theme Import:** `ashen-amoled.theme.css` begins with `@import url('./fonts.css');`.

### 1.3 Stream & Video Call Transparency Shield
* **Root Cause of Black Box:** Discord's stream participant tile strip on the top right uses the utility classes `scrollerBase_ none_`. Global rules targeting `[class*="none_"]` or unscoped scroller backgrounds accidentally painted solid black over this floating overlay.
* **Resolution:**
  - Scope all server-rail scroller rules exclusively to `nav[class*="guilds_"]`.
  - Add explicit transparency shields for call wrappers:
    ```css
    #app-mount [class*="callContainer_"],
    #app-mount [class*="participantsWrapper_"],
    #app-mount [class*="videoControls_"],
    #app-mount [class*="gradientContainer_"],
    #app-mount [class*="videoWrapper_"] {
      background: transparent;
      background-color: transparent;
    }
    ```

---

## 2. File Organization

```
bold-heisenberg/
├── fonts/
│   ├── Cinzel-SemiBold.woff2   # Extracted WOFF2 binary (weight 600)
│   └── Cinzel-Bold.woff2       # Extracted WOFF2 binary (weight 700)
├── fonts.css                   # Font-face declarations & CSP bypass
└── ashen-amoled.theme.css      # Refactored, segmented theme file
```

---

## 3. Theme Segmentation

1. **Meta & Imports:** Theme header metadata and `@import url('./fonts.css');`.
2. **Tokens & Palette:** Color variables, modern semantic tokens (`--bg-base-*`), legacy fallbacks (`--background-*`).
3. **App Base & Titlebar:** `#app-mount`, window frame, title bar chrome.
4. **Scrollbars & Gutter Protection:** Consolidated thin red scrollbars and horizontal overflow lock.
5. **Guilds Rail (Server List):** Server icons, folders, ember indicators (scoped to `nav[class*="guilds_"]`).
6. **Channels & DM Sidebar:** Category headings (Cinzel), channel items, active gradients.
7. **Chat Pane & Composer:** Messages, mentions, code blocks, search bar, text area focus glow.
8. **Badges, Buttons & Interactive Elements:** Quick reactions, filled buttons, boost progress bars.
9. **User Profiles & Material Badges:** Profile modals, activity badges, pills.
10. **Stream & Video Call Overlays:** Full transparency guarantees for active video and screen shares.
11. **Expression Picker & Settings:** Emojis/GIFs popout, user settings panel and navigation.

---

## 4. Verification & Testing Plan
* Verify that `Cinzel-SemiBold.woff2` and `Cinzel-Bold.woff2` are valid non-empty WOFF2 binaries.
* Verify syntax and specificity hierarchy of `ashen-amoled.theme.css`.
* Confirm `!important` count drops from 165+ down to < 20.
* Confirm stream overlay classes have transparent backgrounds.
