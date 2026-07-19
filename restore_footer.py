import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

clean_footer_block = '''    <div class="footer-copyright">
      <p>&copy; 2026 Cap Squeeze. All rights reserved. Made with ❤️ in India 🇮🇳</p>
      <div class="trust-badges">
        <span class="trust-badge">✅ FSSAI Certified</span>
        <span class="trust-badge">🚫 Zero Sugar</span>
        <span class="trust-badge">🇮🇳 Made in India</span>
        <span class="trust-badge">🔒 Secure Payments</span>
      </div>
    </div>
  </footer>

  <!-- WhatsApp Floating Button -->
  <a href="https://wa.me/91XXXXXXXXXX?text=Hi%20Cap%20Squeeze!%20I%20have%20a%20question."
     target="_blank"
     class="whatsapp-float"
     aria-label="Chat on WhatsApp">
    💬
  </a>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find and replace everything from <div class="footer-copyright"> to the </a>
    pattern = r'    <div class="footer-copyright">.*?</a>'
    new_content = re.sub(pattern, clean_footer_block, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Footer restored globally.")
