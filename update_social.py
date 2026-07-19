import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

new_social = '''        <div class="footer-social">
          <a href="https://www.facebook.com/CapSqueeze" target="_blank" aria-label="Facebook">
            <i data-lucide="facebook" class="icon-inline"></i>
          </a>
          <a href="https://www.instagram.com/CapSqueeze" target="_blank" aria-label="Instagram">
            <i data-lucide="instagram" class="icon-inline"></i>
          </a>
          <a href="https://x.com/CapSqueeze" target="_blank" aria-label="X (Twitter)">
            <i data-lucide="twitter" class="icon-inline"></i>
          </a>
          <a href="https://www.linkedin.com/company/CapSqueeze" target="_blank" aria-label="LinkedIn">
            <i data-lucide="linkedin" class="icon-inline"></i>
          </a>
          <a href="https://www.youtube.com/@CapSqueeze" target="_blank" aria-label="YouTube">
            <i data-lucide="youtube" class="icon-inline"></i>
          </a>
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the footer-social block using regex
    pattern = r'<div class="footer-social">.*?</div>'
    # Use re.DOTALL to match across multiple lines
    content = re.sub(pattern, new_social, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Social links updated successfully!")
