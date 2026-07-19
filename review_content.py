import os

files = ['index.html', 'about.html', 'how-it-works.html', 'flavors.html', 'faq.html', 'contact.html']

for f in files:
    if os.path.exists(f):
        print(f"\n--- {f} ---")
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            # print first 500 chars of body
            body_start = content.find('<body')
            if body_start != -1:
                print(content[body_start:body_start+500])
