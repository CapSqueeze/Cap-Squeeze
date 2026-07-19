import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Product Card Minimalist Changes
css = css.replace('  background: var(--bg-ink);\\n  border: 1px solid var(--border-color);', '  background: transparent;\\n  border: none;')
css = css.replace('''  border-color: var(--border-hover);
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(24, 58, 29, 0.1);''', '''  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(24, 58, 29, 0.05);''')

# 2. Card Image Minimalist Changes
css = css.replace('  border-bottom: 1px solid var(--border-color);', '  border-bottom: none;')

# 3. Stepper and Buttons
css = css.replace('  border: 1px solid var(--border-color);\\n  border-radius: 50px;\\n  overflow: hidden;\\n  height: 36px;\\n  background: rgba(24,58,29,0.02);', '  border: none;\\n  border-radius: 50px;\\n  overflow: hidden;\\n  height: 36px;\\n  background: rgba(24,58,29,0.04);')
css = css.replace('  border-left: 1px solid var(--border-color);\\n  border-right: 1px solid var(--border-color);', '  border-left: none;\\n  border-right: none;')
css = css.replace('  border: 1px solid var(--border-color);\\n  border-radius: 50px;', '  border: none;\\n  border-radius: 50px;\\n  background: rgba(24,58,29,0.04);')

# 4. App Banner / Phone Frame
css = css.replace('''  background: #111116;
  border: 1px solid var(--border-color);
  border-radius: 36px;
  padding: 12px;
  box-shadow: 0 25px 60px rgba(24, 58, 29, 0.15);''', '''  background: transparent;
  border: none;
  padding: 0;
  box-shadow: none;''')
css = css.replace('''  background: #183a1d;
  border: 1px solid var(--border-color);''', '''  background: transparent;
  border: none;''')

# 5. FAQ Items
css = css.replace('''  background: var(--bg-ink);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  margin-bottom: 16px;
  overflow: hidden;
  transition: all 0.3s;''', '''  background: transparent;
  border: none;
  border-bottom: 1px solid rgba(24,58,29,0.08);
  border-radius: 0;
  margin-bottom: 0;
  overflow: hidden;
  transition: all 0.3s;''')
css = css.replace('''  border-color: var(--border-hover);
  box-shadow: 0 4px 15px rgba(24, 58, 29, 0.05);''', '''  background: rgba(24,58,29,0.02);''')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Global minimal CSS applied successfully!")
