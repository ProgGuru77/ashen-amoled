import base64
import os
import re

os.makedirs('fonts', exist_ok=True)

with open('docs/superpowers/plans/2026-09-06-ashen-amoled-overhaul.md', 'r', encoding='utf-8') as f:
    text = f.read()

m600 = re.search(r'font_600_b64 = "([^"]+)"', text)
m700 = re.search(r'font_700_b64 = "([^"]+)"', text)

if m600 and m700:
    b600 = base64.b64decode(m600.group(1))
    b700 = base64.b64decode(m700.group(1))
    with open('fonts/Cinzel-SemiBold.woff2', 'wb') as f:
        f.write(b600)
    with open('fonts/Cinzel-Bold.woff2', 'wb') as f:
        f.write(b700)
    print(f"Decoded fonts: 600={len(b600)}B, 700={len(b700)}B, header={b600[:4]}")
    print("Successfully decoded fonts into fonts/ directory.")
else:
    print("Failed to find base64 strings")
