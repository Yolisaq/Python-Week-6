import requests
import os
from urllib.parse import urlparse
from hashlib import md5
from PIL import Image
from io import BytesIO

def fetch_image(url, folder="Fetched_Images"):
    """
    Fetch an image from a URL, save it, and open it automatically.
    Prevents duplicates using hash comparison.
    """
    try:
        os.makedirs(folder, exist_ok=True)
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check content type
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image'):
            print(f"✗ Skipping URL (not an image): {url}")
            return

        # Generate filename from URL or hash
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = f"{md5(response.content).hexdigest()}.jpg"

        filepath = os.path.join(folder, filename)
        if os.path.exists(filepath):
            print(f"⚠ Duplicate detected, skipping: {filename}")
            return

        # Save image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

        # Automatically display image
        try:
            image = Image.open(filepath)
            image.show()  # Opens the default image viewer
        except Exception as e:
            print(f"⚠ Could not open image automatically: {e}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting and viewing images from the web\n")

    urls_input = input(
        "Enter image URLs (comma-separated) or press Enter to use defaults: "
    ).strip()

    if urls_input:
        urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    else:
        # Default working images
        urls = [
            "https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg",
            "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg",
            "https://images.pexels.com/photos/34950/pexels-photo.jpg"
        ]
        print("No URLs entered. Using default example images.\n")

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
