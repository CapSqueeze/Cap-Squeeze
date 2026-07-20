import glob
for f in glob.glob('*.html'):
    content = open(f, 'r', encoding='utf-8').read()
    content = content.replace('style="margin-left: 15px;"', '')
    open(f, 'w', encoding='utf-8').write(content)
