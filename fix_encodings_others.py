html_files = ['flavors.html', 'about.html', 'faq.html', 'how-it-works.html']

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix encodings
        content = content.replace('â‚¹', '₹')
        content = content.replace('ðŸ †', '🏆')
        content = content.replace('ðŸ’°', '💰')
        content = content.replace('dYs', '💧')
        content = content.replace('dYs', '💧')
        content = content.replace('dYrdY3', '🇮🇳')
        content = content.replace('dYrdY3', '🇮🇳')
        content = content.replace('dY"\'', '🔒')
        content = content.replace('dY\'', '💬')
        content = content.replace('dY\'', '💬')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed encodings in {file}")
    except Exception as e:
        print(f"Skipped {file} or error: {e}")
