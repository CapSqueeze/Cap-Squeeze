import re

with open('flavors.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to find the <div class="pfc-price"... up to </button>
# and replace it with our new structure.

def replacer(match):
    full_match = match.group(0)
    
    # Extract the main price
    price_match = re.search(r'Rs\. (\d+)', full_match)
    if not price_match:
        return full_match
        
    base_price = int(price_match.group(1))
    sub_price = int(base_price * 0.85) # 15% off
    
    # Extract the button name
    name_match = re.search(r'data-name="(.*?)"', full_match)
    prod_name = name_match.group(1) if name_match else 'Product'
    
    # Generate a unique ID for this product
    prod_id = re.sub(r'[^a-zA-Z0-9]', '', prod_name).lower()
    
    html = f'''
          <div class="subs-toggle-container" id="subs-container-{prod_id}">
            <label class="subs-option active" onclick="updateSubs('{prod_id}', 'onetime', {base_price}, {sub_price})">
              <input type="radio" name="subs_type_{prod_id}" value="onetime" class="subs-radio" checked>
              <div class="subs-details">
                <div class="subs-title">One-time purchase <span style="font-weight:800;">Rs. {base_price}</span></div>
              </div>
            </label>
            <label class="subs-option" onclick="updateSubs('{prod_id}', 'subscribe', {base_price}, {sub_price})">
              <input type="radio" name="subs_type_{prod_id}" value="subscribe" class="subs-radio">
              <div class="subs-details">
                <div class="subs-title">Subscribe & Save <span class="subs-badge">15% OFF</span></div>
                <div class="subs-desc" style="color:var(--color-coral); font-weight:600; margin-top:6px;">Rs. {sub_price} / delivery</div>
                <select class="subs-frequency-select" style="margin-top:12px;">
                  <option>Deliver Every 1 Week</option>
                  <option>Deliver Every 2 Weeks</option>
                  <option>Deliver Every 1 Month</option>
                </select>
              </div>
            </label>
          </div>
          
          <button id="atc-btn-{prod_id}" class="pfc-atc" data-name="{prod_name}" data-price="{base_price}" style="width:100%; padding: 14px; background: var(--color-text-main); color: var(--bg-ink); border: none; border-radius: 8px; font-weight: 700; font-size: 1rem; cursor: pointer; transition: background 0.2s; margin-bottom: 20px;">Add to Cart - Rs. {base_price}</button>
'''
    return html

# Find everything from <div class="pfc-price" to </button>
pattern = re.compile(r'<div class="pfc-price".*?</button>', re.DOTALL)
new_content = re.sub(pattern, replacer, content)

# Add the JS script right before </body>
js_script = '''
  <script>
    function updateSubs(prodId, type, basePrice, subPrice) {
      const container = document.getElementById('subs-container-' + prodId);
      const options = container.querySelectorAll('.subs-option');
      const btn = document.getElementById('atc-btn-' + prodId);
      
      options.forEach(opt => opt.classList.remove('active'));
      
      if (type === 'onetime') {
        options[0].classList.add('active');
        options[0].querySelector('input').checked = true;
        btn.innerHTML = 'Add to Cart - Rs. ' + basePrice;
        btn.setAttribute('data-price', basePrice);
      } else {
        options[1].classList.add('active');
        options[1].querySelector('input').checked = true;
        btn.innerHTML = 'Subscribe Now - Rs. ' + subPrice;
        btn.setAttribute('data-price', subPrice);
      }
    }
  </script>
</body>'''

new_content = new_content.replace('</body>', js_script)

with open('flavors.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated flavors.html with subscription toggles.")
