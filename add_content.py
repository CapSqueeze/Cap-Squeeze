import os
import shutil

# 1. Create newsletter.html by copying faq.html and replacing the main content
shutil.copy('faq.html', 'newsletter.html')
with open('newsletter.html', 'r', encoding='utf-8') as f:
    news_content = f.read()

# Replace the Title and meta description
news_content = news_content.replace('<title>FAQ — Cap Squeeze</title>', '<title>Newsletter — Cap Squeeze</title>')
news_content = news_content.replace('<meta name="description" content="Frequently Asked Questions about Cap Squeeze. Learn about our flavors, shipping, ingredients, and how our bottle caps work.">', '<meta name="description" content="Join the Squeeze Club! Subscribe to our newsletter for exclusive discounts, new flavor drops, and daily hydration tips.">')

# Make the nav link active
news_content = news_content.replace('href="faq.html" class="nav-link nav-link--active"', 'href="faq.html" class="nav-link"')
# (Newsletter isn't in the main nav, so we just remove the active class from FAQ)

# Replace the main content block
main_content_start = news_content.find('<!-- PAGE HERO -->')
main_content_end = news_content.find('<!-- FOOTER -->')

if main_content_start != -1 and main_content_end != -1:
    newsletter_html = '''  <!-- PAGE HERO -->
  <section class="page-hero" style="min-height: 70vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: var(--bg-ink); padding: 40px;">
    <p class="page-hero-eyebrow">The Squeeze Club</p>
    <h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 20px;">Join the <span class="gradient-text">Hydration Revolution.</span></h1>
    <p style="font-size: 1.2rem; color: var(--color-text-muted); max-width: 600px; margin: 0 auto 40px auto; line-height: 1.6;">
      Subscribe to get 10% off your first order, early access to exclusive new flavors, and daily tips for a healthier, more vibrant life. No spam, just pure hydration.
    </p>
    
    <form id="newsletter-form" style="display: flex; gap: 12px; width: 100%; max-width: 500px; margin: 0 auto;">
      <input type="email" placeholder="Enter your email address..." required style="flex: 1; padding: 16px 24px; border: none; border-radius: 50px; background: rgba(24,58,29,0.04); font-size: 1rem; color: var(--color-text-main); outline: none;">
      <button type="submit" class="btn-addcart" style="width: auto; padding: 0 32px; height: auto;">Subscribe</button>
    </form>
    <p id="newsletter-success" style="display: none; color: #4caf50; font-weight: 600; margin-top: 20px;">🎉 Welcome to the club! Check your inbox for your 10% off code.</p>
  </section>

'''
    news_content = news_content[:main_content_start] + newsletter_html + news_content[main_content_end:]
    
with open('newsletter.html', 'w', encoding='utf-8') as f:
    f.write(news_content)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Add Hydration Revolution section before the Testimonials
revolution_html = '''
  <!-- BRAND STORYTELLING -->
  <section style="padding: 100px 40px; background: var(--bg-surface); text-align: center;">
    <div style="max-width: 800px; margin: 0 auto;">
      <p style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 16px; opacity: 0.7;">Our Mission</p>
      <h2 style="font-size: 2.8rem; font-weight: 800; margin-bottom: 30px; line-height: 1.2;">Ditch the Sugar. Keep the Flavor.</h2>
      <p style="font-size: 1.2rem; color: var(--color-text-muted); line-height: 1.8; margin-bottom: 0;">
        We were tired of choosing between bland water and sugary sodas wrapped in single-use plastic. So we created Cap Squeeze. By concentrating real fruit extracts and essential electrolytes into a 100% recyclable cap, we're empowering you to turn any bottle into a premium hydration experience. It's better for your body, and better for the planet.
      </p>
    </div>
  </section>

  <!-- TESTIMONIALS -->'''
idx = idx.replace('  <!-- TESTIMONIALS -->', revolution_html)

# Add Newsletter CTA before the Footer
cta_html = '''
  <!-- NEWSLETTER CTA -->
  <section style="padding: 100px 40px; background: var(--bg-ink); text-align: center; border-top: 1px solid var(--border-color);">
    <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 16px;">Want 10% off?</h2>
    <p style="font-size: 1.1rem; color: var(--color-text-muted); margin-bottom: 30px;">Join the Squeeze Club for exclusive discounts and early flavor drops.</p>
    <a href="newsletter.html" class="btn" style="background: var(--color-coral); color: #fff; text-decoration: none; padding: 16px 40px; border-radius: 50px; font-weight: 600; font-size: 1.1rem; display: inline-block; transition: transform 0.2s;">Subscribe Now</a>
  </section>

  <!-- FOOTER -->'''
