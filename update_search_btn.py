import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use regex to find the search button and the start of the right icons, then move it.

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the search button block
    search_btn_pattern = r'      <button class="search-icon-btn" aria-label="Search">\s*<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4\.35-4\.35"/></svg>\s*</button>\n'
    
    match = re.search(search_btn_pattern, content)
    if match:
        search_btn_html = match.group(0)
        
        # Remove the original search button
        content = content.replace(search_btn_html, '')
        
        # Insert it at the beginning of the header-right-icons div
        right_icons_start = '      <div class="header-right-icons">\n'
        
        # Make the search button look like the other icons (a bit less margin if it's in the flex container, maybe we just drop it in)
        # Actually it's just a button.
        
        if right_icons_start in content:
            new_right_icons = right_icons_start + search_btn_html
            content = content.replace(right_icons_start, new_right_icons)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"header-right-icons not found in {file}")
    else:
        print(f"search button not found in {file}")

print("Search button moved to the right side successfully!")
