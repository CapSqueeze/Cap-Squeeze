import os

# 1. Update contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('✉️', '<i data-lucide="mail" class="icon-inline"></i>')
content = content.replace('✉', '<i data-lucide="mail" class="icon-inline"></i>')
content = content.replace('🤝', '<i data-lucide="briefcase" class="icon-inline"></i>')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('📅', '<i data-lucide="calendar" class="icon-inline"></i>')
content = content.replace('💡', '<i data-lucide="lightbulb" class="icon-inline"></i>')
content = content.replace('🌐', '<i data-lucide="globe" class="icon-inline"></i>')
content = content.replace('🌿', '<i data-lucide="leaf" class="icon-inline"></i>')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Update flavors.html
with open('flavors.html', 'r', encoding='utf-8') as f:
    content = f.read()

flavor_map = {
    '🍓': '#ff4d4d',
    '🥝': '#8bc34a',
    '🫐': '#5c6bc0',
    '🍊': '#ff9800',
    '🍒': '#e91e63',
    '🥭': '#ffc107',
    '🍉': '#f44336',
    '🍍': '#ffeb3b',
    '🍑': '#ffab40',
    '🍏': '#4caf50',
    '🌿': '#81c784'
}

for emoji, color in flavor_map.items():
    dot = f'<span class="flavor-dot" style="background-color: {color};"></span>'
    content = content.replace(emoji, dot)

with open('flavors.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 4. Add CSS for .flavor-dot
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n/* Flavor Dot */\n.flavor-dot {\n  width: 14px;\n  height: 14px;\n  border-radius: 50%;\n  display: inline-block;\n  margin-right: 8px;\n  vertical-align: middle;\n  box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);\n}\n')

print("All remaining emojis replaced successfully!")
