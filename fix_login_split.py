import os

css = '''  <!-- SPLIT AUTH STYLES -->
  <style>
    .split-auth-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 85vh;
      background: #f4f6f9;
      padding: 40px 20px;
      position: relative;
      overflow: hidden;
    }
    
    /* Background decorative shapes */
    .split-auth-wrapper::before {
      content: '';
      position: absolute;
      top: -10%;
      right: -5%;
      width: 400px;
      height: 400px;
      background: #e57373; /* coral light */
      border-radius: 50%;
      opacity: 0.1;
      z-index: 0;
    }
    .split-auth-wrapper::after {
      content: '';
      position: absolute;
      bottom: -10%;
      left: -10%;
      width: 300px;
      height: 300px;
      background: #ffb74d; /* yellow light */
      border-radius: 50%;
      opacity: 0.1;
      z-index: 0;
    }

    .split-auth-container {
      position: relative;
      width: 900px;
      max-width: 100%;
      min-height: 550px;
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
      display: flex;
      overflow: hidden;
      z-index: 1;
    }
    
    .split-panel {
      flex: 1;
      padding: 60px 40px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }

    .split-panel.colored {
      background: var(--color-coral, #ef5350);
      color: #fff;
      background-image: linear-gradient(135deg, var(--color-coral, #ef5350) 0%, #d32f2f 100%);
    }
    
    .split-panel.white {
      background: #fff;
      color: #333;
    }

    /* Colored Panel Content */
    .colored-title {
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 20px;
      font-family: 'Space Grotesk', sans-serif;
    }
    .colored-desc {
      font-size: 1rem;
      line-height: 1.6;
      margin-bottom: 40px;
      font-weight: 300;
      padding: 0 20px;
    }
    .colored-btn {
      background: transparent;
      border: 2px solid #fff;
      color: #fff;
      padding: 12px 40px;
      border-radius: 30px;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: 1px;
      cursor: pointer;
      text-transform: uppercase;
      transition: all 0.3s ease;
      text-decoration: none;
    }
    .colored-btn:hover {
      background: #fff;
      color: var(--color-coral, #ef5350);
    }

    /* White Panel Content */
    .white-title {
      color: var(--color-coral, #ef5350);
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 20px;
      font-family: 'Space Grotesk', sans-serif;
    }
    .social-icons {
      display: flex;
      gap: 15px;
      margin-bottom: 25px;
    }
    .social-icon {
      width: 45px;
      height: 45px;
      border: 1px solid #ddd;
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #555;
      text-decoration: none;
      transition: all 0.3s ease;
    }
    .social-icon:hover {
      border-color: var(--color-coral, #ef5350);
      color: var(--color-coral, #ef5350);
    }
    
    .use-email-text {
      color: #888;
      font-size: 0.9rem;
      margin-bottom: 25px;
    }

    .form-group {
      width: 100%;
      max-width: 320px;
      margin-bottom: 15px;
      position: relative;
    }
    .form-input {
      width: 100%;
      background: #f4f8f7;
      border: none;
      padding: 15px 20px 15px 45px;
      border-radius: 8px;
      font-size: 0.95rem;
      color: #333;
      outline: none;
      transition: all 0.3s ease;
    }
    .form-input:focus {
      background: #eef5f4;
      box-shadow: inset 0 0 0 2px var(--color-coral, #ef5350);
    }
    .form-icon {
      position: absolute;
      left: 15px;
      top: 50%;
      transform: translateY(-50%);
      color: #aaa;
      width: 18px;
      height: 18px;
    }
    
    .white-btn {
      background: var(--color-coral, #ef5350);
      color: #fff;
      border: none;
      padding: 12px 50px;
      border-radius: 30px;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: 1px;
      cursor: pointer;
      text-transform: uppercase;
      margin-top: 15px;
      transition: all 0.3s ease;
      box-shadow: 0 4px 15px rgba(239, 83, 80, 0.3);
    }
    .white-btn:hover {
      background: #d32f2f;
      transform: translateY(-2px);
    }
    
    .forgot-link {
      display: block;
      margin-top: 15px;
      color: #777;
      text-decoration: none;
      font-size: 0.9rem;
      transition: color 0.3s;
    }
    .forgot-link:hover {
      color: var(--color-coral, #ef5350);
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
      .split-auth-container {
        flex-direction: column;
      }
      .split-panel {
        padding: 40px 20px;
      }
    }
  </style>
'''

login_content = '''
  <section class="split-auth-wrapper">
    <div class="split-auth-container">
      
      <!-- Left White Panel (Login Form) -->
      <div class="split-panel white">
        <h2 class="white-title">Sign in to Cap Squeeze</h2>
        
        <div class="social-icons">
          <a href="#" class="social-icon"><i data-lucide="facebook"></i></a>
          <a href="#" class="social-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/><path d="M12 8v8m-4-4h8"/></svg></a>
          <a href="#" class="social-icon"><i data-lucide="linkedin"></i></a>
        </div>
        
        <p class="use-email-text">or use your email account:</p>

        <form onsubmit="event.preventDefault();" style="width: 100%; display: flex; flex-direction: column; align-items: center;">
          <div class="form-group">
            <i data-lucide="mail" class="form-icon"></i>
            <input type="email" class="form-input" placeholder="Email" required>
          </div>
          <div class="form-group">
            <i data-lucide="lock" class="form-icon"></i>
            <input type="password" class="form-input" placeholder="Password" required>
          </div>
          
          <a href="#" class="forgot-link">Forgot your password?</a>
          <button type="submit" class="white-btn" style="margin-top: 25px;">Sign In</button>
        </form>
      </div>

      <!-- Right Colored Panel (Signup Prompt) -->
      <div class="split-panel colored">
        <h2 class="colored-title">Hello, Friend!</h2>
        <p class="colored-desc">Enter your personal details and start journey with us</p>
        <a href="signup.html" class="colored-btn">Sign Up</a>
      </div>

    </div>
  </section>
'''

# Apply to login.html
with open('login.html', 'r', encoding='utf-8') as f:
    l_content = f.read()

# Instead of looking for AUTH STYLES, we'll look for PAGE HERO (which exists because it's still contact page content)
l_start = l_content.find('  <!-- PAGE HERO -->')
l_end = l_content.find('  <!-- ========== FOOTER ========== -->')

if l_start != -1 and l_end != -1:
    l_content = l_content[:l_start] + css + login_content + '\n' + l_content[l_end:]
    
    # Fix the title as well, since it says "Contact Us" currently
    l_content = l_content.replace('<title>Contact Us — Cap Squeeze</title>', '<title>Sign In — Cap Squeeze</title>')
    
    with open('login.html', 'w', encoding='utf-8') as f:
        f.write(l_content)
    print("login.html properly fixed and styled!")
else:
    print("Could not find bounds in login.html")
