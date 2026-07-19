import re

with open('faq.html', 'r', encoding='utf-8') as f:
    content = f.read()

shipping_section = '''<section class="faq-section" id="shipping" style="margin-top: 60px;">
      <h2>Shipping & Returns</h2>

      <div class="faq-item">
        <button class="faq-q">How long does shipping take? <span class="faq-q-icon">+</span></button>
        <div class="faq-a">We deliver anywhere in India within 3-5 business days. Metro cities usually receive orders within 48 hours via premium courier partners like Bluedart and Delhivery.</div>
      </div>
    </section>

  </div>'''

start_marker = '<section class="faq-section" id="shipping"'
end_marker = '<!-- ========== FOOTER ========== -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + shipping_section + '\n\n  ' + content[end_idx:]
    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully trimmed FAQ to 10 items.")
else:
    print("Could not find markers in faq.html")
