import re

with open('ashen-amoled.theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Count !important
importants = len(re.findall(r'!important', content))
print(f"Total !important count: {importants}")

# Check stream transparency
has_stream_shield = "participantsWrapper_" in content and "background: transparent" in content
print(f"Stream transparency shield present: {has_stream_shield}")

# Check hashless selectors
brittle_hashes = re.findall(r'_[a-z0-9]{5,7}\b', content)
print(f"Brittle hash count: {len(brittle_hashes)}")

# Check embed border ordering
embed_match = re.search(r'\[class\*="embedFull_"\]\s*\{([^}]+)\}', content)
assert embed_match, "embedFull_ rule missing"
embed_rules = [r.strip() for r in embed_match.group(1).split(';') if r.strip()]
border_idx = next(i for i, r in enumerate(embed_rules) if re.match(r'^border\s*:', r))
border_left_idx = next(i for i, r in enumerate(embed_rules) if re.match(r'^border-left(-color)?\s*:', r))
assert border_left_idx > border_idx, "border shorthand must precede border-left accent declaration"

# Check menu focused selector
assert '[class*="menu_"] [class*="item_"][class*="focused_"]' in content, "menu item focused_ state missing"

# Check Module 12: QuickSwitcher & Search Matrix
assert '[class*="quickswitcher_"]' in content, "QuickSwitcher styling missing"
assert '[class*="searchResultsWrap_"]' in content, "Search results styling missing"

# Check Module 13: Chat Autocomplete
assert '[class*="autocomplete_"]' in content, "Autocomplete styling missing"
assert '[class*="autocompleteInner_"]' in content, "Autocomplete inner container styling missing"

# Check Module 14: Extended Cinzel Typography
assert '[class*="header_"][class*="guildHeader_"]' in content, "Guild header Cinzel binding missing"
assert '[class*="root_"] h1' in content, "Modal headers Cinzel binding missing"

# Check Module 16: Friends & Active Now
assert '[class*="nowPlayingColumn_"]' in content, "nowPlayingColumn_ styling missing"
assert '[class*="peopleColumn_"]' in content, "peopleColumn_ styling missing"

# Check Module 17: Codeblocks & Syntax Highlighting
assert 'code.inline' in content, "Inline code styling missing"
assert '.hljs-keyword' in content, "Syntax highlighting keyword styling missing"

# Check Declarative Configuration & Feature Flags (Spec §7)
assert '--ashen-gap:' in content, "Declarative --ashen-gap missing"
assert '--ashen-animations:' in content, "Declarative --ashen-animations toggle missing"
assert '--ashen-transition-normal:' in content, "Declarative --ashen-transition-normal missing"
assert '--ashen-border-radius-sm:' in content, "Declarative --ashen-border-radius-sm missing"
assert '--ashen-accent-crimson:' in content, "Declarative --ashen-accent-crimson missing"
assert '--ashen-amoled-mode:' in content, "Declarative --ashen-amoled-mode missing"

# Check High-Contrast Icon Tokens & Controls
assert '--icon-primary:' in content, "Discord native --icon-primary missing"
assert '--channel-icon:' in content, "Discord native --channel-icon missing"
assert '[class*="circleIconButton_"]' in content, "Guild rail circle icon button styling missing"

# Check OKLCH Perceptually Uniform Scales (Spec §2.2)
oklch_matches = re.findall(r'oklch\([^)]+\)', content)
assert len(oklch_matches) >= 20, f"Expected at least 20 OKLCH scale declarations, found {len(oklch_matches)}"
assert '--ashen-crimson-1:' in content and '--ashen-crimson-5:' in content, "OKLCH Crimson ramp missing"
assert '--ashen-online-1:' in content and '--ashen-online-5:' in content, "OKLCH Online ramp missing"
assert '--ashen-idle-1:' in content and '--ashen-idle-5:' in content, "OKLCH Idle ramp missing"
assert '--ashen-streaming-1:' in content and '--ashen-streaming-5:' in content, "OKLCH Streaming ramp missing"

# Check Dynamic Alpha Blending via color-mix() (Spec §2.3)
color_mix_matches = re.findall(r'color-mix\([^)]+\)', content)
assert len(color_mix_matches) >= 5, f"Expected at least 5 color-mix declarations, found {len(color_mix_matches)}"
assert '--ashen-accent-glow:' in content and 'color-mix' in content, "Dynamic glow via color-mix missing"
assert '--ashen-mention-bg:' in content and 'color-mix' in content, "Dynamic mention background via color-mix missing"

# Check Discord Zero-Selector Token Overrides (Spec §3.1, §3.2)
zero_selector_tokens = [
    '--background-modifier-hover:',
    '--background-modifier-active:',
    '--background-modifier-selected:',
    '--background-modifier-accent:',
    '--background-message-hover:',
    '--card-primary-bg:',
    '--scrollbar-auto-thumb:',
    '--scrollbar-thin-thumb:',
    '--online:',
    '--idle:',
    '--dnd:',
    '--streaming:'
]
for token in zero_selector_tokens:
    assert token in content, f"Zero-selector token {token} missing from theme"

# Check .stylelintrc.json existence (Spec §9.4)
import os
import json
assert os.path.exists('.stylelintrc.json'), "Missing .stylelintrc.json standard configuration"
with open('.stylelintrc.json', 'r', encoding='utf-8') as f:
    stylelint_cfg = json.load(f)
assert 'rules' in stylelint_cfg, "Invalid .stylelintrc.json: missing 'rules'"

assert importants < 10, f"Too many !important flags: {importants}"
assert has_stream_shield, "Missing stream transparency shield"
assert len(brittle_hashes) == 0, f"Found brittle hashes: {brittle_hashes[:5]}"
print("ALL CHECKS PASSED.")
