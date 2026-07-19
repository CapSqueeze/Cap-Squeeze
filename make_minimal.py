import os
import re

html_to_inject = '''  <!-- ========== HOW IT WORKS ========== -->
  <section class="content-section" style="padding:100px 20px; text-align:center;">
    <h2 class="section-heading" style="margin-bottom:60px;">How It Works</h2>
    <div style="display:flex; justify-content:center; gap:60px; flex-wrap:wrap; max-width:1000px; margin:0 auto;">
      <div style="flex:1; min-width:220px; text-align:center;">
        <div style="margin-bottom:25px;"><i data-lucide="droplet" class="icon-inline" style="width:4rem; height:4rem; stroke-width:1.5; color:#183a1d;"></i></div>
        <h3 style="font-size:1.4rem; color:#183a1d; margin-bottom:12px; font-weight:700;">1. Fill</h3>
        <p style="color:#666; line-height:1.6; font-size:1.05rem;">Fill your standard reusable bottle with regular water.</p>
      </div>
      <div style="flex:1; min-width:220px; text-align:center;">
        <div style="margin-bottom:25px;"><i data-lucide="refresh-cw" class="icon-inline" style="width:4rem; height:4rem; stroke-width:1.5; color:#183a1d;"></i></div>
        <h3 style="font-size:1.4rem; color:#183a1d; margin-bottom:12px; font-weight:700;">2. Twist</h3>
        <p style="color:#666; line-height:1.6; font-size:1.05rem;">Attach your Cap Squeeze flavor cap tightly onto the bottle.</p>
      </div>
      <div style="flex:1; min-width:220px; text-align:center;">
        <div style="margin-bottom:25px;"><i data-lucide="zap" class="icon-inline" style="width:4rem; height:4rem; stroke-width:1.5; color:#183a1d;"></i></div>
        <h3 style="font-size:1.4rem; color:#183a1d; margin-bottom:12px; font-weight:700;">3. Squeeze</h3>
        <p style="color:#666; line-height:1.6; font-size:1.05rem;">Squeeze to release the delicious, zero-sugar flavor burst!</p>
      </div>
    </div>
  </section>

  <!-- ========== WHY CHOOSE US ========== -->
  <section class="content-section" style="padding:100px 20px; text-align:center; border-top:1px solid #f0f0f0;">
    <h2 class="section-heading" style="margin-bottom:60px;">Why Cap Squeeze?</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:60px; max-width:1100px; margin:0 auto;">
      <div style="text-align:center;">
        <div style="margin-bottom:25px;"><i data-lucide="ban" class="icon-inline" style="width:3.5rem; height:3.5rem; stroke-width:1.5; color:#e3000b;"></i></div>
        <h3 style="color:#183a1d; font-size:1.25rem; margin-bottom:12px; font-weight:600;">Zero Sugar</h3>
        <p style="color:#777; line-height:1.6; font-size:0.95rem;">Enjoy sweet, refreshing hydration without any of the guilt.</p>
      </div>
      <div style="text-align:center;">
        <div style="margin-bottom:25px;"><i data-lucide="recycle" class="icon-inline" style="width:3.5rem; height:3.5rem; stroke-width:1.5; color:#e3000b;"></i></div>
        <h3 style="color:#183a1d; font-size:1.25rem; margin-bottom:12px; font-weight:600;">Eco-Friendly</h3>
        <p style="color:#777; line-height:1.6; font-size:0.95rem;">Stop buying single-use plastic bottles. Reuse yours!</p>
      </div>
      <div style="text-align:center;">
        <div style="margin-bottom:25px;"><i data-lucide="leaf" class="icon-inline" style="width:3.5rem; height:3.5rem; stroke-width:1.5; color:#e3000b;"></i></div>
        <h3 style="color:#183a1d; font-size:1.25rem; margin-bottom:12px; font-weight:600;">100% Natural</h3>
        <p style="color:#777; line-height:1.6; font-size:0.95rem;">Made from real fruit extracts and no artificial colors.</p>
      </div>
      <div style="text-align:center;">
        <div style="margin-bottom:25px;"><i data-lucide="zap" class="icon-inline" style="width:3.5rem; height:3.5rem; stroke-width:1.5; color:#e3000b;"></i></div>
        <h3 style="color:#183a1d; font-size:1.25rem; margin-bottom:12px; font-weight:600;">Electrolytes</h3>
        <p style="color:#777; line-height:1.6; font-size:0.95rem;">Stay charged all day long with our essential blend.</p>
      </div>
    </div>
  </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Regex to find everything from <!-- ========== HOW IT WORKS ========== --> to just before <!-- ========== CUSTOMER REVIEWS ========== -->
pattern = r'  <!-- ========== HOW IT WORKS ========== -->.*?  <!-- ========== CUSTOMER REVIEWS ========== -->'
new_content = re.sub(pattern, html_to_inject + "\\n\\n  <!-- ========== CUSTOMER REVIEWS ========== -->", content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Minimal design applied successfully!")
