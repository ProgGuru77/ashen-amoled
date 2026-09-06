# Ashen AMOLED (v2.1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement 6 new modules and utilities for Ashen AMOLED v2.1: Quick Switcher, Autocomplete, Extended Cinzel Typography, Friends & Active Now overhaul, Codeblock Syntax Styling, and an Automated Distribution Packager.

**Architecture:** Approach 2 (`#app-mount` prefixing) providing 1-1-0 specificity, zero brittle hashes, resilient wildcard class matching, zero-opacity stream shields, and token-driven pure AMOLED palette.

**Tech Stack:** CSS3, Discord Design Tokens, Vencord Theme Engine, WOFF2 binary fonts, Python 3.

## Global Constraints
- Main theme entrypoint must be named `ashen-amoled.theme.css`.
- Separate font definitions must live in `fonts.css` with binary files in `fonts/`.
- Total `!important` count must remain under 10 across the entire stylesheet (currently 2).
- Zero brittle build hashes (5-7 alphanumeric chars).
- Do NOT search for or include Base64 font strings.
- Do NOT run `git log`, `git log -p`, `git show`, or `git diff`.

---

### Task 1: Add Modules 12–16 to `ashen-amoled.theme.css`

- [ ] Step 1: Update theme version to 2.1.0 and append Modules 12–16:
  - 12. QuickSwitcher & Search Matrix
  - 13. Chat Autocomplete & Mention Popouts
  - 14. Extended Cinzel Typography Suite
  - 15. Friends Tab & Active Now Dashboard
  - 16. Codeblocks & Syntax Highlight Styling
- [ ] Step 2: Validate syntax and integrity.

---

### Task 2: Update Verification Suite (`scripts/verify_theme.py`)

- [ ] Step 1: Add assertions for the 5 new modules.
- [ ] Step 2: Run `python scripts/verify_theme.py` and confirm all tests pass.

---

### Task 3: Build Automated Distribution Release Packager (`scripts/package_release.py`)

- [ ] Step 1: Create `scripts/package_release.py` to run verification and package `dist/ashen-amoled-v{version}.zip`.
- [ ] Step 2: Execute `python scripts/package_release.py` and verify generated archive.

---

### Task 4: Documentation & Final Verification

- [ ] Step 1: Update `README.md` with v2.1 features and distribution packager instructions.
- [ ] Step 2: Run `python scripts/verify_fonts.py` and `python scripts/verify_theme.py`.
- [ ] Step 3: Check `git status` and commit clean changes.
