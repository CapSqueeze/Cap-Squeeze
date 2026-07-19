import os

# Google, Facebook, LinkedIn SVGs
new_social_icons = '''        <div class="social-icons">
          <a href="#" class="social-icon" aria-label="Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
          </a>
          <a href="#" class="social-icon" aria-label="Google">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16c2.2 0 4-1.8 4-4H12"/><path d="M15.3 10.3c-.8-1.5-2.4-2.3-4.3-2.3-2.8 0-5 2.2-5 5s2.2 5 5 5c1.8 0 3.3-1 4.1-2.5"/></svg>
          </a>
          <a href="#" class="social-icon" aria-label="LinkedIn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
          </a>
        </div>'''

files = ['login.html', 'signup.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace the whole <div class="social-icons"> ... </div>
    start_idx = content.find('<div class="social-icons">')
    end_idx = content.find('</div>', start_idx) + 6
    
    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + new_social_icons + content[end_idx:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed social icons in {file}")
    else:
        print(f"Could not find social icons in {file}")
