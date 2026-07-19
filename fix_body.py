import os
import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Replace literal \n</body> string with actual newline and </body>
    c = c.replace('\\n</body>', '\n</body>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

print("Fixed body tag issue!")
