import os, sys, json, subprocess, urllib.request, urllib.error

def get_github_token():
    p = subprocess.Popen('git credential fill'.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate('protocol=https\nhost=github.com\n')
    creds = dict(line.split('=', 1) for line in out.strip().split('\n') if '=' in line)
    return creds.get('password')

def publish_release():
    token = get_github_token()
    if not token:
        print('[!] Failed to retrieve GitHub token from git credentials.')
        sys.exit(1)

    repo = 'ProgGuru77/ashen-amoled'
    tag = 'v2.2.1'
    name = 'Ashen AMOLED v2.2.1'
    zip_name = 'ashen-amoled-v2.2.1.zip'
    zip_path = os.path.join('dist', zip_name)

    if not os.path.exists(zip_path):
        print(f'[!] Zip file {zip_path} does not exist.')
        sys.exit(1)

    body = '''## Ashen AMOLED v2.2.1

High-contrast pure AMOLED black theme with Ashen Crimson highlights and Cinzel typography for Discord (Vencord, BetterDiscord).

### 🙩 What's New in v2.2.1
- **Maximum AMOLED Black (#000000 Default):** Full true-black background across all sidebars, channels, servers rail, and member list. Pixels turn completely OFF for optimal OLED efficiency and zero backlight bleed.
- **High-Contrast Icon Calibration:** Overrides Discord's native icon tokens (--icon-primary, --channel-icon, --icon-secondary, --icon-muted) and provides elevated AMOLED tiles for server circle buttons (circleIconButton_) and reaction badges so icons never blend into dark surfaces.
- **Dynamic OKLCH Color System & Toggle:** Easily toggle the accent color across the entire theme via --ashen-accent-hue in :root (Crimson 18deg, Amber 88deg, Emerald 165deg, Cyan 210deg, Sapphire 260deg, Amethyst 310deg).
- **Enhanced Reactions & Composer:** Distinct elevated reaction pills with crisp count typography and illuminated hover controls.

### 💘 Installation
- **Vencord Online Theme:**
  ```
  https://raw.githubusercontent.com/ProgGuru77/ashen-amoled/main/ashen-amoled.theme.css
  ``` 
- **Manual Installation:**
  Download `ashen-amoled-v2.2.1.zip` below and extract into your Vencord or BetterDiscord themes folder.
'''

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Ashen-AMOLED-Release-Bot'
    }

    release_id = None
    try:
        check_req = urllib.request.Request(f'https://api.github.com/repos/{repo}/releases/tags/{tag}', headers=headers)
        with urllib.request.urlopen(check_req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            release_id = data['id']
            upload_url = data['upload_url'].split('{')[0]
            print(f'[-] GitHub release {tag} already exists (ID: {release_id}).')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f'[-] Creating new GitHub release for {tag}...')
            payload = {
                'tag_name': tag,
                'name': name,
                'body': body,
                'draft': False,
                'prerelease': False
            }
            create_req = urllib.request.Request(
                f'https://api.github.com/repos/{repo}/releases',
                headers={**headers, 'Content-Type': 'application/json'},
                data=json.dumps(payload).encode('utf-8')
            )
            with urllib.request.urlopen(create_req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                release_id = data['id']
                upload_url = data['upload_url'].split('{')[0]
                print(f'[[] Release created successfully (ID: {release_id})!')
        else:
            raise

    assets_req = urllib.request.Request(f'https://api.github.com/repos/{repo}/releases/{release_id}/assets', headers=headers)
    with urllib.request.urlopen(assets_req) as resp:
        existing_assets = json.loads(resp.read().decode('utf-8'))
        for asset in existing_assets:
            if asset['name'] == zip_name:
                print(f'[-] Asset {zip_name} already exists. Deleting older asset ID {asset["id"]}...')
                del_req = urllib.request.Request(asset['url'], headers=headers, method='DELETE')
                urllib.request.urlopen(del_req)
                print('    Deleted.')

    print(f'[-] Uploading {zip_name} to GitHub release...')
    with open(zip_path, 'rb') as f:
        zip_data = f.read()

    upload_headers = {
        'Authorization': f'token {token}',
        'Content-Type': 'application/zip',
        'User-Agent': 'Ashen-AMOLED-Release-Bot'
    }
    upload_req = urllib.request.Request(
        f'{upload_url}?name={zip_name}',
        headers=upload_headers,
        data=zip_data,
        method='POST'
    )
    with urllib.request.urlopen(upload_req) as resp:
        asset_data = json.loads(resp.read().decode('utf-8'))
        print('[OK] GitHub release zip asset uploaded successfully!')
        print(f'     Release:   https://github.com/{repo}/releases/tag/{tag}')
        print(f"     Download: {asset_data.get('browser_download_url')}")

if __name__ == '__main__':
    publish_release()
