from PIL import Image

# Open the composite image
img = Image.open(r'C:\Users\rr\.gemini\antigravity-ide\brain\ca17a7cc-53c0-4977-9da1-65a51e5d8fd1\media__1784459730963.png')
width, height = img.size

# Panel widths are exactly 256 (1024 / 4)
w = 256

panel1 = img.crop((0, 0, w, height)) # Single Cap
panel2 = img.crop((w, 0, w*2, height)) # Bottle
panel3 = img.crop((w*2, 0, w*3, height)) # Stacked Caps

dest_dir = r'images\products'

# Save single cap for all flavors
for flavor in ['cap-lime.png', 'cap-mango.png', 'cap-blueberry.png', 'cap-mint.png', 'cap-orange.png', 'cap-strawberry.png']:
    panel1.save(f"{dest_dir}\\{flavor}")

# Save stacked caps
panel3.save(f"{dest_dir}\\caps-group.png")

# Save bottle
panel2.save(f"{dest_dir}\\caps-on-bottle.png")

print("All images cropped and saved perfectly!")
