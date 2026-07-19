import os
import shutil
import re

# 1. Expand the footer description and update the links
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use a simple regex to replace the footer brand description and the Info links
old_brand_desc_pattern = r'<p style="font-size:\.9rem;opacity:\.85;margin-bottom:16px;line-height:1\.6;">India\'s first flavoured bottle cap\. Zero sugar\. Any bottle\. 12\+ flavors\.</p>'
new_brand_desc = '<p style="font-size:.9rem;opacity:.85;margin-bottom:16px;line-height:1.6;">Cap Squeeze is India\'s first flavoured bottle cap. Turn any standard water bottle into a delicious, zero-sugar, vitamin-enhanced drink instantly. Over 12+ refreshing flavors made with real fruit extracts.</p>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update brand description
    content = re.sub(old_brand_desc_pattern, new_brand_desc, content)

    # Update links
    content = content.replace('<a href="faq.html#shipping">Shipping Info</a>', '<a href="shipping.html">Shipping Info</a>')
    content = content.replace('<a href="faq.html#returns">Returns Policy</a>', '<a href="returns.html">Returns Policy</a>')
    content = content.replace('<a href="contact.html" title="Careers — We\'re Hiring Soon">Careers</a>', '<a href="careers.html">Careers</a>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)


# 2. Build the new pages based on newsletter.html structure
def create_page(filename, title, desc, content_html):
    shutil.copy('newsletter.html', filename)
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Title and meta description
    content = content.replace('<title>Newsletter — Cap Squeeze</title>', f'<title>{title}</title>')
    content = content.replace('<meta name="description" content="Join the Squeeze Club! Subscribe to our newsletter for exclusive discounts, new flavor drops, and daily hydration tips.">', f'<meta name="description" content="{desc}">')

    # Make the nav link active (none of these are in the main nav, so we remove active class)
    content = content.replace('href="newsletter.html" class="nav-link nav-link--active"', 'href="newsletter.html" class="nav-link"')

    # Replace the main content block
    main_content_start = content.find('<!-- PAGE HERO -->')
    main_content_end = content.find('<!-- FOOTER -->')

    if main_content_start != -1 and main_content_end != -1:
        content = content[:main_content_start] + content_html + content[main_content_end:]
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Shipping Page
shipping_html = '''  <!-- PAGE HERO -->
  <section class="page-hero" style="min-height: 50vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: var(--bg-surface); padding: 40px;">
    <p class="page-hero-eyebrow">Info</p>
    <h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 20px;">Shipping <span class="gradient-text">Policy.</span></h1>
  </section>

  <section style="padding: 80px 40px; background: var(--bg-card);">
    <div style="max-width: 800px; margin: 0 auto; color: var(--color-text-muted); font-size: 1.05rem; line-height: 1.7;">
      <h3 style="color: var(--color-text-main); font-size: 1.6rem; font-weight: 800; margin-bottom: 20px;">Processing Times</h3>
      <p style="margin-bottom: 40px;">All orders are processed and dispatched within 1-2 business days from our fulfillment center. Orders placed after 1 PM IST or on weekends/public holidays will be processed the next business day.</p>
      
      <h3 style="color: var(--color-text-main); font-size: 1.6rem; font-weight: 800; margin-bottom: 20px;">Delivery Estimates</h3>
      <ul style="margin-bottom: 40px; list-style-type: disc; padding-left: 20px;">
        <li style="margin-bottom: 10px;"><strong>Metro Cities:</strong> 2-3 Business Days</li>
        <li style="margin-bottom: 10px;"><strong>Rest of India:</strong> 4-6 Business Days</li>
        <li style="margin-bottom: 10px;"><strong>Remote Locations:</strong> Up to 8 Business Days</li>
      </ul>

      <h3 style="color: var(--color-text-main); font-size: 1.6rem; font-weight: 800; margin-bottom: 20px;">Shipping Costs</h3>
      <p style="margin-bottom: 40px;">We offer <strong>Free Standard Shipping</strong> on all orders above ₹499. For orders under ₹499, a flat shipping rate of ₹50 applies. Expedited shipping options may be available at checkout depending on your pin code.</p>
      
      <p style="font-style: italic;">If your order is significantly delayed, please reach out to our support team with your order number via the <a href="contact.html" style="color: var(--color-coral); text-decoration: underline;">Contact Page</a>.</p>
    </div>
  </section>
'''
create_page('shipping.html', 'Shipping Info — Cap Squeeze', 'Shipping processing times, delivery estimates, and costs for Cap Squeeze orders.', shipping_html)

# Returns Page
returns_html = '''  <!-- PAGE HERO -->
  <section class="page-hero" style="min-height: 50vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: var(--bg-surface); padding: 40px;">
    <p class="page-hero-eyebrow">Info</p>
    <h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 20px;">Returns <span class="gradient-text">Policy.</span></h1>
  </section>

  <section style="padding: 80px 40px; background: var(--bg-card);">
    <div style="max-width: 800px; margin: 0 auto; color: var(--color-text-muted); font-size: 1.05rem; line-height: 1.7;">
      <h3 style="color: var(--color-text-main); font-size: 1.6rem; font-weight: 800; margin-bottom: 20px;">14-Day Guarantee</h3>
      <p style="margin-bottom: 40px;">We stand behind the quality of Cap Squeeze. Because our products are consumable food items, we cannot accept returns on opened packages for health and safety reasons. However, if your items arrive damaged or defective, we offer a hassle-free 14-day replacement guarantee.</p>
      
      <h3 style="color: var(--color-text-main); font-size: 1.6rem; font-weight: 800; margin-bottom: 20px;">Initiating a Return</h3>
      <p style="margin-bottom: 40px;">If your order is incorrect or damaged during transit, please contact us within 14 days of delivery. Send us an email at <strong>hello@capsqueeze.com</strong> with your order number and photos of the damaged items. Our team will review the issue and dispatch a replacement immediately.</p>

      <h3 style="color: var(--color-text-main); font-size: 1.6rem; font-weight: 800; margin-bottom: 20px;">Refunds</h3>
      <p style="margin-bottom: 40px;">In cases where a replacement is not possible or desired, refunds will be processed to the original method of payment within 5-7 business days of approval.</p>
    </div>
  </section>
'''
create_page('returns.html', 'Returns Policy — Cap Squeeze', 'Learn about our 14-day guarantee, returns, and refund policy for Cap Squeeze products.', returns_html)

# Careers Page
careers_html = '''  <!-- PAGE HERO -->
  <section class="page-hero" style="min-height: 50vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: var(--bg-surface); padding: 40px;">
    <p class="page-hero-eyebrow">Info</p>
    <h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 20px;">Careers at <span class="gradient-text">Cap Squeeze.</span></h1>
  </section>

  <section style="padding: 80px 40px; background: var(--bg-card);">
    <div style="max-width: 800px; margin: 0 auto; color: var(--color-text-muted); font-size: 1.05rem; line-height: 1.7; text-align: center;">
      <i data-lucide="rocket" style="width: 48px; height: 48px; margin-bottom: 24px; color: var(--color-coral);"></i>
      <h3 style="color: var(--color-text-main); font-size: 1.6rem; font-weight: 800; margin-bottom: 20px;">Help Us Build the Future of Hydration</h3>
      <p style="margin-bottom: 40px;">We are a fast-growing, passionate team dedicated to eradicating single-use plastic while making water taste amazing. If you are driven, creative, and want to make a real impact on health and sustainability in India, we want to hear from you.</p>
      
      <div style="background: rgba(24,58,29,0.03); padding: 40px; border-radius: 16px; border: 1px solid var(--border-color); text-align: left; margin-bottom: 40px;">
        <h4 style="color: var(--color-text-main); font-size: 1.3rem; font-weight: 700; margin-bottom: 15px;">Current Openings</h4>
        <p style="margin-bottom: 0;">We currently do not have any open positions listed. However, we are always on the lookout for exceptional talent in Marketing, Operations, and Product Development.</p>
      </div>

      <p>Send your resume and a brief cover letter telling us why you'd be a great fit to <a href="mailto:careers@capsqueeze.com" style="color: var(--color-coral); text-decoration: underline; font-weight: 600;">careers@capsqueeze.com</a>.</p>
    </div>
  </section>
'''
create_page('careers.html', 'Careers — Cap Squeeze', 'Join the Cap Squeeze team and help us build the future of hydration and sustainability.', careers_html)

print("Info pages created and footer updated successfully!")
