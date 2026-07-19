import os

auth_js_content = """
// Initialize Supabase Client
const SUPABASE_URL = 'https://ceszjffxeswpffjugnmj.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNlc3pqZmZ4ZXN3cGZmanVnbm1qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQ0NzI5OTMsImV4cCI6MjEwMDA0ODk5M30.u0rL0jnqnICTc62DvUZ9wyriC2hZ7wFSCypr_4dMmbY';

const supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// Check if user is logged in and update UI
async function checkUserSession() {
  const { data: { session } } = await supabase.auth.getSession();
  
  const loginLinks = document.querySelectorAll('.login-link');
  
  if (session) {
    // User is logged in
    loginLinks.forEach(link => {
      link.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
        Log Out
      `;
      link.href = "#";
      link.addEventListener('click', async (e) => {
        e.preventDefault();
        await supabase.auth.signOut();
        window.location.reload();
      });
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  checkUserSession();
  
  // Google Auth Button
  const googleBtns = document.querySelectorAll('.google-btn');
  googleBtns.forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'google',
        options: {
          redirectTo: window.location.origin + '/index.html'
        }
      });
      if (error) {
        console.error('Error logging in with Google:', error);
        alert('Failed to login with Google.');
      }
    });
  });

  // Email/Password Signup Form
  const signupForm = document.getElementById('signup-form');
  if (signupForm) {
    signupForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const email = document.getElementById('signup-email').value;
      const password = document.getElementById('signup-password').value;
      const name = document.getElementById('signup-name').value;
      
      const { data, error } = await supabase.auth.signUp({
        email,
        password,
        options: {
          data: {
            full_name: name
          }
        }
      });
      
      if (error) {
        alert(error.message);
      } else {
        alert('Signup successful! Check your email for confirmation, or try logging in.');
        window.location.href = 'login.html';
      }
    });
  }

  // Email/Password Login Form
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const email = document.getElementById('login-email').value;
      const password = document.getElementById('login-password').value;
      
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password
      });
      
      if (error) {
        alert(error.message);
      } else {
        window.location.href = 'index.html';
      }
    });
  }
});
"""

# Create js/auth.js
os.makedirs('js', exist_ok=True)
with open('js/auth.js', 'w', encoding='utf-8') as f:
    f.write(auth_js_content)
    
print("Created js/auth.js")

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We need to inject Supabase CDN and auth.js into every HTML file before </body>
supabase_scripts = '''  <!-- Supabase & Auth -->
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script src="js/auth.js"></script>
'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already added
    if '<script src="js/auth.js"></script>' not in content:
        # Find </body>
        body_idx = content.rfind('</body>')
        if body_idx != -1:
            content = content[:body_idx] + supabase_scripts + content[body_idx:]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected scripts into {file}")

# We need to update login.html and signup.html forms to have the correct IDs so auth.js can find them.
# For signup.html
with open('signup.html', 'r', encoding='utf-8') as f:
    signup_content = f.read()

signup_content = signup_content.replace('<form onsubmit="event.preventDefault(); alert(\'Signup functionality will be connected to your backend.\');"', '<form id="signup-form"')
signup_content = signup_content.replace('<form onsubmit="event.preventDefault();"', '<form id="signup-form"')
signup_content = signup_content.replace('placeholder="Name" required>', 'id="signup-name" placeholder="Name" required>')
signup_content = signup_content.replace('placeholder="Email" required>', 'id="signup-email" placeholder="Email" required>')
signup_content = signup_content.replace('placeholder="Password" required>', 'id="signup-password" placeholder="Password" required>')

with open('signup.html', 'w', encoding='utf-8') as f:
    f.write(signup_content)

# For login.html
with open('login.html', 'r', encoding='utf-8') as f:
    login_content = f.read()

login_content = login_content.replace('<form onsubmit="event.preventDefault();"', '<form id="login-form"')
login_content = login_content.replace('placeholder="Email" required>', 'id="login-email" placeholder="Email" required>')
login_content = login_content.replace('placeholder="Password" required>', 'id="login-password" placeholder="Password" required>')

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(login_content)

print("Updated form IDs in login.html and signup.html")
