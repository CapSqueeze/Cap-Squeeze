import os

# We will use contact.html as the base template since it's verified to be intact
with open('contact.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Custom CSS for Auth forms
auth_css = '''  <!-- AUTH STYLES -->
  <style>
    .auth-container {
      max-width: 480px;
      margin: 80px auto 120px;
      padding: 50px 40px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      text-align: center;
    }
    .auth-title {
      font-size: 2.2rem;
      font-weight: 800;
      margin-bottom: 10px;
      color: var(--color-text-main);
    }
    .auth-subtitle {
      color: var(--color-text-muted);
      margin-bottom: 40px;
      font-size: 1rem;
    }
    .auth-form-group {
      margin-bottom: 20px;
      text-align: left;
    }
    .auth-label {
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      margin-bottom: 8px;
      color: var(--color-text-main);
    }
    .auth-input {
      width: 100%;
      padding: 14px 20px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--color-text-main);
      font-size: 1rem;
      transition: all 0.3s ease;
    }
    .auth-input:focus {
      outline: none;
      border-color: var(--color-coral);
      box-shadow: 0 0 0 3px rgba(239,83,80,0.1);
    }
    .auth-btn {
      width: 100%;
      padding: 16px;
      border-radius: 30px;
      background: var(--color-coral);
      color: #fff;
      font-size: 1.1rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      transition: all 0.3s ease;
      margin-top: 10px;
    }
    .auth-btn:hover {
      background: #e53935;
      transform: translateY(-2px);
    }
    .auth-links {
      margin-top: 30px;
      font-size: 0.95rem;
      color: var(--color-text-muted);
    }
    .auth-links a {
      color: var(--color-coral);
      font-weight: 600;
      text-decoration: none;
    }
    .auth-links a:hover {
      text-decoration: underline;
    }
    .forgot-pw {
      display: block;
      text-align: right;
      font-size: 0.85rem;
      margin-top: 8px;
      color: var(--color-text-muted);
      text-decoration: none;
    }
    .forgot-pw:hover {
      color: var(--color-coral);
    }
  </style>
'''

# Login Page Content
login_content = auth_css + '''
  <section style="min-height: 80vh; display: flex; align-items: center; justify-content: center; background: var(--bg-surface);">
    <div class="auth-container">
      <h1 class="auth-title">Welcome Back</h1>
      <p class="auth-subtitle">Sign in to your Cap Squeeze account.</p>
      
      <form onsubmit="event.preventDefault(); alert('Login functionality will be connected to your backend.');">
        <div class="auth-form-group">
          <label class="auth-label" for="email">Email Address</label>
          <input type="email" id="email" class="auth-input" placeholder="hello@capsqueeze.com" required>
        </div>
        <div class="auth-form-group">
          <label class="auth-label" for="password">Password</label>
          <input type="password" id="password" class="auth-input" placeholder="••••••••" required>
          <a href="#" class="forgot-pw">Forgot password?</a>
        </div>
        <button type="submit" class="auth-btn">Sign In</button>
      </form>

      <div class="auth-links">
        Don't have an account? <a href="signup.html">Create one</a>
      </div>
    </div>
  </section>
'''

# Signup Page Content
signup_content = auth_css + '''
  <section style="min-height: 80vh; display: flex; align-items: center; justify-content: center; background: var(--bg-surface);">
    <div class="auth-container">
      <h1 class="auth-title">Create Account</h1>
      <p class="auth-subtitle">Join the hydration revolution today.</p>
      
      <form onsubmit="event.preventDefault(); alert('Signup functionality will be connected to your backend.');">
        <div style="display: flex; gap: 16px; margin-bottom: 20px;">
          <div class="auth-form-group" style="margin-bottom: 0; flex: 1;">
            <label class="auth-label" for="fname">First Name</label>
            <input type="text" id="fname" class="auth-input" placeholder="Priya" required>
          </div>
          <div class="auth-form-group" style="margin-bottom: 0; flex: 1;">
            <label class="auth-label" for="lname">Last Name</label>
            <input type="text" id="lname" class="auth-input" placeholder="Sharma" required>
          </div>
        </div>
        <div class="auth-form-group">
          <label class="auth-label" for="email">Email Address</label>
          <input type="email" id="email" class="auth-input" placeholder="hello@capsqueeze.com" required>
        </div>
        <div class="auth-form-group">
          <label class="auth-label" for="password">Password</label>
          <input type="password" id="password" class="auth-input" placeholder="Create a strong password" required>
        </div>
        <button type="submit" class="auth-btn">Create My Account</button>
      </form>

      <div class="auth-links">
        Already have an account? <a href="login.html">Sign in</a>
      </div>
    </div>
  </section>
'''

def write_auth_page(filename, title, desc, html_content):
    content = template
    content = content.replace('<title>Contact Us — Cap Squeeze</title>', f'<title>{title}</title>')
    content = content.replace('<meta name="description" content="Get in touch with Cap Squeeze. Reach out for support, wholesale inquiries, or to find out more about our flavored bottle caps.">', f'<meta name="description" content="{desc}">')
    content = content.replace('nav-link--active', '') # remove active class from contact
    
    main_content_start = content.find('  <!-- PAGE HERO -->')
    main_content_end = content.find('  <!-- FOOTER -->')
    
    if main_content_start != -1 and main_content_end != -1:
        content = content[:main_content_start] + html_content + content[main_content_end:]
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

write_auth_page('login.html', 'Sign In — Cap Squeeze', 'Sign in to your Cap Squeeze account to manage orders, subscriptions, and rewards.', login_content)
write_auth_page('signup.html', 'Create Account — Cap Squeeze', 'Create a new Cap Squeeze account to get exclusive access to flavors and rewards.', signup_content)

print("Auth pages successfully fixed using a clean template!")
