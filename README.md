# Ashen AMOLED (v2.2)

> A high-contrast, pure AMOLED black theme with Ashen Crimson highlights and Cinzel typography for Discord (via Vencord, BetterDiscord, or custom clients).

---

## Highlights

- **Pure AMOLED (`#000000`):** True-black background across app containers, chat messages, and channels. Ideal for OLED displays.
- **Approach 2 Architecture (`#app-mount` Prefixing):** Elevated specificity (`1-1-0`) naturally supersedes Discord's compiled component styles (`0-1-0`) without requiring brittle `!important` declarations (only 2 in entire stylesheet).
- **OKLCH Uniform Color Scales:** Perceptually uniform 5-step color ramps for Ashen Crimson (`--ashen-crimson-1` to `5`) and presence states (`--ashen-online-*`, `--ashen-idle-*`, `--ashen-dnd-*`, `--ashen-streaming-*`).
- **Dynamic Alpha Blending with `color-mix()`:** Zero hardcoded RGBA alphas for brand accents; all glows, subtle tints, border highlights, and directional mention gradients are derived dynamically from root tokens.
- **Zero-Selector Discord Token Exploitation:** Overrides Discord's compiled design system tokens (`--background-modifier-*`, `--background-message-hover`, `--card-primary-bg`, `--scrollbar-*-thumb`, `--online`, etc.) directly on `:root` and `.theme-dark`.
- **Declarative Configuration & Feature Flags:** User-customizable geometry tokens (`--ashen-border-radius-*`), motion variables (`--ashen-transition-*`), and feature toggles (`--ashen-animations`, `--ashen-panel-blur`).
- **Decoupled Font Assets:** `Cinzel` (SemiBold 600 and Bold 700) is extracted into standalone WOFF2 binaries inside `fonts/` and imported cleanly via `fonts.css`.
- **Stream & Call Transparency Shield:** Completely resolves the stream overlay occlusion ("black box" bug) by enforcing explicit zero-opacity rules for video wrappers and scoping guild scrollers.
- **Resilient Selectors:** Uses attribute wildcard selectors (e.g., `[class*="chatContent_"]`) instead of transient build hashes.
- **QuickSwitcher & Global Search (Ctrl+K):** AMOLED surfaces with crimson active indicators for search results and Quick Switcher.
- **Chat Autocomplete & Mentions:** Styled `@`, `#`, and `:` suggestion popouts with Cinzel category headers.
- **Extended Typography:** Server dropdown headers, channel titles, and modal dialogs bound to Cinzel.
- **Friends & "Active Now" Dashboard:** Deep AMOLED surfaces eliminating Discord's default grey cards.
- **Codeblock & Syntax Theme:** Crimson accents on keywords, inline code styling, and clean borders.
- **Production Linter & Release Packager:** `.stylelintrc.json` configuration and automated bundler (`scripts/package_release.py`) that runs all tests and packages clean release archives into `dist/`.

---

## Directory Structure

```
.
├── fonts/
│   ├── Cinzel-SemiBold.woff2      # Local WOFF2 binary (Weight 600)
│   └── Cinzel-Bold.woff2          # Local WOFF2 binary (Weight 700)
├── fonts.css                      # @font-face declarations referencing local font binaries
├── ashen-amoled.theme.css         # Main theme entrypoint (17 segmented modules)
├── .stylelintrc.json              # Standard Stylelint configuration
├── scripts/
│   ├── decode_fonts.py            # Font decoder utility
│   ├── verify_fonts.py            # Font & fonts.css verification script
│   ├── verify_theme.py            # Theme verification (specificity, stream shield, OKLCH, tokens, hashes)
│   └── package_release.py         # Automated test runner and release bundler
└── README.md
```

---

## Installation

### Vencord (Local Theme)

1. Clone or download this repository into your Vencord themes directory:
   - **Windows:** `%AppData%\Vencord\themes\ashen-amoled`
   - **Linux:** `~/.config/Vencord/themes/ashen-amoled`
   - **macOS:** `~/Library/Application Support/Vencord/themes/ashen-amoled`
2. Ensure the `fonts/` directory and `fonts.css` are placed alongside `ashen-amoled.theme.css`.
3. Open Discord Settings -> **Vencord** -> **Themes**.
4. Enable **Ashen AMOLED** (or point the Online Theme import to `ashen-amoled.theme.css`).

---

## Verification & Release Packaging

Automated verification scripts are provided to validate all architectural guarantees:

```bash
# Verify fonts exist, have valid WOFF2 headers, and are referenced in fonts.css
python scripts/verify_fonts.py

# Verify !important count (<10), stream transparency shield, OKLCH scales, color-mix, and hashless selectors
python scripts/verify_theme.py

# Run all preflight checks and bundle into dist/ashen-amoled-v2.2.0.zip
python scripts/package_release.py
```

---

## License

MIT License. Designed and maintained by [ProgGuru77](https://github.com/ProgGuru77).
