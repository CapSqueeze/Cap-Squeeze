from PIL import Image

def remove_bg(img_path, out_path, tolerance=30):
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    # Get corner colors to determine background
    w, h = img.size
    corners = [img.getpixel((0,0)), img.getpixel((w-1,0)), img.getpixel((0,h-1)), img.getpixel((w-1,h-1))]
    bg_color = corners[0] # Assume top-left is bg
    
    new_data = []
    for item in data:
        # Check if color is within tolerance of bg_color
        if (abs(item[0] - bg_color[0]) <= tolerance and
            abs(item[1] - bg_color[1]) <= tolerance and
            abs(item[2] - bg_color[2]) <= tolerance):
            new_data.append((255, 255, 255, 0)) # transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, "PNG")

remove_bg(r'D:\Harsh Vashishtha\Shubham Prajapat\Cap Squeeze\images\logo\logo.png', r'D:\Harsh Vashishtha\Shubham Prajapat\Cap Squeeze\images\logo\logo_transparent.png', tolerance=15)
print("Background removed via color tolerance.")
