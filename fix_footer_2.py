import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Coupons section
    coupons_pattern = re.compile(r'<div style="margin-top:20px;">\s*<p style="font-size:\.8rem;font-weight:600;margin-bottom:8px;opacity:\.9;">Coupons</p>.*?</div>', re.DOTALL)
    content = coupons_pattern.sub('', content)

    # Remove Payment Methods text
    payment_title = re.compile(r'<p class="footer-payment-title">We accept the following payment methods</p>', re.DOTALL)
    content = payment_title.sub('', content)

    payment_icons = re.compile(r'<div class="footer-payment-icons">.*?</div>', re.DOTALL)
    content = payment_icons.sub('', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Cleaned up footer across all HTML files (Attempt 2).')
