# -*- coding: utf-8 -*-
import re

with open('flavors.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Products Grid -->'
end_marker = '<!-- NUTRITION SECTION -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_grid = '''<!-- Products Grid -->
      <div class="products-grid">

        <!-- PRODUCT 1 -->
        <div class="product-full-card" style="position:relative; overflow:hidden; border: 1px solid var(--border-color); border-radius: 16px; padding: 20px; background: var(--bg-card); transition: transform 0.3s ease, box-shadow 0.3s ease;">
          <span class="pfc-badge" style="background: var(--color-coral); color: #fff; padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; display: inline-block; margin-bottom: 15px;">&#11088; Best Seller</span>
          <div class="pfc-img" style="text-align:center; padding: 20px 0;"><img src="images/products/caps-group.png" alt="Starter Kit" style="max-width:80%; margin:0 auto; transition: transform 0.3s ease;"></div>
          <div style="display:flex; gap:6px; margin-bottom: 12px; flex-wrap: wrap;">
             <span style="background: rgba(240, 160, 75, 0.15); color: var(--color-coral); padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">Sweet & Tangy</span>
             <span style="background: rgba(246, 196, 83, 0.15); color: #b88a10; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">Refreshing</span>
          </div>
          <p class="pfc-title" style="font-size: 1.3rem; font-weight: 800; color: var(--color-text-main); margin-bottom: 6px;">Cap Squeeze Starter Kit</p>
          <div style="display:flex; align-items:center; gap: 4px; margin-bottom: 12px; font-size: 0.85rem; color: var(--color-text-muted);">
            <span style="color: #f6c453;">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <span>4.9 (2.1k Reviews)</span>
          </div>
          <p class="pfc-desc" style="font-size: 0.9rem; color: var(--color-text-muted); line-height: 1.5; margin-bottom: 20px;">Everything you need to start. 1 premium Cap Squeeze flavour cap + 6 natural zero-sugar flavour pods.</p>
          
          <select class="pfc-select" style="width:100%; padding: 12px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface); color: var(--color-text-main); margin-bottom: 20px; font-family: inherit;">
            <option>Variety Pack (Best Mix)</option>
            <option>Citrus Pack</option>
          </select>
          
          <div class="pfc-price" style="display:flex; align-items:baseline; gap: 10px; margin-bottom: 20px;">
            <span class="pfc-price-main" style="font-size: 1.6rem; font-weight: 800; color: var(--color-text-main);">Rs. 1599</span>
            <span class="pfc-price-old" style="font-size: 1rem; color: var(--color-text-muted); text-decoration: line-through;">Rs. 1799</span>
          </div>
          <button class="pfc-atc" data-name="Cap Squeeze Starter Kit" data-price="1599" style="width:100%; padding: 14px; background: var(--color-text-main); color: var(--bg-ink); border: none; border-radius: 8px; font-weight: 700; font-size: 1rem; cursor: pointer; transition: background 0.2s;">Add to Cart</button>
        </div>

        <!-- PRODUCT 2 -->
        <div class="product-full-card" style="position:relative; overflow:hidden; border: 1px solid var(--border-color); border-radius: 16px; padding: 20px; background: var(--bg-card); transition: transform 0.3s ease, box-shadow 0.3s ease;">
          <span class="pfc-badge" style="background: var(--color-pink); color: #183a1d; padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; display: inline-block; margin-bottom: 15px;">&#128176; Best Value</span>
          <div class="pfc-img" style="text-align:center; padding: 20px 0;"><img src="images/products/caps-group.png" alt="Refill Mega-Pack" style="max-width:80%; margin:0 auto; transition: transform 0.3s ease;"></div>
          <div style="display:flex; gap:6px; margin-bottom: 12px; flex-wrap: wrap;">
             <span style="background: rgba(240, 160, 75, 0.15); color: var(--color-coral); padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">Customizable</span>
          </div>
          <p class="pfc-title" style="font-size: 1.3rem; font-weight: 800; color: var(--color-text-main); margin-bottom: 6px;">Refill Mega-Pack (12)</p>
          <div style="display:flex; align-items:center; gap: 4px; margin-bottom: 12px; font-size: 0.85rem; color: var(--color-text-muted);">
            <span style="color: #f6c453;">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <span>4.8 (850 Reviews)</span>
          </div>
          <p class="pfc-desc" style="font-size: 0.9rem; color: var(--color-text-muted); line-height: 1.5; margin-bottom: 20px;">Stock up and save big. 12 recyclable natural flavour pods - no cap included. Perfect for regular customers.</p>
          
          <select class="pfc-select" style="width:100%; padding: 12px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface); color: var(--color-text-main); margin-bottom: 20px; font-family: inherit;">
            <option>All 12 Flavors Mix</option>
            <option>Berry Explosion Mix</option>
          </select>
          
          <div class="pfc-price" style="display:flex; align-items:baseline; gap: 10px; margin-bottom: 20px;">
            <span class="pfc-price-main" style="font-size: 1.6rem; font-weight: 800; color: var(--color-text-main);">Rs. 1799</span>
            <span class="pfc-price-old" style="font-size: 1rem; color: var(--color-text-muted); text-decoration: line-through;">Rs. 1999</span>
          </div>
          <button class="pfc-atc" data-name="Refill Mega-Pack (12 Pods)" data-price="1799" style="width:100%; padding: 14px; background: var(--color-text-main); color: var(--bg-ink); border: none; border-radius: 8px; font-weight: 700; font-size: 1rem; cursor: pointer; transition: background 0.2s;">Add to Cart</button>
        </div>

        <!-- PRODUCT 3 -->
        <div class="product-full-card" style="position:relative; overflow:hidden; border: 1px solid var(--border-color); border-radius: 16px; padding: 20px; background: var(--bg-card); transition: transform 0.3s ease, box-shadow 0.3s ease;">
          <span class="pfc-badge" style="background: var(--bg-surface); color: var(--color-text-main); padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; display: inline-block; margin-bottom: 15px; border: 1px solid var(--border-color);">🍋 Pick Your Fave</span>
          <div class="pfc-img" style="text-align:center; padding: 20px 0;"><img src="images/products/cap-lime.png" alt="Single Flavor 6-Pack" style="max-width:80%; margin:0 auto; transition: transform 0.3s ease;"></div>
          <div style="display:flex; gap:6px; margin-bottom: 12px; flex-wrap: wrap;">
             <span style="background: rgba(139, 195, 74, 0.15); color: #558b2f; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">Zesty</span>
             <span style="background: rgba(3, 169, 244, 0.15); color: #0277bd; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">Hydrating</span>
          </div>
          <p class="pfc-title" style="font-size: 1.3rem; font-weight: 800; color: var(--color-text-main); margin-bottom: 6px;">Single Flavor 6-Pack</p>
          <div style="display:flex; align-items:center; gap: 4px; margin-bottom: 12px; font-size: 0.85rem; color: var(--color-text-muted);">
            <span style="color: #f6c453;">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <span>4.7 (1.2k Reviews)</span>
          </div>
          <p class="pfc-desc" style="font-size: 0.9rem; color: var(--color-text-muted); line-height: 1.5; margin-bottom: 20px;">Found your go-to flavour? Get 6 of the same pod. Perfect for your daily routine hydration.</p>
          
          <select class="pfc-select" style="width:100%; padding: 12px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface); color: var(--color-text-main); margin-bottom: 20px; font-family: inherit;">
            <option>Lemon Zest</option>
            <option>Strawberry Burst</option>
            <option>Wild Watermelon</option>
            <option>Minty Fresh</option>
          </select>
          
          <div class="pfc-price" style="display:flex; align-items:baseline; gap: 10px; margin-bottom: 20px;">
            <span class="pfc-price-main" style="font-size: 1.6rem; font-weight: 800; color: var(--color-text-main);">Rs. 1449</span>
            <span class="pfc-price-old" style="font-size: 1rem; color: var(--color-text-muted); text-decoration: line-through;">Rs. 1549</span>
          </div>
          <button class="pfc-atc" data-name="Single Flavor 6-Pack" data-price="1449" style="width:100%; padding: 14px; background: var(--color-text-main); color: var(--bg-ink); border: none; border-radius: 8px; font-weight: 700; font-size: 1rem; cursor: pointer; transition: background 0.2s;">Add to Cart</button>
        </div>

      </div>
    </div>
  </section>

  <style>
    .product-full-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 30px rgba(24, 58, 29, 0.1);
    }
    .product-full-card:hover .pfc-img img {
      transform: scale(1.05);
    }
    .pfc-atc:hover {
      background: var(--color-coral) !important;
      color: #fff !important;
    }
  </style>

  <!-- NUTRITION SECTION -->'''
    
    content = content[:start_idx] + new_grid + content[end_idx + len('<!-- NUTRITION SECTION -->'):]
    with open('flavors.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated flavors.html')
else:
    print('Could not find markers in flavors.html')
