import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# .top-bar color
css = css.replace(
    '.top-bar {\n  background: #183a1d;\n  color: var(--color-text-muted);',
    '.top-bar {\n  background: #183a1d;\n  color: #ffffff;'
)

# .top-bar-left a:hover
css = css.replace(
    '.top-bar-left a:hover { color: var(--color-text-main); }',
    '.top-bar-left a:hover { color: #ffffff; opacity: 0.8; }'
)

# .top-bar-center a
css = css.replace(
    '.top-bar-center a { color: var(--color-text-main); text-decoration: underline; }',
    '.top-bar-center a { color: #ffffff; text-decoration: underline; }'
)

# .login-link color
css = css.replace(
    '.login-link {\n  display: flex;\n  align-items: center;\n  gap: 6px;\n  color: var(--color-text-muted);\n}',
    '.login-link {\n  display: flex;\n  align-items: center;\n  gap: 6px;\n  color: #ffffff;\n}'
)

# .login-link:hover
css = css.replace(
    '.login-link:hover { color: var(--color-text-main); }',
    '.login-link:hover { color: #ffffff; opacity: 0.8; }'
)

# Also check if top-bar-left a needs a base color, because it inherits from somewhere
# usually links have a default color, we should set top-bar a explicitly
css = css.replace(
    '.top-bar-inner {\n  max-width: 1200px;',
    '.top-bar a {\n  color: #ffffff;\n}\n\n.top-bar-inner {\n  max-width: 1200px;'
)


with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS updated for top-bar")
