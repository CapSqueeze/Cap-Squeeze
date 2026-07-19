import os
import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Replace literal \n string with actual newline
    c = c.replace('\\n</head>', '\n</head>')
    
    # Remove old favicon
    c = c.replace('  <link rel="icon" type="image/png" href="Cap Squeeze.png">\n', '')
    c = c.replace('<link rel="icon" type="image/png" href="Cap Squeeze.png">', '')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

print("Fixed!")
