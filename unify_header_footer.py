import os
import glob
import re

def main():
    with open("index.html", "r", encoding="utf-8") as f:
        index_content = f.read()

    # Extract Header
    header_pattern = re.compile(r'(<!-- ========== TOP UTILITY BAR ========== -->\s*<div class="top-bar">.*?</nav>)', re.DOTALL)
    header_match = header_pattern.search(index_content)
    if not header_match:
        print("Header not found in index.html")
        return
    master_header = header_match.group(1)

    # Extract Footer (include WhatsApp button)
    footer_pattern = re.compile(r'(<!-- ========== FOOTER ========== -->\s*<footer class="site-footer">.*?</footer>\s*<!-- WhatsApp Floating Button -->\s*<a .*?</a>)', re.DOTALL)
    # wait, the comment for footer might not be exact. Let's just match from <footer to </footer>
    footer_pattern2 = re.compile(r'(<footer class="site-footer">.*?</footer>)', re.DOTALL)
    footer_match = footer_pattern2.search(index_content)
    if not footer_match:
        print("Footer not found in index.html")
        return
    master_footer = footer_match.group(1)

    whatsapp_pattern = re.compile(r'(<!-- WhatsApp Floating Button -->\s*<a.*?</a>)', re.DOTALL)
    whatsapp_match = whatsapp_pattern.search(index_content)
    master_whatsapp = whatsapp_match.group(1) if whatsapp_match else ""

    html_files = glob.glob("*.html")
    for file in html_files:
        if file == "index.html":
            continue
            
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace Header
        # Some files might not have <!-- ========== TOP UTILITY BAR ========== -->
        file_header_pattern = re.compile(r'(?:<!-- ========== TOP UTILITY BAR ========== -->\s*)?<div class="top-bar">.*?</nav>', re.DOTALL)
        content = file_header_pattern.sub(master_header, content)

        # Replace Footer
        file_footer_pattern = re.compile(r'(?:<!-- ========== FOOTER ========== -->\s*)?<footer class="site-footer">.*?</footer>', re.DOTALL)
        content = file_footer_pattern.sub(master_footer, content)

        # Add WhatsApp button if missing
        if "WhatsApp Floating Button" not in content and master_whatsapp:
            content = content.replace("</footer>", f"</footer>\n\n  {master_whatsapp}")

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Updated {file}")

if __name__ == "__main__":
    main()
