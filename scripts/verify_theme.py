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

assert importants < 30, f"Too many !important flags: {importants}"
assert has_stream_shield, "Missing stream transparency shield"
assert len(brittle_hashes) == 0, f"Found brittle hashes: {brittle_hashes[:5]}"
print("ALL CHECKS PASSED.")
