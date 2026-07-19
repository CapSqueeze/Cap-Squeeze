import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Coupons section
    # Let's use regex to find and remove it.
    # We want to remove from <p class="footer-help" style="margin-top:20px;">Coupons</p> 
    # to FLAT50 — ₹50 off<br><span style="font-size:0.75rem;opacity:0.6;">₹499+</span></p>
    coupons_pattern = re.compile(r'<p class="footer-help"[^>]*>Coupons</p>.*?(?=</div>\s*</div>)', re.DOTALL)
    content = coupons_pattern.sub('', content)

    # Remove Payment Methods text
    # Let's find "VISA Mastercard PayPal UPI Razorpay COD" and the "Payment Methods" links
    payment_methods_links = re.compile(r'<a href="#">Payment Methods</a>', re.DOTALL)
    content = payment_methods_links.sub('', content)

    visa_text = re.compile(r'<p style="font-size:\.8rem;opacity:\.6;margin-top:20px;">VISA Mastercard PayPal UPI Razorpay COD</p>', re.DOTALL)
    content = visa_text.sub('', content)

    # Also remove the "We accept the following payment methods" text if it exists
    we_accept = re.compile(r'<p style="font-size: 0\.85rem; color: var\(--color-text-muted\);">We accept the following payment methods</p>', re.DOTALL)
    content = we_accept.sub('', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Cleaned up footer across all HTML files.')
