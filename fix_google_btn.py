import os

google_btn_html = '''        <a href="#" class="google-btn">
          <svg viewBox="0 0 24 24" width="22" height="22" xmlns="http://www.w3.org/2000/svg">
            <g transform="matrix(1, 0, 0, 1, 12, 12)">
              <path fill="#4285F4" d="M11.64 0.692C11.64 -0.052 11.57 -0.732 11.45 -1.392H-0.01V2.628H6.55C6.26 3.968 5.48 5.128 4.37 5.868V8.468H8.29C10.59 6.348 11.64 3.192 11.64 0.692Z" />
              <path fill="#34A853" d="M-0.00999999 11.848C3.27 11.848 6.01 10.768 7.99 8.868L4.07 6.268C3.01 6.988 1.63 7.428 -0.00999999 7.428C-3.18 7.428 -5.87 5.288 -6.84 2.388H-10.89V5.048C-8.91 8.988 -4.8 11.848 -0.00999999 11.848Z" />
              <path fill="#FBBC05" d="M-6.83 2.388C-7.08 1.668 -7.21 0.888 -7.21 0.0879999C-7.21 -0.712 -7.08 -1.492 -6.83 -2.212V-4.872H-10.88C-11.68 -3.272 -12.13 -1.452 -12.13 0.0879999C-12.13 1.628 -11.68 3.448 -10.88 5.048L-6.83 2.388Z" />
              <path fill="#EA4335" d="M-0.00999999 -7.252C1.77 -7.252 3.35 -6.642 4.61 -5.442L8.35 -9.182C6.01 -11.362 3.27 -12.672 -0.00999999 -12.672C-4.8 -12.672 -8.91 -9.812 -10.89 -5.872L-6.84 -3.212C-5.87 -6.112 -3.18 -7.252 -0.00999999 -7.252Z" />
            </g>
          </svg>
          Continue with Google
        </a>'''

google_btn_css = '''    .google-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      width: 100%;
      max-width: 320px;
      padding: 12px 20px;
      margin: 0 auto 25px;
      background: #fff;
      border: 1px solid #ddd;
      border-radius: 30px;
      color: #555;
      font-size: 1rem;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.3s ease;
    }
    .google-btn:hover {
      background: #fcfcfc;
      border-color: #ccc;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
'''

files = ['login.html', 'signup.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace social icons HTML
    start_idx = content.find('<div class="social-icons">')
    end_idx = content.find('</div>', start_idx) + 6
    
    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + google_btn_html + content[end_idx:]
    
    # Add Google btn CSS right before </style> in SPLIT AUTH STYLES
    style_end_idx = content.find('</style>')
    if style_end_idx != -1 and '.google-btn' not in content:
        content = content[:style_end_idx] + google_btn_css + content[style_end_idx:]
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file}")
