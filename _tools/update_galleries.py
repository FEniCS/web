#!/usr/bin/env python3
import os
import urllib.request
import re
from html.parser import HTMLParser


class SwiftLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.subdirs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    # Exclude parent or absolute links
                    if (
                        value == '../'
                        or value.startswith('/')
                        or value.startswith('http')
                    ):
                        continue
                    if value.endswith('/'):
                        self.subdirs.append(value)
                    elif value.lower().endswith(
                        ('.jpg', '.jpeg', '.png', '.gif')
                    ):
                        if 'thumbnails' not in value.lower():
                            self.images.append(value)


def fetch_images_from_url(url):
    all_images = []

    def crawl(current_url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(current_url, headers=headers)
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
            parser = SwiftLinkParser()
            parser.feed(html)

            # Add images found in current dir
            for img in parser.images:
                all_images.append(current_url + img)

            # Recurse into subdirs
            for subdir in parser.subdirs:
                if current_url.endswith('/'):
                    subdir_url = current_url + subdir
                else:
                    subdir_url = current_url + '/' + subdir
                crawl(subdir_url)
        except Exception as e:
            print(f"Error crawling {current_url}: {e}")

    crawl(url)

    # Explicitly check for 'jpeg/' subfolder if virtual directories are hidden
    jpeg_url = url + 'jpeg/' if url.endswith('/') else url + '/jpeg/'
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(jpeg_url, headers=headers)
        with urllib.request.urlopen(req):
            print(f"Crawling explicit subfolder: {jpeg_url}")
            crawl(jpeg_url)
    except Exception:
        pass

    return sorted(list(set(all_images)))


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
    row1_start = "<!-- GALLERY_ROW1_START -->"
    row1_end = "<!-- GALLERY_ROW1_END -->"
    row2_start = "<!-- GALLERY_ROW2_START -->"
    row2_end = "<!-- GALLERY_ROW2_END -->"

    if (
        row1_start not in body_content
        or row1_end not in body_content
        or row2_start not in body_content
        or row2_end not in body_content
    ):
        return

    print(f"Updating gallery rows in-place for {filepath}")
    images = fetch_images_from_url(gallery_url)
    if not images:
        print(f"No images found for {gallery_url}")
        return

    # Divide images into two rows
    mid = (len(images) + 1) // 2
    row1_images = images[:mid]
    row2_images = images[mid:]

    def build_row_html(images_list, start_idx):
        lines_list = []
        for idx, img_url in enumerate(images_list):
            line = (
                f'        <a href="{img_url}" target="_blank" '
                f'rel="noopener noreferrer">'
                f'<img src="{img_url}" loading="lazy" '
                f'alt="Photo {start_idx + idx + 1}" /></a>'
            )
            lines_list.append(line)
        return "\n".join(lines_list)

    row1_html = build_row_html(row1_images, 0)
    row2_html = build_row_html(row2_images, mid)

    # Replace row 1
    pattern1 = re.escape(row1_start) + r"(.*?)" + re.escape(row1_end)
    replacement1 = f"{row1_start}\n{row1_html}\n        {row1_end}"
    new_body_content = re.sub(
        pattern1, replacement1, body_content, flags=re.DOTALL
    )

    # Replace row 2
    pattern2 = re.escape(row2_start) + r"(.*?)" + re.escape(row2_end)
    replacement2 = f"{row2_start}\n{row2_html}\n        {row2_end}"
    new_body_content = re.sub(
        pattern2, replacement2, new_body_content, flags=re.DOTALL
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

    msg = (
        f"Successfully updated {filepath} with {len(images)} static links "
        f"across 2 rows."
    )
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
