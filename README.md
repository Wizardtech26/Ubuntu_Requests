# 🌍 Ubuntu Requests

A respectful, community-minded Python tool for fetching and organizing images from the web.

## ✨ Features
- Prompts the user for one or more image URLs
- Creates a `Fetched_Images/` directory automatically
- Downloads and saves images with proper filenames
- Handles errors gracefully (invalid URL, non-image, etc.)
- Prevents duplicates by checking existing files
- Checks HTTP headers to ensure content is an image

## 🛠 Requirements
- Python 3.8+
- [requests](https://docs.python-requests.org/)

Install dependencies:
```bash
pip install requests
