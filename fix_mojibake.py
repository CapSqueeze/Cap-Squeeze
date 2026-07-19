import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use regex to catch variations of these corrupted strings, or just simple string replacements.
replacements = {
    "dY'>": "❤️",
    "o.": "✅",
    "dYrdY3": "🇮🇳",
    "dYs": "💧",
    "dYs": "💧",
    "dY\"'": "🔒",
    "dY'": "💬",
    "âœ...": "✅",
    "ðŸš«": "🚫",
    "ðŸ‡®ðŸ‡³": "🇮🇳",
    "ðŸ’>": "❤️",
    "ðŸ’'": "🔒",
    "ðŸ’": "💬"
}

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed all mojibake/corrupted characters across HTML files.")
