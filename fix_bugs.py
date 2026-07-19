import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the \n literal bug in head
    content = content.replace('\\n  <script src="https://unpkg.com/lucide@latest"></script>\\n</head>', '  <script src="https://unpkg.com/lucide@latest"></script>\\n</head>')
    
    # 2. Fix the broken Cap Squeeze.png logo
    bad_logo = '<img src="Cap Squeeze.png" alt="Cap Squeeze" style="height: 48px; width: auto; display: inline-block;">'
    good_logo = '<img src="images/logo.png" alt="Cap Squeeze" style="height:40px; margin-right:10px;">'
    content = content.replace(bad_logo, good_logo)
    
    # 3. Remove the duplicate/broken favicon link
    bad_favicon = '  <link rel="icon" type="image/png" href="Cap Squeeze.png">\\n'
    content = content.replace(bad_favicon, '')
    
    # 4. Fix the yellow circle mojibake in the marquee (index.html)
    content = content.replace('ðŸŸ¡', '&bull;')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Bug fixes applied successfully!")
