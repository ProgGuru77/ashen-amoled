#!/usr/bin/env python3
"""
Ashen AMOLED - Release Packaging Utility
Validates theme and font assets, then packages a release archive into dist/.
"""

import os
import re
import sys
import hashlib
import zipfile
import subprocess

def run_preflight_checks():
    print("[-] Running pre-flight verification checks...")
    
    # Check fonts
    res_fonts = subprocess.run([sys.executable, 'scripts/verify_fonts.py'], capture_output=True, text=True)
    if res_fonts.returncode != 0:
        print("[!] Font verification FAILED:\n" + res_fonts.stderr + res_fonts.stdout)
        sys.exit(1)
    print("    [PASS] Fonts and fonts.css verified.")

    # Check theme
    res_theme = subprocess.run([sys.executable, 'scripts/verify_theme.py'], capture_output=True, text=True)
    if res_theme.returncode != 0:
        print("[!] Theme verification FAILED:\n" + res_theme.stderr + res_theme.stdout)
        sys.exit(1)
    print("    [PASS] Theme stylesheet verified (Approach 2, 0 brittle hashes).")

def extract_version():
    with open('ashen-amoled.theme.css', 'r', encoding='utf-8') as f:
        match = re.search(r'@version\s+([0-9\.]+)', f.read())
    if not match:
        raise ValueError("Could not extract @version from ashen-amoled.theme.css")
    return match.group(1)

def package_release():
    run_preflight_checks()

    version = extract_version()
    print(f"[-] Packaging Ashen AMOLED v{version}...")

    os.makedirs('dist', exist_ok=True)
    zip_path = os.path.join('dist', f"ashen-amoled-v{version}.zip")

    files_to_pack = [
        ('ashen-amoled.theme.css', 'ashen-amoled.theme.css'),
        ('fonts.css', 'fonts.css'),
        ('fonts/Cinzel-SemiBold.woff2', 'fonts/Cinzel-SemiBold.woff2'),
        ('fonts/Cinzel-Bold.woff2', 'fonts/Cinzel-Bold.woff2'),
        ('README.md', 'README.md'),
    ]

    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for src, arcname in files_to_pack:
            if not os.path.exists(src):
                raise FileNotFoundError(f"Missing required release file: {src}")
            zf.write(src, arcname)
            size = os.path.getsize(src)
            print(f"    + Added {arcname} ({size:,} bytes)")

    # Calculate SHA-256
    hasher = hashlib.sha256()
    with open(zip_path, 'rb') as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    sha256 = hasher.hexdigest()
    zip_size = os.path.getsize(zip_path)

    print("\n[OK] Release package created successfully!")
    print(f"    Path:    {zip_path}")
    print(f"    Size:    {zip_size:,} bytes")
    print(f"    SHA-256: {sha256}\n")
    return zip_path

if __name__ == '__main__':
    package_release()
