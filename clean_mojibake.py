import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

replacements = {
    'ðŸ’›': '💛',
    'âœ…': '✅',
    'ðŸš«': '🚫',
    'ðŸ‡®ðŸ‡³': '🇮🇳',
    'ðŸ”’': '🔒',
    'ðŸ’¬': '💬',
    'â‚¹': '₹',
    'â€”': '—',
    'ðŸ †': '🏆',
    'ðŸ’°': '💰'
}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mojibake reversed successfully!")
