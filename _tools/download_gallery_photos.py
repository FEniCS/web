#!/usr/bin/env python3
import os
import urllib.request
import re


def download_file(url, dest):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            with open(dest, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match frontmatter between ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return

    frontmatter_content = match.group(1)
    body_content = match.group(2)

    # Parse gallery_url from frontmatter
    lines = frontmatter_content.split('\n')
    gallery_url = None
    for line in lines:
        if line.startswith('gallery_url:'):
            gallery_url = line.split(':', 1)[1].strip().strip('"\'')

    if not gallery_url:
        return

    # Find all references to local files in conference/pages_2026/
    # e.g., /conference/pages_2026/IMG_9738.jpeg
    pattern = r'/?conference/pages_2026/([a-zA-Z0-9_\-\.]+)'
    filenames = set(re.findall(pattern, body_content))

    if not filenames:
        return

    print(
        f"Processing {filepath}: found {len(filenames)} "
        "referenced local images."
    )
    out_dir = os.path.join('.', 'conference', 'pages_2026')
    os.makedirs(out_dir, exist_ok=True)

    for filename in filenames:
        dest_path = os.path.join(out_dir, filename)
        if os.path.exists(dest_path):
            continue

        # Try downloading from root gallery_url
        src_url = (
            gallery_url + filename
            if gallery_url.endswith('/')
            else gallery_url + '/' + filename
        )
        print(f"Downloading {filename} from {src_url}...")
        success = download_file(src_url, dest_path)

        # If failed, try downloading from gallery_url + 'jpeg/'
        if not success:
            jpeg_url = (
                gallery_url + 'jpeg/' + filename
                if gallery_url.endswith('/')
                else gallery_url + '/jpeg/' + filename
            )
            print(f"Retrying {filename} from {jpeg_url}...")
            success = download_file(jpeg_url, dest_path)

        if not success:
            print(f"Warning: Could not download {filename} from {gallery_url}")


def main():
    # Walk all files in the repo looking for .md files
    for root, dirs, files in os.walk('.'):
        if '.git' in root or '_site' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    main()
