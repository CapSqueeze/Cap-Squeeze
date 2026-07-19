import re

with open('flavors.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the 12 flavors section
match = re.search(r'(<!-- 12 FLAVORS SECTION -->.*?</section>)', html, re.DOTALL)
if match:
    flavors_section = match.group(1)
    
    # Remove it from original place
    html = html.replace(flavors_section, '')
    
    # Insert it above filter-tabs
    html = html.replace('<!-- Filter Tabs -->', flavors_section + '\n\n      <!-- Filter Tabs -->')

    with open('flavors.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("flavors.html reordered.")
else:
    print("Could not find the 12 flavors section.")


with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_card = '''
.flavor-mini-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  display: flex;
  flex-direction: column;
}

.flavor-mini-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(24, 58, 29, 0.08);
}
'''

new_card = '''
.flavor-mini-card {
  background: transparent;
  border: none;
  padding: 16px;
  text-align: center;
  transition: transform 0.2s ease;
  display: flex;
  flex-direction: column;
}

.flavor-mini-card:hover {
  transform: translateY(-4px);
}
'''

if old_card.strip() in css.strip() or '.flavor-mini-card {' in css:
    css = re.sub(r'\.flavor-mini-card \{.*?\n\}', '.flavor-mini-card {\n  background: transparent;\n  border: none;\n  padding: 16px;\n  text-align: center;\n  transition: transform 0.2s ease;\n  display: flex;\n  flex-direction: column;\n}', css, flags=re.DOTALL)
    css = re.sub(r'\.flavor-mini-card:hover \{.*?\n\}', '.flavor-mini-card:hover {\n  transform: translateY(-4px);\n}', css, flags=re.DOTALL)
    
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css minimalized.")
else:
    print("Could not find the exact old card css.")
