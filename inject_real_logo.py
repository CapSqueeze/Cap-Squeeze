import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_logo = '<a href="index.html" class="site-logo">Cap Squeeze.</a>'
new_logo = '''<a href="index.html" class="site-logo" style="display:flex; align-items:center;">
        <img src="images/logo.png" alt="Cap Squeeze" style="height:40px; margin-right:10px;">
        Cap Squeeze.
      </a>'''

old_footer_logo = '<a href="index.html" class="footer-logo">Cap Squeeze.</a>'
new_footer_logo = '''<a href="index.html" class="footer-logo" style="display:flex; align-items:center; margin-bottom:15px;">
          <img src="images/logo.png" alt="Cap Squeeze" style="height:45px; margin-right:12px;">
          Cap Squeeze.
        </a>'''

favicon_tag = '  <link rel="icon" href="images/favicon.png" type="image/png">\n'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace logos
    content = content.replace(old_logo, new_logo)
    content = content.replace(old_footer_logo, new_footer_logo)
    
    # Inject favicon before closing </head> if not already there
    if 'favicon.png' not in content:
        content = content.replace('</head>', favicon_tag + '</head>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Logo and Favicon inserted in all HTML files.")
