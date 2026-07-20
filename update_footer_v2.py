import os
import glob

def update_files():
    html_files = glob.glob("*.html")
    
    replace_blog = '<li><span style="opacity:.5;font-size:.85rem;cursor:default;" title="Coming Soon">Blog (Coming Soon)</span></li>'
    new_blog = '<li><a href="newsletter.html">Newsletter</a></li>'
    
    menu_search = '<li><a href="flavors.html">Shop Flavors</a></li>\n          <li><a href="about.html">About Us</a></li>'
    menu_replace = '<li><a href="flavors.html">Shop Flavors</a></li>\n          <li><a href="newsletter.html">Newsletter</a></li>\n          <li><a href="about.html">About Us</a></li>'

    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # 1. Replace Blog (Coming Soon)
        content = content.replace(replace_blog, new_blog)
        
        # 2. Update Menu
        content = content.replace(menu_search, menu_replace)
        
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {file_path}")

if __name__ == "__main__":
    update_files()
