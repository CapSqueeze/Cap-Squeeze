import re

html_to_inject = '''
  <!-- 12 FLAVORS SECTION -->
  <section class="content-section" style="padding-top: 20px;">
    <div style="max-width:1200px;margin:0 auto;">
      <h2 style="font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 40px; color: var(--color-text-main); font-family: 'Space Grotesk', sans-serif;">Meet Our 12 Flavors</h2>
      <div class="flavors-list-grid">
        <!-- Flavor 1 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍋</div>
          <h4 class="flavor-name">Lemon Zest</h4>
          <p class="flavor-profile">Bright, citrusy, and deeply refreshing.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 2 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍓</div>
          <h4 class="flavor-name">Strawberry Burst</h4>
          <p class="flavor-profile">Sweet, juicy, summer berry goodness.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 3 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍉</div>
          <h4 class="flavor-name">Wild Watermelon</h4>
          <p class="flavor-profile">Crisp and hydrating, perfect for hot days.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 4 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🌿</div>
          <h4 class="flavor-name">Minty Fresh</h4>
          <p class="flavor-profile">Cool, botanical, and invigorating.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 5 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🥭</div>
          <h4 class="flavor-name">Mango Tango</h4>
          <p class="flavor-profile">Tropical, luscious, and naturally sweet.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 6 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍏</div>
          <h4 class="flavor-name">Green Apple Tart</h4>
          <p class="flavor-profile">A crisp, sour bite that wakes you up.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 7 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍑</div>
          <h4 class="flavor-name">Peach Paradise</h4>
          <p class="flavor-profile">Soft, floral, and delicately fruity.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 8 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🫐</div>
          <h4 class="flavor-name">Blueberry Splash</h4>
          <p class="flavor-profile">Deep, rich, and loaded with antioxidants.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 9 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍊</div>
          <h4 class="flavor-name">Citrus Grapefruit</h4>
          <p class="flavor-profile">Zesty, mildly bitter, incredibly thirst-quenching.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 10 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🥝</div>
          <h4 class="flavor-name">Kiwi Melon</h4>
          <p class="flavor-profile">A unique blend of tangy kiwi and smooth melon.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 11 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍒</div>
          <h4 class="flavor-name">Raspberry Lemonade</h4>
          <p class="flavor-profile">The ultimate sweet and tart combination.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
        <!-- Flavor 12 -->
        <div class="flavor-mini-card">
          <div class="flavor-emoji">🍍</div>
          <h4 class="flavor-name">Coconut Pineapple</h4>
          <p class="flavor-profile">A mini vacation in a bottle.</p>
          <a href="#" class="flavor-add-btn">Add +</a>
        </div>
      </div>
    </div>
  </section>

'''

with open('flavors.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject right before NUTRITION SECTION
html = html.replace('<!-- NUTRITION SECTION -->', html_to_inject + '<!-- NUTRITION SECTION -->')

with open('flavors.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("flavors.html updated")

css_to_inject = '''
/* 12 Flavors Grid */
.flavors-list-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.flavor-mini-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  display: flex;
  flex-direction: column;
}

.flavor-mini-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(24, 58, 29, 0.08);
}

.flavor-emoji {
  font-size: 3rem;
  margin-bottom: 12px;
}

.flavor-name {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--color-text-main);
  margin-bottom: 8px;
  font-family: 'Space Grotesk', sans-serif;
}

.flavor-profile {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  line-height: 1.4;
  margin-bottom: 20px;
  flex-grow: 1;
}

.flavor-add-btn {
  display: inline-block;
  padding: 8px 16px;
  background: transparent;
  color: var(--color-text-main);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  font-weight: 700;
  font-size: 0.9rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.flavor-add-btn:hover {
  background: var(--color-coral);
  color: #fff;
  border-color: var(--color-coral);
}

@media (max-width: 900px) {
  .flavors-list-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 600px) {
  .flavors-list-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 400px) {
  .flavors-list-grid {
    grid-template-columns: 1fr;
  }
}
'''

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_inject)
print("style.css updated")

