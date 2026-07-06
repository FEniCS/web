#!/usr/bin/env python3
import os
import urllib.request
import re
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
    for line in lines:
        if line.startswith('gallery_url:'):
            gallery_url = line.split(':', 1)[1].strip().strip('"\'')

    if not gallery_url:
        return

    # Check if markers exist in body
    start_marker = "<!-- GALLERY_IMAGES_START -->"
    end_marker = "<!-- GALLERY_IMAGES_END -->"
    if start_marker not in body_content or end_marker not in body_content:
        return

    print(f"Updating gallery in-place for {filepath}")
    images = fetch_images_from_url(gallery_url)
    if not images:
        print(f"No images found for {gallery_url}")
        return

    # Generate image list HTML
    image_lines = []
    for idx, img_url in enumerate(images):
        line = (
            f'      <a href="{img_url}" target="_blank" '
            f'rel="noopener noreferrer">'
            f'<img src="{img_url}" loading="lazy" '
            f'alt="Photo {idx + 1}" /></a>'
        )
        image_lines.append(line)

    gallery_html = "\n".join(image_lines)

    # Replace content between markers
    pattern = re.escape(start_marker) + r"(.*?)" + re.escape(end_marker)
    replacement = f"{start_marker}\n{gallery_html}\n      {end_marker}"
    new_body_content = re.sub(
        pattern, replacement, body_content, flags=re.DOTALL
    )

    # Remove gallery_data and gallery_images from frontmatter if present
    new_fm_lines = []
    for line in lines:
        if (
            line.startswith('gallery_data:')
            or line.startswith('gallery_images:')
        ):
            continue
        new_fm_lines.append(line)

    new_frontmatter = '\n'.join(new_fm_lines)
    new_content = f"---\n{new_frontmatter}\n---\n{new_body_content}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    msg = f"Successfully updated {filepath} with {len(images)} static links."
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