idx = idx.replace('  <!-- FOOTER -->', cta_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# 3. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    abt = f.read()

core_values = '''
      <p style="color:var(--color-text-muted);font-size:1.15rem;line-height:1.7;margin-bottom:30px;">
        Every cap we design is engineered to reduce single-use plastic while maximizing health benefits. We source only the highest quality real fruit extracts, and we never use artificial sweeteners or colors.
      </p>

      <!-- CORE VALUES GRID -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; margin-top: 60px; text-align: center;">
        <div style="padding: 30px; background: rgba(24,58,29,0.03); border-radius: 16px;">
          <i data-lucide="droplet" style="width: 32px; height: 32px; margin-bottom: 16px; color: var(--color-coral);"></i>
          <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 10px;">Real Ingredients</h4>
          <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.5;">Made with natural fruit extracts and zero artificial junk. Just pure, refreshing flavor.</p>
        </div>
        <div style="padding: 30px; background: rgba(24,58,29,0.03); border-radius: 16px;">
          <i data-lucide="leaf" style="width: 32px; height: 32px; margin-bottom: 16px; color: var(--color-coral);"></i>
          <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 10px;">Eco-Conscious</h4>
          <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.5;">By reusing your own bottle, you help keep thousands of plastic bottles out of our oceans.</p>
        </div>
        <div style="padding: 30px; background: rgba(24,58,29,0.03); border-radius: 16px;">
          <i data-lucide="map-pin" style="width: 32px; height: 32px; margin-bottom: 16px; color: var(--color-coral);"></i>
          <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 10px;">Made in India</h4>
          <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.5;">Proudly developed and manufactured locally, supporting our community and economy.</p>
        </div>
      </div>
'''
abt = abt.replace('<p style="color:var(--color-text-muted);font-size:1.15rem;line-height:1.7;margin-bottom:30px;">', core_values)
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(abt)


# 4. Update how-it-works.html
with open('how-it-works.html', 'r', encoding='utf-8') as f:
    hiw = f.read()

pro_tips = '''
  </section>

  <!-- PRO TIPS -->
  <section style="padding: 80px 40px; background: var(--bg-surface); border-top: 1px solid rgba(24,58,29,0.05);">
    <div style="max-width: 900px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 40px;">Pro Hydration Tips</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; text-align: left;">
        <div>
          <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;"><i data-lucide="thermometer-snowflake" style="width: 20px; color: var(--color-coral);"></i> Keep It Cold</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem;">Cap Squeeze flavors burst the best when mixed with ice-cold water. Drop a few ice cubes in your bottle before twisting on the cap.</p>
        </div>
        <div>
          <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;"><i data-lucide="sliders-horizontal" style="width: 20px; color: var(--color-coral);"></i> Adjust Your Squeeze</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem;">You control the intensity! Give it a gentle squeeze for a subtle hint of fruit, or a firm press for a bold, punchy flavor explosion.</p>
        </div>
        <div>
          <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;"><i data-lucide="refresh-cw" style="width: 20px; color: var(--color-coral);"></i> Rinse & Repeat</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem;">Our caps are designed to last for up to 3 refills of a standard 500ml bottle. When empty, recycle the cap and grab a new flavor!</p>
        </div>
      </div>
    </div>
'''
hiw = hiw.replace('  </section>\n\n  <!-- FOOTER -->', pro_tips + '\n  </section>\n\n  <!-- FOOTER -->')
with open('how-it-works.html', 'w', encoding='utf-8') as f:
    f.write(hiw)

# 5. Update flavors.html
with open('flavors.html', 'r', encoding='utf-8') as f:
    flv = f.read()

ingredient_spotlight = '''
  <section class="page-hero" style="padding-bottom: 20px;">
    <p class="page-hero-eyebrow">Our Flavors</p>
    <h1>Find your <span class="gradient-text">favorite.</span></h1>
    <p style="max-width: 600px; margin: 20px auto 0; color: var(--color-text-muted); font-size: 1.1rem; line-height: 1.6;">
      Every Cap Squeeze is crafted with real fruit extracts, essential electrolytes, and absolutely zero sugar. Pure, minimalist hydration.
    </p>
  </section>
'''
flv = flv.replace('''  <section class="page-hero">
    <p class="page-hero-eyebrow">Our Flavors</p>
    <h1>Find your <span class="gradient-text">favorite.</span></h1>
  </section>''', ingredient_spotlight)
with open('flavors.html', 'w', encoding='utf-8') as f:
    f.write(flv)

# 6. Update main.js for newsletter form
with open('js/main.js', 'a', encoding='utf-8') as f:
    f.write('''\n\n// Newsletter Form Handler
document.addEventListener('DOMContentLoaded', () => {
  const newsletterForm = document.getElementById('newsletter-form');
  if(newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      newsletterForm.style.display = 'none';
      document.getElementById('newsletter-success').style.display = 'block';
    });
  }
});\n''')

print("Content expansion applied successfully!")
