import os

assert os.path.exists("fonts/Cinzel-SemiBold.woff2"), "Missing fonts/Cinzel-SemiBold.woff2"
assert os.path.exists("fonts/Cinzel-Bold.woff2"), "Missing fonts/Cinzel-Bold.woff2"

with open("fonts/Cinzel-SemiBold.woff2", "rb") as f:
    header600 = f.read(4)
    assert header600 == b"wOF2", f"Invalid WOFF2 header for 600: {header600}"

with open("fonts/Cinzel-Bold.woff2", "rb") as f:
    header700 = f.read(4)
    assert header700 == b"wOF2", f"Invalid WOFF2 header for 700: {header700}"

size600 = os.path.getsize("fonts/Cinzel-SemiBold.woff2")
size700 = os.path.getsize("fonts/Cinzel-Bold.woff2")
print(f"Verified WOFF2 binaries: SemiBold ({size600} bytes), Bold ({size700} bytes)")
assert size600 > 20000, f"SemiBold font size too small: {size600}"
assert size700 > 20000, f"Bold font size too small: {size700}"

assert os.path.exists("fonts.css"), "Missing fonts.css"
with open("fonts.css", "r", encoding="utf-8") as f:
    fonts_css = f.read()

assert "@font-face" in fonts_css, "fonts.css missing @font-face"
assert "font-family: 'Cinzel'" in fonts_css or 'font-family: "Cinzel"' in fonts_css, "fonts.css missing Cinzel family"
assert "font-weight: 600" in fonts_css, "fonts.css missing weight 600"
assert "font-weight: 700" in fonts_css, "fonts.css missing weight 700"
assert "Cinzel-SemiBold.woff2" in fonts_css, "fonts.css missing Cinzel-SemiBold.woff2 reference"
assert "Cinzel-Bold.woff2" in fonts_css, "fonts.css missing Cinzel-Bold.woff2 reference"
print("fonts.css verified successfully.")
print("ALL FONT CHECKS PASSED.")
