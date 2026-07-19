import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix newsletter text color
css = css.replace('.newsletter-banner {\n  background: #183a1d;', '.newsletter-banner {\n  background: #183a1d;\n  color: var(--bg-ink);')
css = css.replace('.newsletter-inner h3 {\n  font-size: 3rem;', '.newsletter-inner h3 {\n  font-size: 3rem;\n  color: var(--bg-ink);')
css = css.replace('.newsletter-inner p {', '.newsletter-inner p {\n  color: var(--bg-ink);')

# Fix footer text color
css = css.replace('.footer-bottom {\n  max-width: 1200px;', '.footer-bottom {\n  max-width: 1200px;\n  color: var(--bg-ink);')
css = css.replace('.footer-copyright {\n  background: #183a1d;', '.footer-copyright {\n  background: #183a1d;\n  color: var(--bg-ink);')

# Fix trust badges in footer bottom so their text shows up
css = css.replace('.trust-badge {\n  display: flex;', '.trust-badge {\n  display: flex;\n  color: var(--bg-ink);')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS fixes applied.")
