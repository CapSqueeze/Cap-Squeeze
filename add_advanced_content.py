import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

why_choose_us = '''
  <!-- WHY CHOOSE US -->
  <section style="padding: 100px 40px; background: var(--bg-card); text-align: center; border-bottom: 1px solid var(--border-color);">
    <div style="max-width: 1000px; margin: 0 auto;">
      <p style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 16px; opacity: 0.7;">The Cap Squeeze Advantage</p>
      <h2 style="font-size: 2.8rem; font-weight: 800; margin-bottom: 60px; line-height: 1.2;">Designed for <span class="gradient-text">Life in Motion.</span></h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 40px;">
        <div>
          <i data-lucide="zap" style="width: 40px; height: 40px; margin-bottom: 20px; color: var(--color-coral);"></i>
          <h4 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 12px;">Zero Sugar, Zero Calories</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem;">All the sweet, vibrant flavor you crave without any of the dietary drawbacks. Completely guilt-free hydration.</p>
        </div>
        <div>
          <i data-lucide="pocket" style="width: 40px; height: 40px; margin-bottom: 20px; color: var(--color-coral);"></i>
          <h4 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 12px;">Pocket-Sized Portability</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem;">Skip the heavy cans and bulky bottles. Slip a Cap Squeeze into your pocket or gym bag and flavor your water anywhere.</p>
        </div>
        <div>
          <i data-lucide="recycle" style="width: 40px; height: 40px; margin-bottom: 20px; color: var(--color-coral);"></i>
          <h4 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 12px;">100% Recyclable</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem;">By reusing your existing water bottle and concentrating our flavors, we drastically reduce single-use plastic waste.</p>
        </div>
        <div>
          <i data-lucide="droplet" style="width: 40px; height: 40px; margin-bottom: 20px; color: var(--color-coral);"></i>
          <h4 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 12px;">Essential Electrolytes</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem;">More than just flavor. Our caps are infused with a balanced blend of electrolytes to keep you optimally hydrated all day.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- TESTIMONIALS -->'''
idx = idx.replace('  <!-- TESTIMONIALS -->', why_choose_us)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# 2. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    abt = f.read()

founders_note = '''
      <!-- SUSTAINABILITY & FOUNDER -->
      <div style="margin-top: 80px; padding-top: 60px; border-top: 1px solid rgba(24,58,29,0.1); text-align: left;">
        <h3 style="font-size: 2rem; font-weight: 800; margin-bottom: 20px;">Our Sustainability Promise</h3>
        <p style="color:var(--color-text-muted);font-size:1.1rem;line-height:1.7;margin-bottom:40px;">
          The beverage industry is broken. Every day, millions of gallons of water are needlessly shipped around the world in heavy, single-use plastic bottles, generating a massive carbon footprint. We realized that if you already have the water, we just need to provide the flavor. Every Cap Squeeze used is one less plastic bottle in a landfill. By concentrating the flavor, we are cutting down on shipping weight, carbon emissions, and plastic waste. It's a small twist of a cap, but a massive step for our planet.
        </p>

        <div style="background: var(--bg-ink); padding: 40px; border-radius: 16px; border: 1px solid var(--border-color);">
          <h3 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 16px;">A Note from the Team</h3>
          <p style="color:var(--color-text-muted);font-size:1.05rem;line-height:1.7;margin-bottom:20px; font-style: italic;">
            "We started Cap Squeeze because we were bored of plain water and disgusted by the sugar in sodas and sports drinks. We wanted something healthy, sustainable, and genuinely delicious. Building this company in India has been a dream come true, and we are so grateful for the community of hydration enthusiasts we are building. Whether you're hitting the gym, studying for finals, or just trying to drink more water, we're here to make every sip better."
          </p>
          <p style="font-weight: 700; font-size: 1.1rem; margin: 0;">— The Cap Squeeze Founders</p>
        </div>
      </div>
'''
abt = abt.replace('<!-- CORE VALUES GRID -->', founders_note + '\n      <!-- CORE VALUES GRID -->')
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(abt)

# 3. Update how-it-works.html
with open('how-it-works.html', 'r', encoding='utf-8') as f:
    hiw = f.read()

