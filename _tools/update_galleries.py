#!/usr/bin/env python3
import os
import urllib.request
import re
import json
from html.parser import HTMLParser


class SwiftLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    # Filter for image links and exclude thumbnails
                    is_img = value.lower().endswith(
                        ('.jpg', '.jpeg', '.png', '.gif')
                    )
                    is_thumb = 'thumbnails' in value.lower()
                    if is_img and not is_thumb:
                        self.links.append(value)


def fetch_images_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        parser = SwiftLinkParser()
        parser.feed(html)
        # Construct absolute URLs
        image_urls = []
        for link in parser.links:
            if not link.startswith('http'):
                image_urls.append(url + link)
            else:
                image_urls.append(link)
        return sorted(list(set(image_urls)))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []


def update_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match frontmatter between ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return

    frontmatter_content = match.group(1)
    body_content = match.group(2)

    # Parse frontmatter simple key-value pairs
    lines = frontmatter_content.split('\n')
    gallery_url = None
    gallery_data = None
    for line in lines:
        if line.startswith('gallery_url:'):
            gallery_url = line.split(':', 1)[1].strip().strip('"\'')
        elif line.startswith('gallery_data:'):
            gallery_data = line.split(':', 1)[1].strip().strip('"\'')

    if not gallery_url or not gallery_data:
        return

    print(f"Updating gallery for {filepath}")
    images = fetch_images_from_url(gallery_url)
    if not images:
        print(f"No images found for {gallery_url}")
        return

    # Write images to the JSON file specified in gallery_data relative to repo root
    clean_data_path = gallery_data.lstrip('/')
    output_file = os.path.join('.', clean_data_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(images, f, indent=2)

    # Reconstruct frontmatter without existing gallery_images
    new_lines = []
    in_gallery_images = False
    for line in lines:
        if line.startswith('gallery_images:'):
            in_gallery_images = True
            continue
        if in_gallery_images:
            if (
                line.startswith(' ')
                or line.startswith('-')
                or line.strip() == ''
            ):
                continue
            else:
                in_gallery_images = False
        new_lines.append(line)

    new_frontmatter = '\n'.join(new_lines)
    new_content = f"---\n{new_frontmatter}\n---\n{body_content}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    msg = f"Wrote {len(images)} image URLs to {output_file}"
    print(msg)


def main():
    # Walk all files in the repo looking for .md files
    for root, dirs, files in os.walk('.'):
        # Skip git and other hidden directories
        if '.git' in root or '_site' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                update_markdown_file(os.path.join(root, file))


if __name__ == "__main__":
    main()
