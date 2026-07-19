import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. MOJIBAKE REPLACEMENTS
replacements = {
    'ðŸ’›': '💛',
    'âœ…': '✅',
    'ðŸš«': '🚫',
    'ðŸ‡®ðŸ‡³': '🇮🇳',
    'ðŸ”’': '🔒',
    'ðŸ’¬': '💬',
    'â‚¹': '₹',
    'â€”': '—',
    'ðŸ †': '🏆',
    'ðŸ’°': '💰'
}

# 2. HOME PAGE INJECTION CONTENT
html_to_inject = '''  <!-- ========== HOW IT WORKS ========== -->
  <section class="content-section" style="background:#f4f9f4; padding:80px 20px; text-align:center;">
    <h2 class="section-heading">How It Works</h2>
    <div style="display:flex; justify-content:center; gap:40px; flex-wrap:wrap; max-width:1000px; margin:50px auto 0;">
      <div style="flex:1; min-width:250px;">
        <div style="font-size:3.5rem; margin-bottom:20px;">💧</div>
        <h3 style="font-size:1.5rem; color:#183a1d; margin-bottom:15px; font-weight:800;">1. Fill</h3>
        <p style="color:#555; line-height:1.6; font-size:1.1rem;">Fill up any standard reusable bottle with regular water.</p>
      </div>
      <div style="flex:1; min-width:250px;">
        <div style="font-size:3.5rem; margin-bottom:20px;">🔄</div>
        <h3 style="font-size:1.5rem; color:#183a1d; margin-bottom:15px; font-weight:800;">2. Twist</h3>
        <p style="color:#555; line-height:1.6; font-size:1.1rem;">Attach your Cap Squeeze flavor cap tightly onto the bottle.</p>
      </div>
      <div style="flex:1; min-width:250px;">
        <div style="font-size:3.5rem; margin-bottom:20px;">💥</div>
        <h3 style="font-size:1.5rem; color:#183a1d; margin-bottom:15px; font-weight:800;">3. Squeeze</h3>
        <p style="color:#555; line-height:1.6; font-size:1.1rem;">Squeeze to release the delicious, zero-sugar flavor burst!</p>
      </div>
    </div>
  </section>

  <!-- ========== WHY CHOOSE US ========== -->
  <section class="content-section" style="padding:80px 20px; text-align:center;">
    <h2 class="section-heading">Why Cap Squeeze?</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(250px, 1fr)); gap:30px; max-width:1200px; margin:50px auto 0;">
      <div style="background:#fff; padding:40px 30px; border-radius:20px; box-shadow:0 15px 40px rgba(0,0,0,0.06); border:1px solid #f0f0f0;">
        <div style="font-size:2.5rem; margin-bottom:15px;">🚫</div>
        <h3 style="color:#e3000b; font-size:1.4rem; margin-bottom:15px; font-weight:700;">Zero Sugar</h3>
        <p style="color:#666; line-height:1.6;">Enjoy sweet, refreshing hydration without any of the guilt.</p>
      </div>
      <div style="background:#fff; padding:40px 30px; border-radius:20px; box-shadow:0 15px 40px rgba(0,0,0,0.06); border:1px solid #f0f0f0;">
        <div style="font-size:2.5rem; margin-bottom:15px;">♻️</div>
        <h3 style="color:#e3000b; font-size:1.4rem; margin-bottom:15px; font-weight:700;">Eco-Friendly</h3>
        <p style="color:#666; line-height:1.6;">Stop buying single-use plastic bottles. Reuse yours!</p>
      </div>
      <div style="background:#fff; padding:40px 30px; border-radius:20px; box-shadow:0 15px 40px rgba(0,0,0,0.06); border:1px solid #f0f0f0;">
        <div style="font-size:2.5rem; margin-bottom:15px;">🍋</div>
        <h3 style="color:#e3000b; font-size:1.4rem; margin-bottom:15px; font-weight:700;">100% Natural</h3>
        <p style="color:#666; line-height:1.6;">Made from real fruit extracts and absolutely no artificial colors.</p>
      </div>
      <div style="background:#fff; padding:40px 30px; border-radius:20px; box-shadow:0 15px 40px rgba(0,0,0,0.06); border:1px solid #f0f0f0;">
        <div style="font-size:2.5rem; margin-bottom:15px;">⚡</div>
        <h3 style="color:#e3000b; font-size:1.4rem; margin-bottom:15px; font-weight:700;">Added Electrolytes</h3>
        <p style="color:#666; line-height:1.6;">Stay charged all day long with our essential electrolyte blend.</p>
      </div>
    </div>
  </section>

  <!-- ========== CUSTOMER REVIEWS ========== -->
  <section class="content-section" style="background:#183a1d; color:#fff; padding:80px 20px; text-align:center;">
    <h2 class="section-heading" style="color:#fff;">Loved by Hydrators</h2>
    <div style="display:flex; justify-content:center; gap:25px; flex-wrap:wrap; max-width:1200px; margin:50px auto 0;">
      <div style="background:rgba(255,255,255,0.05); padding:35px; border-radius:20px; flex:1; min-width:300px; text-align:left; backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.1);">
        <div style="color:#f1c40f; font-size:1.4rem; margin-bottom:15px;">★★★★★</div>
        <p style="font-style:italic; line-height:1.7; margin-bottom:20px; font-size:1.05rem;">"Finally, water isn't boring anymore! The Mango Fizz is my absolute favorite. It's so flavorful."</p>
        <strong style="color:#fff; font-size:1.1rem;">- Priya S.</strong>
      </div>
      <div style="background:rgba(255,255,255,0.05); padding:35px; border-radius:20px; flex:1; min-width:300px; text-align:left; backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.1);">
        <div style="color:#f1c40f; font-size:1.4rem; margin-bottom:15px;">★★★★★</div>
        <p style="font-style:italic; line-height:1.7; margin-bottom:20px; font-size:1.05rem;">"I've stopped buying plastic bottles completely. It's so much cheaper and tastes amazing."</p>
        <strong style="color:#fff; font-size:1.1rem;">- Rahul M.</strong>
      </div>
      <div style="background:rgba(255,255,255,0.05); padding:35px; border-radius:20px; flex:1; min-width:300px; text-align:left; backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.1);">
        <div style="color:#f1c40f; font-size:1.4rem; margin-bottom:15px;">★★★★★</div>
        <p style="font-style:italic; line-height:1.7; margin-bottom:20px; font-size:1.05rem;">"My kids actually want to drink water now. Best purchase ever for a healthy family."</p>
        <strong style="color:#fff; font-size:1.1rem;">- Anita K.</strong>
      </div>
    </div>
  </section>
'''

