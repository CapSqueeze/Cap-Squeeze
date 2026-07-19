import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<label class="nl-check">\s*<input type="checkbox">.*?</label>', re.DOTALL)
content = pattern.sub('', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed checkbox from newsletter form.")
