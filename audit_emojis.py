import os
import emoji

def find_emojis(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    found_emojis = []
    for char in content:
        if char in emoji.EMOJI_DATA:
            found_emojis.append(char)
            
    return list(set(found_emojis))

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
all_found = {}

for f in html_files:
    emojis = find_emojis(f)
    if emojis:
        all_found[f] = emojis

with open('emoji_audit_results.txt', 'w', encoding='utf-8') as out:
    if all_found:
        out.write('Found emojis:\n')
        for f, emjs in all_found.items():
            out.write(f"{f}: {' '.join(emjs)}\n")
    else:
        out.write('No emojis found in any HTML files!\n')
