# 🌑 Ashen AMOLED (v2.2.1)

> A high-contrast, pure AMOLED black theme with Ashen Crimson highlights and Cinzel typography for Discord.

[![Version](https://img.shields.io/badge/version-2.2.1-ff2a4b.svg)](https://github.com/ProgGuru77/ashen-amoled/releases)
[![Clients](https://img.shields.io/badge/clients-Vencord%20%7C%20BetterDiscord-black.svg)](https://vencord.dev)
[![License](https://img.shields.io/badge/license-MIT-red.svg)](#license)
[![OLED Friendly](https://img.shields.io/badge/display-Pure%20AMOLED%20%23000000-000000.svg)](#features)

---

## ✨ Features

- **🖤 Maximum AMOLED Black (`#000000` Default):** 100% true-black background across all chat containers, channels, servers rail, and member lists. Pixels turn completely OFF for optimal OLED efficiency and zero backlight bleed.
- **🔥 Absolute Maximum Crimson Hue:** Laser-vivid Ashen Crimson highlights engineered with peak OKLCH chroma (0.28) for maximum saturation, vibrant glow overlays, and mention banners against true black.
- **🎯 High-Contrast Icon Calibration:** Overrides Discord's native icon tokens (`--icon-primary`, `--channel-icon`, etc.) and provides elevated AMOLED tiles for server circle buttons and reaction badges so icons never look muddy or blend into backgrounds.
- **🏛️ Cinzel Typography:** Classical serif headers for server titles, category channels, and modal windows with bundled local fonts.
- **📹 Glitch-Free Video & Screenshares:** Fully transparent video overlay shields ensure stream feeds and camera calls never get blocked by black boxes.
- **⚡ Fluid Interactions:** Smooth transitions on hover, custom reaction pills, and crimson glow on focused buttons and inputs.
- **🔍 Polished Surfaces:** Custom AMOLED treatments for the Quick Switcher (`Ctrl + K`), search results, chat autocomplete, and the "Active Now" game activity dashboard.
- **💻 Syntax Highlighting:** Refined codeblock styling with crimson keywords, warm accents, and custom inline code tags.
- **⚙️ Simple Customization:** Declarative settings at the top of the stylesheet let you customize corners, adjust transitions, or toggle features in seconds.

---

## 🚀 Quick Install

### Method 1: Vencord Online Theme (Recommended)
1. Open Discord **Settings** -> **Vencord** -> **Themes**.
2. Paste the following URL into the **Online Themes** box:
   ```
   https://raw.githubusercontent.com/ProgGuru77/ashen-amoled/main/ashen-amoled.theme.css
   ```
3. Hit **Enter** and enjoy!

---

### Method 2: Manual / Local Installation

#### For Vencord:
1. Download the latest `ashen-amoled-v2.2.1.zip` from [Releases](https://github.com/ProgGuru77/ashen-amoled/releases).
2. Extract the folder into your Vencord themes directory:
   - **Windows:** `%AppData%\Vencord\themes\ashen-amoled`
   - **Linux:** `~/.config/Vencord/themes/ashen-amoled`
   - **macOS:** `~/Library/Application Support/Vencord/themes/ashen-amoled`
3. Make sure the `fonts/` folder and `fonts.css` are in the same folder as `ashen-amoled.theme.css`.
4. Enable **Ashen AMOLED** in Discord Settings -> **Vencord** -> **Themes**.

#### For BetterDiscord:
1. Download `ashen-amoled.theme.css` and the `fonts/` folder.
2. Place them into your BetterDiscord `themes/` folder.
3. Enable **Ashen AMOLED** in Discord Settings -> **Themes**.

---

## 🎨 Customization

You can easily customize Ashen AMOLED by editing the declarative configuration variables at the top of `ashen-amoled.theme.css`:

```css
:root {
  /* AMOLED Intensity Mode: 'max' (Default: 100% True Black #000000 across all panels) */
  --ashen-amoled-mode: max;

  /* Primary Accent: Absolute Maximum Vivid Crimson (Peak Chroma 0.28) */
  --ashen-accent-crimson: oklch(62% 0.28 22deg);
  --ashen-accent-hover:   oklch(70% 0.28 22deg);
  --ashen-accent-active:  oklch(54% 0.28 22deg);
  --ashen-accent-dark:    oklch(40% 0.24 22deg);

  /* Layout & Corners */
  --ashen-border-radius-sm: 4px;   /* Small badges & reactions */
  --ashen-border-radius-md: 8px;   /* Modals, cards, text areas */
  --ashen-border-radius-lg: 12px;  /* Floating popouts */

  /* Feature Toggles */
  --ashen-animations: on;          /* Smooth button & list transitions */
  --ashen-panel-blur: off;         /* Optional frosted glass effect on panels */
  --ashen-blur-amount: 12px;       /* Strength of frosted blur */
}
```

---

## 📦 Developer & Verification

If you are modifying the theme or building a custom package:

```bash
# Verify theme integrity, zero stream occlusion, and token scales
python scripts/verify_theme.py

# Package a clean distribution zip with checksums into dist/
python scripts/package_release.py
```

---

## 📜 License

Released under the [MIT License](https://opensource.org/licenses/MIT). Designed and maintained by [ProgGuru77](https://github.com/ProgGuru77).
