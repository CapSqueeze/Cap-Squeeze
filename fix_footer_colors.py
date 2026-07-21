import os
import re

footer_replacement = '''<!-- ========== FOOTER ========== -->
  <footer class="site-footer">
    <div class="footer-inner">
      <!-- COLUMN 1: Brand & Contact -->
      <div class="footer-col footer-col--brand">
        <a href="index.html" class="footer-logo" style="display:flex; align-items:center; margin-bottom:15px; text-decoration:none;">
          <img src="images/logo.png" alt="Cap Squeeze" style="height:45px; margin-right:12px;">
          <span style="font-size:1.5rem; font-weight:800; color:var(--color-text-main);">Cap Squeeze.</span>
        </a>
        <p style="font-size:.9rem;opacity:.85;margin-bottom:16px;line-height:1.6; color:var(--color-text-muted);">Cap Squeeze is India\\'s first flavoured bottle cap. Turn any standard water bottle into a delicious, zero-sugar, vitamin-enhanced drink instantly.</p>
        
        <div class="footer-contact-info" style="margin-top: 25px; margin-bottom: 25px;">
          <h4 style="font-size: 1.1rem; margin-bottom: 15px; font-weight: 700; text-transform: uppercase; color: var(--color-text-main);">Contact Info</h4>
          <div class="footer-contact-item" style="color:var(--color-text-muted); margin-bottom: 10px; line-height:1.6;"><span style="color:var(--color-coral); font-weight:600; margin-right:6px;">Address:</span>71 Pennington Lane Vernon Rockville, CT 06066.</div>
          <div class="footer-contact-item" style="color:var(--color-text-muted); margin-bottom: 10px; line-height:1.6;"><span style="color:var(--color-coral); font-weight:600; margin-right:6px;">Phone:</span>0123-456-789</div>
          <div class="footer-contact-item" style="color:var(--color-text-muted); margin-bottom: 10px; line-height:1.6;"><span style="color:var(--color-coral); font-weight:600; margin-right:6px;">E-mail:</span>Demo@Yourstore.Com</div>
        </div>

        <div class="footer-social-circles">
          <h4 style="font-size: 1.1rem; margin-bottom: 15px; font-weight: 700; text-transform: uppercase; color: var(--color-text-main);">Follow Us</h4>
          <div class="social-circle-list">
            <a href="#" class="social-circle social-fb"><i data-lucide="facebook" style="width:18px;height:18px"></i></a>
            <a href="#" class="social-circle social-tw"><i data-lucide="twitter" style="width:18px;height:18px"></i></a>
            <a href="#" class="social-circle social-gp"><span style="font-weight:bold;font-family:serif;">G+</span></a>
            <a href="#" class="social-circle social-ig"><i data-lucide="instagram" style="width:18px;height:18px"></i></a>
            <a href="#" class="social-circle social-yt"><i data-lucide="youtube" style="width:18px;height:18px"></i></a>
          </div>
        </div>
      </div>

      <!-- COLUMN 2: Links (Consolidated) -->
      <div class="footer-col" style="margin-top:20px;">
        <h4 style="font-size: 1.1rem; margin-bottom: 20px; font-weight: 700; text-transform: uppercase; color: var(--color-text-main);">Shop & Info</h4>
        <ul style="list-style:none; padding:0; margin:0;">
          <li style="margin-bottom:12px;"><a href="index.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Home</a></li>
          <li style="margin-bottom:12px;"><a href="how-it-works.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">How It Works</a></li>
          <li style="margin-bottom:12px;"><a href="flavors.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Shop Flavors</a></li>
          <li style="margin-bottom:12px;"><a href="about.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">About Us</a></li>
          <li style="margin-bottom:12px;"><a href="faq.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">FAQ</a></li>
          <li style="margin-bottom:12px;"><a href="contact.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Customer Support</a></li>
        </ul>
      </div>

      <!-- COLUMN 3: Links (My Choice & Policies) -->
      <div class="footer-col" style="margin-top:20px;">
        <h4 style="font-size: 1.1rem; margin-bottom: 20px; font-weight: 700; text-transform: uppercase; color: var(--color-text-main);">My Choice & Legal</h4>
        <ul style="list-style:none; padding:0; margin:0;">
          <li style="margin-bottom:12px;"><a href="flavors.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Favorites</a></li>
          <li style="margin-bottom:12px;"><a href="dashboard.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">My Orders</a></li>
          <li style="margin-bottom:12px;"><a href="dashboard.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Track Order</a></li>
          <li style="margin-bottom:12px;"><a href="flavors.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Subscriptions</a></li>
          <li style="margin-bottom:12px;"><a href="shipping.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Shipping Info</a></li>
          <li style="margin-bottom:12px;"><a href="returns.html" style="color:var(--color-text-muted); text-decoration:none; transition:color 0.2s;">Returns Policy</a></li>
        </ul>
      </div>

      <!-- COLUMN 4: Newsletter & Payment -->
      <div class="footer-col" style="margin-top:20px;">
        <div class="footer-newsletter-widget">
          <h4 style="font-size: 1.1rem; margin-bottom: 15px; font-weight: 700; text-transform: uppercase; color: var(--color-text-main);">Subscribe Newsletter</h4>
          <p style="color:var(--color-text-muted);">Subscribe to our newsletters now and stay up to date with new collections and exclusive offers.</p>
          <form class="footer-newsletter-form" onsubmit="return false;" style="margin-top:20px; border-bottom: 1px solid var(--border-color);">
            <input type="email" placeholder="Your email address" style="font-size:0.9rem; color:var(--color-text-main);">
            <button type="submit" class="footer-newsletter-btn" aria-label="Subscribe">
              <i data-lucide="send" style="width:18px;height:18px; transform:rotate(45deg); margin-left:-3px; margin-bottom:-3px;"></i>
            </button>
          </form>
        </div>

        <div class="footer-payment" style="margin-top:40px;">
          <h4 style="font-size: 1.1rem; margin-bottom: 15px; font-weight: 700; text-transform: uppercase; color: var(--color-text-main);">Payment</h4>
          <div class="payment-icons">
            <span class="payment-icon" style="background:#2776b3; color:#fff; font-weight:800; font-size:10px; display:flex; align-items:center;">AMEX</span>
            <span class="payment-icon" style="background:#1a1f71; color:#fff; font-weight:800; font-size:12px; font-style:italic; display:flex; align-items:center;">VISA</span>
            <span class="payment-icon" style="background:#003087; color:#009cde; font-weight:800; font-size:11px; font-style:italic; display:flex; align-items:center;">PayPal</span>
            <span class="payment-icon" style="background:#ff6000; color:#fff; font-weight:800; font-size:10px; display:flex; align-items:center; border-radius:12px;">Discover</span>
            <span class="payment-icon" style="background:#eb001b; color:#f79e1b; font-weight:800; font-size:10px; display:flex; align-items:center; border-radius:50%; width:24px; justify-content:center;">MC</span>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-divider" style="margin:40px 0 20px 0; border-top:1px solid var(--border-color);"></div>

    <div class="footer-copyright" style="text-align:center; padding-bottom:20px;">
      <p style="color:var(--color-text-muted); font-size:0.9rem;">&copy; 2026 Cap Squeeze. All rights reserved. Made with <i data-lucide="heart" class="icon-inline" style="color:var(--color-coral); width:14px;"></i> in India <i data-lucide="map-pin" class="icon-inline" style="color:var(--color-coral); width:14px;"></i></p>
    </div>
  </footer>'''

files = [f for f in os.listdir('.') if f.endswith('.html')]
pattern = re.compile(r'<!-- ========== FOOTER ========== -->.*?</footer>', re.DOTALL)

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(pattern, footer_replacement, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Updated footer in {f}")
