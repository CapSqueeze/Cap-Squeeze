import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_nav = f'''    <div class="nav-inner">
      <a href="index.html" class="nav-link{' nav-link--active' if file == 'index.html' else ''}">Home</a>
      <a href="flavors.html" class="nav-link{' nav-link--active' if file == 'flavors.html' else ''}">Shop Flavors</a>
      <a href="how-it-works.html" class="nav-link{' nav-link--active' if file == 'how-it-works.html' else ''}">How It Works</a>
      <a href="newsletter.html" class="nav-link{' nav-link--active' if file == 'newsletter.html' else ''}">Newsletter</a>
      <a href="about.html" class="nav-link{' nav-link--active' if file == 'about.html' else ''}">About</a>
      <a href="contact.html" class="nav-link{' nav-link--active' if file == 'contact.html' else ''}">Contact</a>
    </div>'''

    pattern = r'<div class="nav-inner">.*?</div>'
    content = re.sub(pattern, new_nav, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Main navigation updated successfully!")
