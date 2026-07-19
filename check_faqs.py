import re

with open('faq.html', 'r', encoding='utf-8') as f:
    content = f.read()

faq_items = re.findall(r'(<div class="faq-item">.*?</div>\n)', content, re.DOTALL)
print(f"Total FAQs found: {len(faq_items)}")

# We will keep exactly 10 FAQs. We can just parse the file and rebuild it.
