import os
import re

# We will use index.html as the ultimate source of truth for the Header, Nav, and Footer.
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Helper function to extract a block of HTML using start and end markers
def extract_block(content, start_marker, end_marker):
    start = content.find(start_marker)
    if start == -1:
        return None
    end = content.find(end_marker, start)
    if end == -1:
        # If no end marker is found, assume it goes to the end (shouldn't happen for these)
        return None
    return content[start:end + len(end_marker)]

# The header/nav section starts at top-bar and ends at the end of main-nav
# Wait, let's extract each piece precisely.

# In index.html, the markers might be slightly different. Let's define the blocks.
top_bar_start = '  <!-- ========== TOP UTILITY BAR ========== -->'
top_bar_alt = '  <!-- TOP BAR -->'
header_start = '  <!-- ========== MAIN HEADER ========== -->'
header_alt = '  <!-- HEADER -->'
nav_start = '  <!-- ========== MAIN NAVIGATION ========== -->'
nav_alt = '  <!-- NAV -->'
hero_start = '  <!-- ========== HERO ========== -->'
hero_alt = '  <!-- PAGE HERO -->'
footer_start = '  <!-- ========== FOOTER ========== -->'
footer_alt = '  <!-- FOOTER -->'
body_end = '</body>'

# Let's just find the start of the top bar, and the start of the hero. Everything in between is the header.
start_of_header_idx = index_content.find(top_bar_start)
if start_of_header_idx == -1:
    start_of_header_idx = index_content.find(top_bar_alt)

end_of_header_idx = index_content.find(hero_start)
if end_of_header_idx == -1:
    end_of_header_idx = index_content.find(hero_alt)

if start_of_header_idx == -1 or end_of_header_idx == -1:
    print("Could not find header boundaries in index.html")
    exit(1)

master_header = index_content[start_of_header_idx:end_of_header_idx]

# Now for the footer. It starts at the footer marker and ends at the body end.
start_of_footer_idx = index_content.find(footer_start)
if start_of_footer_idx == -1:
    start_of_footer_idx = index_content.find(footer_alt)

end_of_footer_idx = index_content.find(body_end)

if start_of_footer_idx == -1 or end_of_footer_idx == -1:
    print("Could not find footer boundaries in index.html")
    exit(1)

master_footer = index_content[start_of_footer_idx:end_of_footer_idx]

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Header
    f_start_head = content.find(top_bar_start)
    if f_start_head == -1:
        f_start_head = content.find(top_bar_alt)
        
    f_end_head = content.find(hero_start)
    if f_end_head == -1:
        f_end_head = content.find(hero_alt)
        
    # Wait, auth pages use a different hero: <!-- PAGE HERO (Hidden for Auth pages) --> or similar
    if f_end_head == -1:
        f_end_head = content.find('  <!-- PAGE HERO')
        
    if f_start_head != -1 and f_end_head != -1:
        content = content[:f_start_head] + master_header + content[f_end_head:]
    else:
        print(f"Could not find header boundaries in {file}")

    # Replace Footer
    f_start_foot = content.find(footer_start)
    if f_start_foot == -1:
        f_start_foot = content.find(footer_alt)
        
    f_end_foot = content.find(body_end)
    
    if f_start_foot != -1 and f_end_foot != -1:
        content = content[:f_start_foot] + master_footer + content[f_end_foot:]
    else:
        print(f"Could not find footer boundaries in {file}")
        
    # In index.html the header link for "Home" is active. We should remove the active class 
    # for all other pages, or dynamically add it.
    # Actually, the user asked for the *same* header, but dynamically setting active class is best practice.
    # Let's remove the active class from all links in master_header for the other pages, then add it to the correct one.
    
    # Strip all active classes first
    content = content.replace('nav-link--active', '')
    
    # Add it back based on filename
    if file == 'about.html':
        content = content.replace('href="about.html" class="nav-link"', 'href="about.html" class="nav-link nav-link--active"')
    elif file == 'flavors.html':
        content = content.replace('href="flavors.html" class="nav-link"', 'href="flavors.html" class="nav-link nav-link--active"')
    elif file == 'how-it-works.html':
        content = content.replace('href="how-it-works.html" class="nav-link"', 'href="how-it-works.html" class="nav-link nav-link--active"')
    elif file == 'newsletter.html':
        content = content.replace('href="newsletter.html" class="nav-link"', 'href="newsletter.html" class="nav-link nav-link--active"')
    elif file == 'contact.html':
        content = content.replace('href="contact.html" class="nav-link"', 'href="contact.html" class="nav-link nav-link--active"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Headers and Footers perfectly synchronized across all files!")
