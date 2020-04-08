# Simple image optimization with Pillow.

from pathlib import Path
from PIL import Image

images_path = Path("/Users/shreyashkarnik/Desktop")

print(f"Hey! This is a PNG optimizer by Shreyash.")

for i in images_path.glob("*.png"):
    with Image.open(i) as img_obj:
        img_obj.save("png/" + i.stem + ".png", optimize=True)
