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

# Check Module 15: Friends & Active Now
assert '[class*="nowPlayingColumn_"]' in content, "nowPlayingColumn_ styling missing"
assert '[class*="peopleColumn_"]' in content, "peopleColumn_ styling missing"

# Check Module 16: Codeblocks & Syntax Highlighting
assert 'code.inline' in content, "Inline code styling missing"
assert '.hljs-keyword' in content, "Syntax highlighting keyword styling missing"

assert importants < 10, f"Too many !important flags: {importants}"
assert has_stream_shield, "Missing stream transparency shield"
assert len(brittle_hashes) == 0, f"Found brittle hashes: {brittle_hashes[:5]}"
print("ALL CHECKS PASSED.")
