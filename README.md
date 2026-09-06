# Ashen AMOLED (v2.1)

> A high-contrast, pure AMOLED black theme with Ashen Crimson highlights and Cinzel typography for Discord (via Vencord, BetterDiscord, or custom clients).

---

## Highlights

- **Pure AMOLED (`#000000`):** True-black background across app containers, chat messages, and channels. Ideal for OLED displays.
- **Approach 2 Architecture (`#app-mount` Prefixing):** Elevated specificity (`1-1-0`) naturally supersedes Discord's compiled component styles (`0-1-0`) without requiring brittle `!important` declarations (only 2 in entire stylesheet).
- **Decoupled Font Assets:** `Cinzel` (SemiBold 600 and Bold 700) is extracted into standalone WOFF2 binaries inside `fonts/` and imported cleanly via `fonts.css`.
- **Stream & Call Transparency Shield:** Completely resolves the stream overlay occlusion ("black box" bug) by enforcing explicit zero-opacity rules for video wrappers and scoping guild scrollers.
- **Resilient Selectors:** Uses attribute wildcard selectors (e.g., `[class*="chatContent_"]`) instead of transient build hashes.
- **QuickSwitcher & Global Search (Ctrl+K):** AMOLED surfaces with crimson active indicators for search results and Quick Switcher.
- **Chat Autocomplete & Mentions:** Styled `@`, `#`, and `:` suggestion popouts with Cinzel category headers.
- **Extended Typography:** Server dropdown headers, channel titles, and modal dialogs bound to Cinzel.
- **Friends & "Active Now" Dashboard:** Eliminates Discord's default grey cards in favor of deep AMOLED surfaces.
- **Codeblock & Syntax Theme:** Crimson accents on keywords, inline code styling, and clean borders.
- **One-Click Release Packaging:** Automated bundler (`scripts/package_release.py`) that runs all tests and packages clean release archives into `dist/`.

---

## Directory Structure

```
.
├── fonts/
│   ├── Cinzel-SemiBold.woff2      # Local WOFF2 binary (Weight 600)
│   └── Cinzel-Bold.woff2          # Local WOFF2 binary (Weight 700)
├── fonts.css                      # @font-face declarations referencing local font binaries
├── ashen-amoled.theme.css         # Main theme entrypoint (16 segmented modules)
├── scripts/
│   ├── decode_fonts.py            # Font decoder utility
│   ├── verify_fonts.py            # Font & fonts.css verification script
│   ├── verify_theme.py            # Theme verification (specificity, stream shield, hashes)
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

# Verify !important count (<10), stream transparency shield, and hashless selectors
python scripts/verify_theme.py

# Run all preflight checks and bundle into dist/ashen-amoled-v2.1.0.zip
python scripts/package_release.py
```

---

## License

MIT License. Designed and maintained by [ProgGuru77](https://github.com/ProgGuru77).
