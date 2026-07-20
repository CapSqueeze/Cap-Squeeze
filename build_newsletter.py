import os

newsletter_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Newsletter — Cap Squeeze</title>
  
  <!-- Fonts & CSS -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=50506">
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    /* Newsletter Page Styles */
    .newsletter-hero {
      text-align: center;
      padding: 100px 20px 60px;
      max-width: 900px;
      margin: 0 auto;
    }
    
    .newsletter-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 1rem;
      border-radius: 50px;
      background-color: rgba(239, 83, 80, 0.1);
      color: var(--color-coral, #ef5350);
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 30px;
    }
    
    .pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: var(--color-coral, #ef5350);
      animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(239, 83, 80, 0.7); }
      70% { box-shadow: 0 0 0 10px rgba(239, 83, 80, 0); }
      100% { box-shadow: 0 0 0 0 rgba(239, 83, 80, 0); }
    }

    .newsletter-headline {
      font-size: 3.5rem;
      font-weight: 800;
      line-height: 1.1;
      color: #333;
      margin-bottom: 20px;
      font-family: 'Space Grotesk', sans-serif;
    }
    
    .newsletter-headline em {
      color: var(--color-coral, #ef5350);
      font-style: normal;
    }

    .newsletter-desc {
      font-size: 1.25rem;
      color: #666;
      max-width: 600px;
      margin: 0 auto 40px auto;
      line-height: 1.6;
    }

    .subscribe-form {
      display: flex;
      max-width: 500px;
      margin: 0 auto;
      background: #fff;
      border: 1px solid #ddd;
      border-radius: 30px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .subscribe-input {
      flex: 1;
      padding: 15px 25px;
      border: none;
      outline: none;
      font-size: 1rem;
    }
    
    .subscribe-btn {
      background: var(--color-coral, #ef5350);
      color: white;
      border: none;
      padding: 0 30px;
      font-weight: 600;
      cursor: pointer;
      font-family: 'Outfit', sans-serif;
      font-size: 1rem;
      transition: background 0.3s ease;
    }
    
    .subscribe-btn:hover {
      background: #d32f2f;
    }

    .stats-container {
      display: flex;
      gap: 3rem;
      justify-content: center;
      margin-top: 60px;
      padding-top: 40px;
      border-top: 1px solid #eee;
    }
    
    .stat-item {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    
    .stat-number {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.5rem;
      font-weight: 700;
      color: #333;
      line-height: 1;
    }
    
    .stat-label {
      font-size: 0.9rem;
      color: #777;
      margin-top: 8px;
    }

    /* Latest Editions Section */
    .latest-section {
      background-color: #f9fbfa;
      padding: 80px 20px;
    }
    
    .latest-container {
      max-width: 1200px;
      margin: 0 auto;
    }
    
    .latest-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 50px;
      flex-wrap: wrap;
      gap: 20px;
    }
    
    .latest-title-wrap .eyebrow {
      color: #777;
      text-transform: uppercase;
      font-size: 0.85rem;
      letter-spacing: 2px;
      margin-bottom: 10px;
      display: block;
    }
    
    .latest-title {
      font-size: 2.5rem;
      margin: 0;
      color: var(--color-green, #2b4c3b);
      font-family: 'Space Grotesk', sans-serif;
    }
    
    .category-filters {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    
    .filter-btn {
      padding: 8px 20px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 500;
      font-size: 0.9rem;
      transition: all 0.3s;
    }
    
    .filter-btn.active {
      background: var(--color-coral, #ef5350);
      color: #fff;
    }
    
    .filter-btn:not(.active) {
      background: #fff;
      color: #555;
      border: 1px solid #ddd;
    }
    
    .filter-btn:not(.active):hover {
      border-color: var(--color-coral);
      color: var(--color-coral);
    }

    .articles-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 40px;
    }
    
    .article-card {
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      gap: 20px;
      transition: transform 0.3s ease;
    }
    
    .article-card:hover {
      transform: translateY(-5px);
    }
    
    .article-image {
      width: 100%;
      aspect-ratio: 16/9;
      background-color: #eee;
      border-radius: 12px;
      overflow: hidden;
      position: relative;
    }
    
    .article-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }
    
    .article-card:hover .article-image img {
      transform: scale(1.05);
    }
    
    .article-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.8rem;
      color: #777;
    }
    
    .article-category {
      font-weight: 600;
      color: var(--color-coral, #ef5350);
    }
    
    .article-title {
      font-size: 1.4rem;
      font-weight: 700;
      line-height: 1.3;
      color: #333;
      margin: 0;
    }
    
    .article-excerpt {
      font-size: 0.95rem;
      color: #666;
      line-height: 1.6;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    @media (max-width: 768px) {
      .newsletter-headline { font-size: 2.5rem; }
      .stats-container { flex-direction: column; gap: 2rem; }
    }
  </style>
</head>
<body>

  <!-- ========== TOP UTILITY BAR ========== -->
  <div class="top-bar">
    <div class="top-bar-inner">
      <div class="top-bar-left">
        <a href="about.html">About Us</a>
        <a href="contact.html">Customer Support</a>
      </div>
      <div class="top-bar-center">
        Free shipping on orders above ₹499. <a href="flavors.html">Shop Now</a>
      </div>
      <div class="top-bar-right">
        <a href="login.html" class="login-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          Log In
        </a>
        <a href="signup.html" class="signup-link">
          Sign Up
        </a>
      </div>
    </div>
  </div>

  <!-- ========== MAIN HEADER ========== -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="site-logo" style="display:flex; align-items:center;">
        <img src="images/logo.png" alt="Cap Squeeze" style="height:40px; margin-right:10px;">
        Cap Squeeze.
      </a>

      <div class="header-right-icons">
        <button class="search-icon-btn" aria-label="Search">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        </button>
        <a href="about.html" aria-label="About">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        </a>
        <a href="#" aria-label="Wishlist">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
        </a>
        <a href="dashboard.html" class="cart-icon-link" aria-label="Cart">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <span class="cart-badge" id="cart-badge-count">0</span>
        </a>
      </div>
    </div>
  </header>

  <!-- ========== MAIN NAVIGATION ========== -->
  <nav class="main-nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-link">Home</a>
      <a href="flavors.html" class="nav-link">Shop Flavors</a>
      <a href="how-it-works.html" class="nav-link">How It Works</a>
      <a href="newsletter.html" class="nav-link active">Newsletter</a>
      <a href="about.html" class="nav-link">About</a>
      <a href="contact.html" class="nav-link">Contact</a>
    </div>
  </nav>

  <!-- ========== NEWSLETTER HERO ========== -->
  <main>
    <section class="newsletter-hero">
      <div class="newsletter-tag">
        <span class="pulse-dot"></span>
        The Squeeze Weekly
      </div>
      <h1 class="newsletter-headline">Insights on Hydration, <br><em>Health &amp; Innovation.</em></h1>
      <p class="newsletter-desc">Discover new flavor launches, health tips, and the science of hydration. Join readers discovering the cutting edge of modern beverages.</p>
      
      <form class="subscribe-form" onsubmit="event.preventDefault(); alert('Subscribed successfully!');">
        <input type="email" placeholder="Enter your email address..." class="subscribe-input" required>
        <button type="submit" class="subscribe-btn">Subscribe</button>
      </form>

      <div class="stats-container">
        <div class="stat-item">
          <span class="stat-number">10,000+</span>
          <span class="stat-label">Subscribers</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">24</span>
          <span class="stat-label">Editions</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">~3 min</span>
          <span class="stat-label">Avg. Read Time</span>
        </div>
      </div>
    </section>

    <!-- ========== LATEST EDITIONS ========== -->
    <section id="latest" class="latest-section">
      <div class="latest-container">
        <div class="latest-header">
          <div class="latest-title-wrap">
            <span class="eyebrow">Archive</span>
            <h2 class="latest-title">Latest <em>Editions</em></h2>
          </div>
          <div class="category-filters">
            <a href="#" class="filter-btn active">All</a>
            <a href="#" class="filter-btn">Health</a>
            <a href="#" class="filter-btn">Flavors</a>
            <a href="#" class="filter-btn">Behind the Scenes</a>
          </div>
        </div>
        
        <div class="articles-grid">
          
          <!-- Article 1 -->
          <a href="#" class="article-card">
            <div class="article-image">
              <img src="images/flavors/lemon.jpg" alt="Lemon Flavor Science" onerror="this.src='https://images.unsplash.com/photo-1556767576-5ec41e3239ea?q=80&w=600'">
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="article-meta">
                <span class="article-category">Flavors</span>
                <span>•</span>
                <span>Jul 18, 2026</span>
                <span>•</span>
                <span>3 min read</span>
              </div>
              <h3 class="article-title">The Science Behind Our New Zesty Lemon Cap</h3>
              <p class="article-excerpt">How we extracted the perfect citrus notes without adding a single gram of sugar or artificial preservatives to your water.</p>
            </div>
          </a>

          <!-- Article 2 -->
          <a href="#" class="article-card">
            <div class="article-image">
              <img src="images/flavors/berry.jpg" alt="Hydration Myths" onerror="this.src='https://images.unsplash.com/photo-1548839140-29a749e1bc4e?q=80&w=600'">
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="article-meta">
                <span class="article-category">Health</span>
                <span>•</span>
                <span>Jul 11, 2026</span>
                <span>•</span>
                <span>4 min read</span>
              </div>
              <h3 class="article-title">5 Hydration Myths You Need to Stop Believing</h3>
              <p class="article-excerpt">Does coffee really dehydrate you? Do you really need 8 glasses a day? We break down the latest scientific consensus.</p>
            </div>
          </a>

          <!-- Article 3 -->
          <a href="#" class="article-card">
            <div class="article-image">
              <img src="images/hero-bg.jpg" alt="Cap Squeeze Factory" onerror="this.src='https://images.unsplash.com/photo-1574624644917-814d485eb174?q=80&w=600'">
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="article-meta">
                <span class="article-category">Behind the Scenes</span>
                <span>•</span>
                <span>Jul 04, 2026</span>
                <span>•</span>
                <span>5 min read</span>
              </div>
              <h3 class="article-title">Inside the Factory: How Cap Squeeze is Made</h3>
              <p class="article-excerpt">Take an exclusive look into our state-of-the-art facility in Mumbai where flavor innovation meets sustainable manufacturing.</p>
            </div>
          </a>

          <!-- Article 4 -->
          <a href="#" class="article-card">
            <div class="article-image">
              <img src="https://images.unsplash.com/photo-1490818387583-1b5ba459ee53?q=80&w=600" alt="Vitamins">
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="article-meta">
                <span class="article-category">Health</span>
                <span>•</span>
                <span>Jun 27, 2026</span>
                <span>•</span>
                <span>3 min read</span>
              </div>
              <h3 class="article-title">Vitamin B12: The Hidden Energy Booster in Your Cap</h3>
              <p class="article-excerpt">Why we decided to fortify our berry flavor line with essential B vitamins, and what it means for your daily energy levels.</p>
            </div>
          </a>

          <!-- Article 5 -->
          <a href="#" class="article-card">
            <div class="article-image">
              <img src="https://images.unsplash.com/photo-1513624233765-b7ad12b4e5bb?q=80&w=600" alt="Workout">
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="article-meta">
                <span class="article-category">Health</span>
                <span>•</span>
                <span>Jun 20, 2026</span>
                <span>•</span>
                <span>2 min read</span>
              </div>
              <h3 class="article-title">Pre-Workout vs. Cap Squeeze: What's the Difference?</h3>
              <p class="article-excerpt">A deep dive into clean energy alternatives for athletes and gym-goers who want to avoid the crash.</p>
            </div>
          </a>

          <!-- Article 6 -->
          <a href="#" class="article-card">
            <div class="article-image">
              <img src="https://images.unsplash.com/photo-1563804820250-983141f237f3?q=80&w=600" alt="Recycling">
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div class="article-meta">
                <span class="article-category">Behind the Scenes</span>
                <span>•</span>
                <span>Jun 13, 2026</span>
                <span>•</span>
                <span>4 min read</span>
              </div>
              <h3 class="article-title">Our Commitment to 100% Recyclable Caps</h3>
              <p class="article-excerpt">The engineering challenges we faced to make our flavor dispensing mechanism completely environmentally friendly.</p>
            </div>
          </a>

        </div>
      </div>
    </section>
  </main>

  <!-- ========== FOOTER ========== -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col footer-col--brand">
        <a href="index.html" class="footer-logo" style="display:flex; align-items:center; margin-bottom:15px;">
          <img src="images/logo.png" alt="Cap Squeeze" style="height:45px; margin-right:12px;">
          Cap Squeeze.
        </a>
        <p style="font-size:.9rem;opacity:.85;margin-bottom:16px;line-height:1.6;">Cap Squeeze is India's first flavoured bottle cap. Turn any standard water bottle into a delicious, zero-sugar, vitamin-enhanced drink instantly. Over 12+ refreshing flavors made with real fruit extracts.</p>
        <p class="footer-help">Need Help?</p>
        <a href="mailto:hello@capsqueeze.com" class="footer-email">hello@capsqueeze.com</a>
      </div>

      <div class="footer-col">
        <h4>Shop</h4>
        <ul>
          <li><a href="flavors.html">All Flavors</a></li>
          <li><a href="#">Starter Kits</a></li>
          <li><a href="#">Accessories</a></li>
          <li><a href="#">Gift Cards</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Info</h4>
        <ul>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="contact.html">Customer Support</a></li>
          <li><a href="shipping.html">Shipping Info</a></li>
          <li><a href="returns.html">Returns Policy</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>My Choice</h4>
        <ul>
          <li><a href="dashboard.html">My Orders</a></li>
          <li><a href="dashboard.html">Track Order</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-copyright">
      <p>&copy; 2026 Cap Squeeze. All rights reserved.</p>
    </div>
  </footer>

  <script src="js/main.js"></script>
  <script>lucide.createIcons();</script>
  <!-- Supabase & Auth -->
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script src="js/auth.js"></script>
</body>
</html>
"""

with open("newsletter.html", "w", encoding="utf-8") as f:
    f.write(newsletter_html)

print("newsletter.html created successfully.")
