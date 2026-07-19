from PIL import Image

img = Image.open(r'D:\Harsh Vashishtha\Shubham Prajapat\Cap Squeeze\images\logo\logo.png')
print(f"Mode: {img.mode}, Size: {img.size}")
if img.mode == 'RGBA':
    extrema = img.getextrema()
    if extrema[3][0] < 255:
        print("Image already has transparency.")
    else:
        print("Image has alpha channel but no transparent pixels.")
else:
    print("Image does not have transparency.")
