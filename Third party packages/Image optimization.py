# Optimizing and saving images with Pillow.

from PIL import Image
from pathlib import Path

source = Path("png")
target = Path("result")

# with Image.open(source/"about_back_image1.png") as img_obj:
#     img_obj = img_obj.quantize(method=2)
#     img_obj.save(target/"about.png")

for i in source.glob("*.png"):
    try:
        with Image.open(i) as img_obj:
            img_obj = img_obj.quantize(method=2)  # Quantize uses the 'P' mode. It reduces the file size.
            img_obj.save("result/" + i.stem + ".png", optimize=True)
    except:
        print(i)

print("Process done.")
