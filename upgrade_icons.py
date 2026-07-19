import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Emojis to Lucide Icons mapping
replacements = {
    '💧': '<i data-lucide="droplet" class="icon-inline"></i>',
    '🔄': '<i data-lucide="refresh-cw" class="icon-inline"></i>',
    '💥': '<i data-lucide="zap" class="icon-inline"></i>',
    '🚫': '<i data-lucide="ban" class="icon-inline"></i>',
    '♻️': '<i data-lucide="recycle" class="icon-inline"></i>',
    '🍋': '<i data-lucide="leaf" class="icon-inline"></i>',
    '⚡': '<i data-lucide="zap" class="icon-inline"></i>',
    '💛': '<i data-lucide="heart" class="icon-inline"></i>',
    '✅': '<i data-lucide="check-circle" class="icon-inline"></i>',
    '🇮🇳': '<i data-lucide="map-pin" class="icon-inline"></i>',
    '🔒': '<i data-lucide="lock" class="icon-inline"></i>',
    '💬': '<i data-lucide="message-circle" class="icon-inline"></i>',
    '🏆': '<i data-lucide="award" class="icon-inline"></i>',
    '💰': '<i data-lucide="tag" class="icon-inline"></i>',
    '★★★★★': '<div class="stars-wrap" style="display:flex; gap:4px; margin-bottom:15px; color:#f1c40f;"><i data-lucide="star" class="icon-star"></i><i data-lucide="star" class="icon-star"></i><i data-lucide="star" class="icon-star"></i><i data-lucide="star" class="icon-star"></i><i data-lucide="star" class="icon-star"></i></div>'
}

lucide_script_head = '  <script src="https://unpkg.com/lucide@latest"></script>\\n'
lucide_script_body = '  <script>lucide.createIcons();</script>\\n'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace emojis with Lucide tags
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # 2. Inject Lucide CDN into <head>
    if '<script src="https://unpkg.com/lucide@latest"></script>' not in content:
        content = content.replace('</head>', lucide_script_head + '</head>')
        
    # 3. Inject lucide.createIcons() before </body>
    if '<script>lucide.createIcons();</script>' not in content:
        content = content.replace('</body>', lucide_script_body + '</body>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Lucide icons applied to all HTML files successfully!")
