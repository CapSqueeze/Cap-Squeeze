import os
from PIL import Image

img = Image.open(r'C:\Users\rr\.gemini\antigravity-ide\brain\ca17a7cc-53c0-4977-9da1-65a51e5d8fd1\media__1784459730963.png')
w = 256
height = img.size[1]

panel1 = img.crop((0, 0, w, height)) # Single Cap

os.makedirs('temp_refs', exist_ok=True)
panel1.save(r'temp_refs\single_cap_ref.png')
print("Saved reference!")
