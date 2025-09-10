"""
Ubuntu Requests 🌍
A respectful, community-minded image fetcher.

This script:
- Prompts the user for one or more image URLs
- Creates a "Fetched_Images" directory if it does not exist
- Downloads and saves the images with appropriate filenames
- Handles errors gracefully (network, invalid URLs, duplicates, etc.)
"""

import os
import requests
from urllib.parse import urlparse
import hashlib


def create_directory():
    """Create Fetched_Images directory if it doesn't exist."""
    os.makedirs("Fetched_Images", exist_ok=True)


def generate_filename(url, content):
    """
    Extract filename from URL or generate one using hash of content.
    Prevents duplicates by checking if file already exists.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # If URL doesn't have a filename, generate one
    if not filename:
        filename = f"image_{hashlib.md5(content).hexdigest()[:8]}.jpg"

    return filename


def download_image(url):
    """Download image from a single URL with respectful error handling."""
    try:
        print(f"\n🔗 Connecting to: {url}")
        response = requests.get(url, timeout=10)

        # Respectful HTTP error handling
        response.raise_for_status()

        # Content-Type check for images
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print(f"⚠️ Skipping: {url} (not an image, got {content_type})")
            return

        # Generate filename
        filename = generate_filename(url, response.content)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate download
        if os.path.exists(filepath):
            print(f"🟡 Skipped (duplicate): {filename}")
            return

        # Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Saved: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch {url}: {e}")


def main():
    print("🌍 Ubuntu Requests – Respectful Image Fetcher")
    print("Enter image URLs (separated by commas if multiple):")

    urls = input("URLs: ").strip().split(",")

    create_directory()

    for url in [u.strip() for u in urls if u.strip()]:
        download_image(url)


if __name__ == "__main__":
    main()
