import re

with open('faq.html', 'r', encoding='utf-8') as f:
    content = f.read()

faq_items = re.findall(r'<button class="faq-q">(.*?)</button>', content, re.DOTALL)
for i, q in enumerate(faq_items):
    print(f"{i+1}: {q}")
