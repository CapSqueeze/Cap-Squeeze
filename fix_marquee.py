import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

marquee_items = [
    "🟡 Zero Sugar",
    "🟡 12+ Flavors",
    "🟡 Any Bottle",
    "🟡 Natural Ingredients",
    "🟡 Electrolytes Included",
    "🟡 Made in India 🇮🇳",
    "🟡 Eco-Friendly",
    "🟡 No Artificial Colors",
    "🟡 FSSAI Certified",
    "🟡 Free Shipping ₹499+"
]

span_html = '\n'.join([f"      <span>{item}</span>" for item in marquee_items])
# Duplicate for loop
marquee_content = f"\n{span_html}\n      <!-- duplicate for seamless loop -->\n{span_html}\n    "

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = re.sub(r'(<div class="marquee-track">).*?(</div>)', r'\1' + marquee_content + r'\2', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Restored full marquee with proper emojis.")