# 3. LOGO AND FAVICON INJECTION
old_logo = '<a href="index.html" class="site-logo">Cap Squeeze.</a>'
new_logo = '''<a href="index.html" class="site-logo" style="display:flex; align-items:center;">
        <img src="images/logo.png" alt="Cap Squeeze" style="height:40px; margin-right:10px;">
        Cap Squeeze.
      </a>'''

old_footer_logo = '<a href="index.html" class="footer-logo">Cap Squeeze.</a>'
new_footer_logo = '''<a href="index.html" class="footer-logo" style="display:flex; align-items:center; margin-bottom:15px;">
          <img src="images/logo.png" alt="Cap Squeeze" style="height:45px; margin-right:12px;">
          Cap Squeeze.
        </a>'''

favicon_tag = '  <link rel="icon" href="images/favicon.png" type="image/png">\\n'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply Mojibake Fixes
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Apply Logo & Favicon
    content = content.replace(old_logo, new_logo)
    content = content.replace(old_footer_logo, new_footer_logo)
    if 'favicon.png' not in content:
        content = content.replace('</head>', favicon_tag + '</head>')
        
    # Apply Home Page Injection (only to index.html)
    if file == 'index.html':
        injection_point = '  <!-- ========== NEWSLETTER BANNER ========== -->'
        content = content.replace(injection_point, html_to_inject + "\\n" + injection_point)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("All fixes applied successfully!")
