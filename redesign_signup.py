import re

with open('signup.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the entire auth-container and its styles.
# Let's write the new styles and HTML.

new_auth_css = '''  <!-- AUTH STYLES -->
  <style>
    .auth-container {
      max-width: 400px;
      margin: 80px auto 120px;
      padding: 40px 30px;
      background: #ffffff;
      border-radius: 8px;
      text-align: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .auth-title {
      font-size: 2.5rem;
      font-weight: 400;
      margin-bottom: 8px;
      color: #000;
    }
    .auth-subtitle {
      color: #333;
      margin-bottom: 40px;
      font-size: 0.9rem;
      font-weight: 500;
    }
    .auth-form-group {
      margin-bottom: 30px;
      text-align: left;
    }
    .auth-input {
      width: 100%;
      padding: 8px 0;
      border: none;
      border-bottom: 1px solid #ccc;
      background: transparent;
      color: #333;
      font-size: 0.95rem;
      transition: all 0.3s ease;
    }
    .auth-input::placeholder {
      color: #888;
    }
    .auth-input:focus {
      outline: none;
      border-bottom-color: #1976d2;
    }
    .auth-btn {
      width: 100%;
      padding: 12px;
      border-radius: 4px;
      background: #1976d2;
      color: #fff;
      font-size: 1rem;
      font-weight: 600;
      border: none;
      cursor: pointer;
      transition: background 0.3s ease;
      margin-top: 10px;
    }
    .auth-btn:hover {
      background: #1565c0;
    }
    .auth-checkbox-group {
      display: flex;
      align-items: center;
      margin-top: 15px;
      margin-bottom: 30px;
      font-size: 0.9rem;
      color: #333;
      font-weight: 500;
    }
    .auth-checkbox-group input {
      margin-right: 8px;
      width: 16px;
      height: 16px;
      accent-color: #1976d2;
    }
    .auth-divider {
      display: flex;
      align-items: center;
      text-align: center;
      margin: 20px 0;
      color: #888;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.5px;
    }
    .auth-divider::before,
    .auth-divider::after {
      content: '';
      flex: 1;
      border-bottom: 1px solid #eee;
    }
    .auth-divider:not(:empty)::before {
      margin-right: .5em;
    }
    .auth-divider:not(:empty)::after {
      margin-left: .5em;
    }
    .auth-social-group {
      display: flex;
      gap: 15px;
      justify-content: space-between;
    }
    .auth-social-btn {
      flex: 1;
      padding: 10px 0;
      border: 1px solid #bbdefb;
      background: #fff;
      border-radius: 4px;
      color: #1976d2;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    .auth-social-btn:hover {
      background: #f0f8ff;
      border-color: #1976d2;
    }
  </style>
'''

new_auth_content = '''  <section style="min-height: 80vh; display: flex; align-items: center; justify-content: center; background: #fafafa;">
    <div class="auth-container">
      <h1 class="auth-title">Sign up</h1>
      <p class="auth-subtitle">Sign up to continue</p>
      
      <form onsubmit="event.preventDefault();">
        <div class="auth-form-group">
          <input type="text" id="name" class="auth-input" placeholder="Name" required>
        </div>
        <div class="auth-form-group">
          <input type="email" id="email" class="auth-input" placeholder="Email" required>
        </div>
        <div class="auth-form-group" style="margin-bottom: 20px;">
          <input type="password" id="password" class="auth-input" placeholder="Password" required>
        </div>
        
        <button type="submit" class="auth-btn">Sign up</button>
        
        <div class="auth-checkbox-group">
          <input type="checkbox" id="remember" checked>
          <label for="remember">Remember me</label>
        </div>
      </form>

      <div class="auth-divider">ACCESS QUICKLY</div>

      <div class="auth-social-group">
        <button class="auth-social-btn">Google</button>
        <button class="auth-social-btn">Linkedin</button>
        <button class="auth-social-btn">SSO</button>
      </div>
    </div>
  </section>'''

# Extract boundaries
start_marker = '  <!-- AUTH STYLES -->'
end_marker = '  </section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if start_idx != -1 and content.find(end_marker, start_idx) != -1:
    content = content[:start_idx] + new_auth_css + new_auth_content + content[end_idx:]
    with open('signup.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Signup page updated successfully!")
else:
    print("Could not find auth markers in signup.html")
