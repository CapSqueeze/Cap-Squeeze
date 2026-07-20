import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the top-bar-right block
    login_link_str = '''<a href="login.html" class="login-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          Log In
        </a>'''
        
    signup_link_str = '''<a href="login.html" class="login-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          Log In
        </a>
        <a href="signup.html" class="signup-link" style="margin-left: 15px;">
          Sign Up
        </a>'''

    if login_link_str in content:
        if '<a href="signup.html" class="signup-link"' not in content:
            content = content.replace(login_link_str, signup_link_str)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added Sign Up link to {file}")
        else:
            print(f"Sign Up link already in {file}")
    else:
        print(f"Could not find exact login link pattern in {file}")
