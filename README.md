# wallpaper_changer
# Wallpaper Changer with Previous Wallpaper Backup

This Python script automatically sets a random nature image as your desktop wallpaper and backs up the current wallpaper. It uses the Unsplash API to fetch random nature images.

## Features

- Fetches a random nature image from Unsplash.
- Sets the fetched image as the wallpaper on your primary monitor.
- Backs up the current wallpaper before changing it.
- Allows restoration of the previous wallpaper.

## Requirements

- Python 3.7 or higher
- An Unsplash API key (free to obtain)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/wallpaper-changer.git
    cd wallpaper-changer
    ```

2. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Get an Unsplash API key:**
    - Visit [Unsplash Developers](https://unsplash.com/developers) and sign up for an API key.
    - Replace the placeholder in the script with your actual API key.

## Usage

1. **Set up your Unsplash API key:**
   
    Edit the `main.py` file and replace `''` with your Unsplash API key.

2. **Run the script:**

    ```sh
    python main.py
    ```

    The script will:
    - Backup the current wallpaper to `previous_wallpaper.jpg` in the script's directory.
    - Download a random nature image from Unsplash.
    - Save the downloaded image as `current_wallpaper.jpg`.
    - Set `current_wallpaper.jpg` as the new wallpaper.

3. **Restore the previous wallpaper:**

    To restore the previous wallpaper, uncomment the line `restore_previous_wallpaper()` at the end of the script and run the script again:

    ```python
    # Uncomment the next line if you want to restore the previous wallpaper
    # restore_previous_wallpaper()
    ```

    Then run:

    ```sh
    python main.py
    ```

## Directory Structure

