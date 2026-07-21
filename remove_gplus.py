import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
pattern = re.compile(r'\s*<a href="#" class="social-circle social-gp" aria-label="Google Plus"><span style="font-weight:bold;font-family:serif;font-size:14px;">G\+</span></a>')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(pattern, '', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Removed G+ icon from {f}")
