#!/usr/bin/env python3
import os
from PIL import Image

def clean_path(raw_path):
    # Remove whitespace and common quote characters users paste around paths.
    return raw_path.strip().strip("\"'`“”‘’")

def merge_images():
    try:
        # 1. Take input from user
        # Normalize pasted paths by removing surrounding spaces/quotes.
        path1 = clean_path(input("Enter path for the first image: "))
        path2 = clean_path(input("Enter path for the second image: "))
        output_name = input("Enter the name for the output image (e.g., merged.jpg): ").strip()

        if not os.path.isfile(path1):
            raise FileNotFoundError(f"First image not found: {path1}")
        if not os.path.isfile(path2):
            raise FileNotFoundError(f"Second image not found: {path2}")

        # 2. Open images
        img1 = Image.open(path1)
        img2 = Image.open(path2)

        # 3. Resize second image to match the height of the first
        # This ensures they align perfectly side-by-side
        width1, height1 = img1.size
        img2 = img2.resize((int(img2.width * height1 / img2.height), height1))
        width2, height2 = img2.size

        # 4. Create a new blank canvas with combined width
        new_width = width1 + width2
        new_height = max(height1, height2)
        new_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))

        # 5. Paste the two images onto the canvas
        new_image.paste(img1, (0, 0))
        new_image.paste(img2, (width1, 0))

        # 6. Save the result
        new_image.save(output_name)
        print(f"Success! Merged image saved as {output_name}")
        new_image.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    merge_images()
