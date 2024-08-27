"""A quick script for transforming a picture for printing.

   Takes in a photo, squares it and creates a 5x3 array.
   - you might want to preprocess the photo by removing the background
   This ensures that when printed as a 15x10cm image (without fitting)
   we achieve 3x3cm photos, which are needed for JLPT applications.
"""

import sys
from pathlib import Path
from PIL import Image


def transform(filename):
    p = Path(filename)
    img = Image.open(p)

    # square based on smaller dimension
    SIZE = min(img.size)
    squared = img.crop((0, 0, SIZE, SIZE))

    # resize to save a bit of space
    NEW_SIZE = SIZE // 4
    resized = squared.resize((NEW_SIZE, NEW_SIZE))

    # create new image with 3:2 dimensions, white background
    WIDTH = NEW_SIZE * 5
    HEIGHT = WIDTH * 2 // 3

    new = Image.new("RGBA", (WIDTH, HEIGHT), color="white")

    for row in range(3):
        for column in range(5):
            new.alpha_composite(resized, (column * NEW_SIZE, row * NEW_SIZE))

    new.save(f"transformed_{p.name}")


if __name__ == "__main__":
    files = sys.argv[1:]

    for file in files:
        transform(file)
