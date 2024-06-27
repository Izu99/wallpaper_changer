import os
import ctypes
import requests
from PIL import Image
from io import BytesIO

# Unsplash API credentials
# Replace with your Unsplash API key
UNSPLASH_API_KEY = 'unsplash APi Key'

# Paths for wallpapers
script_dir = os.path.dirname(os.path.abspath(__file__))
CURRENT_WALLPAPER = os.path.join(script_dir, 'current_wallpaper.jpg')
PREVIOUS_WALLPAPER = os.path.join(script_dir, 'previous_wallpaper.jpg')
NEW_WALLPAPER = os.path.join(script_dir, 'new_wallpaper.jpg')


def fetch_random_nature_image():
    url = 'https://api.unsplash.com/photos/random'
    headers = {
        'Authorization': f'Client-ID ' + UNSPLASH_API_KEY
    }
    params = {
        'query': 'nature',         # Search for nature images
        'orientation': 'landscape'  # Optional: use 'landscape' for wallpaper-friendly images
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError if the request failed
        data = response.json()

        if 'urls' in data and 'full' in data['urls']:
            return data['urls']['full']
        else:
            print(
                "Error: 'urls' key not found in the response or no 'full' image available.")
            print("Response JSON:", data)
            return None
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
        return None


def download_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        img = Image.open(BytesIO(response.content))
        img.save(NEW_WALLPAPER)
        return NEW_WALLPAPER
    except requests.RequestException as e:
        print(f"Error downloading image: {e}")
        return None


def set_wallpaper(image_path):
    # Set wallpaper using SystemParametersInfo
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


def backup_current_wallpaper():
    try:
        if os.path.exists(CURRENT_WALLPAPER):
            # Move current wallpaper to previous wallpaper
            os.replace(CURRENT_WALLPAPER, PREVIOUS_WALLPAPER)
            print(f"Previous wallpaper saved to: {PREVIOUS_WALLPAPER}")
        else:
            print("No current wallpaper found to backup.")
    except Exception as e:
        print(f"Error backing up wallpaper: {e}")


def restore_previous_wallpaper():
    try:
        if os.path.exists(PREVIOUS_WALLPAPER):
            # Set previous wallpaper as the current wallpaper
            set_wallpaper(PREVIOUS_WALLPAPER)
            print("Restored the previous wallpaper.")
        else:
            print("No previous wallpaper found to restore.")
    except Exception as e:
        print(f"Error restoring wallpaper: {e}")


if __name__ == "__main__":
    # Backup current wallpaper before changing
    backup_current_wallpaper()

    # Fetch and set new wallpaper
    image_url = fetch_random_nature_image()
    if image_url:
        print(f"Fetching image from: {image_url}")
        image_path = download_image(image_url)
        if image_path:
            print(f"Downloaded image to: {image_path}")
            # Rename the new wallpaper to current wallpaper
            os.replace(image_path, CURRENT_WALLPAPER)
            set_wallpaper(CURRENT_WALLPAPER)
            print("Wallpaper updated successfully.")
        else:
            print("Failed to download the image.")
    else:
        print("Failed to fetch the image URL.")

    # Optionally restore the previous wallpaper
    # Uncomment the next line if you want to restore the previous wallpaper
    # restore_previous_wallpaper()