science_compat = '''
  <!-- SCIENCE AND COMPATIBILITY -->
  <section style="padding: 100px 40px; background: var(--bg-card);">
    <div style="max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px;">
      
      <div>
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: rgba(24,58,29,0.05); display: flex; align-items: center; justify-content: center;">
            <i data-lucide="microscope" style="color: var(--color-coral);"></i>
          </div>
          <h3 style="font-size: 1.8rem; font-weight: 800; margin: 0;">The Science of the Cap</h3>
        </div>
        <p style="color: var(--color-text-muted); line-height: 1.7; font-size: 1.05rem; margin-bottom: 20px;">
          It looks simple, but inside every Cap Squeeze is a patented, precision-flow membrane. This micro-dosing technology ensures that the highly concentrated flavor syrup never leaks into your bag, but releases perfectly the moment you apply pressure to the bottle. 
        </p>
        <p style="color: var(--color-text-muted); line-height: 1.7; font-size: 1.05rem;">
          The internal mixing chamber instantly emulsifies the fruit extracts and electrolytes with your water, meaning no shaking or stirring is required. Just squeeze and drink.
        </p>
      </div>

      <div>
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
          <div style="width: 48px; height: 48px; border-radius: 50%; background: rgba(24,58,29,0.05); display: flex; align-items: center; justify-content: center;">
            <i data-lucide="settings-2" style="color: var(--color-coral);"></i>
          </div>
          <h3 style="font-size: 1.8rem; font-weight: 800; margin: 0;">Compatibility Guide</h3>
        </div>
        <p style="color: var(--color-text-muted); line-height: 1.7; font-size: 1.05rem; margin-bottom: 20px;">
          We designed Cap Squeeze to be the most versatile hydration tool on the market. The threading on our caps is engineered to the industry standard <strong>28mm PCO 1881</strong> specification. 
        </p>
        <p style="color: var(--color-text-muted); line-height: 1.7; font-size: 1.05rem;">
          This means it seamlessly fits 99% of all standard PET water and soda bottles worldwide. From Bisleri and Kinley to Aquafina and Dasani, your Cap Squeeze will lock on tight with a perfect, leak-proof seal every time.
        </p>
      </div>

    </div>
  </section>

  <!-- PRO TIPS -->'''
hiw = hiw.replace('  <!-- PRO TIPS -->', science_compat)
with open('how-it-works.html', 'w', encoding='utf-8') as f:
    f.write(hiw)

# 4. Update flavors.html
with open('flavors.html', 'r', encoding='utf-8') as f:
    flv = f.read()

flavor_profiles = '''
  <!-- FLAVOR PROFILES GUIDE -->
  <section style="padding: 60px 40px 20px 40px; background: var(--bg-ink); border-bottom: 1px solid rgba(24,58,29,0.05);">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h3 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 30px;">Find Your Perfect Pairing</h3>
      <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
        <div style="background: var(--bg-card); padding: 16px 24px; border-radius: 50px; border: 1px solid var(--border-color); font-size: 0.95rem; font-weight: 600;">
          <span style="color: #ff9800;">🌅 The Morning Boost:</span> Citrus & Orange
        </div>
        <div style="background: var(--bg-card); padding: 16px 24px; border-radius: 50px; border: 1px solid var(--border-color); font-size: 0.95rem; font-weight: 600;">
          <span style="color: #5c6bc0;">💪 Post-Workout Recovery:</span> Mixed Berry & Watermelon
        </div>
        <div style="background: var(--bg-card); padding: 16px 24px; border-radius: 50px; border: 1px solid var(--border-color); font-size: 0.95rem; font-weight: 600;">
          <span style="color: #8bc34a;">🌿 Afternoon Refresh:</span> Kiwi & Mint
        </div>
      </div>
    </div>
  </section>

  <div class="store-grid">'''
flv = flv.replace('  <div class="store-grid">', flavor_profiles)
with open('flavors.html', 'w', encoding='utf-8') as f:
    f.write(flv)


# 5. Update contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    cnt = f.read()

contact_guarantee = '''
        <div style="margin-top: 60px; background: rgba(24,58,29,0.03); padding: 30px; border-radius: 12px; border: 1px solid var(--border-color);">
          <h4 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 10px;">Our Response Guarantee</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem; margin-bottom: 20px;">We know there is nothing worse than waiting days for customer support. Our dedicated team guarantees a personalized response to all inquiries within <strong>24 business hours</strong>.</p>
          
          <h4 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 10px;">Wholesale & Gym Partnerships</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6; font-size: 0.95rem; margin-bottom: 0;">Looking to stock Cap Squeeze in your gym, office, or retail store? We offer competitive wholesale pricing for bulk orders. Select "Wholesale/B2B" in the contact form to connect with our partnerships team.</p>
        </div>
'''
cnt = cnt.replace('        <form class="contact-form">', contact_guarantee + '\n        <form class="contact-form">')
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(cnt)

print("Advanced content expansion applied successfully!")
