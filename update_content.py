import re

def update_about():
    with open('about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Hero
    html = re.sub(
        r'<h1>We got tired of.*?</h1>',
        r'<h1>We got tired of <span class="gradient-text">boring</span> water.</h1>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<p>So we built India\'s first flavoured bottle cap.</p>',
        r'<p>So we built India\'s first flavored bottle cap. No sugar, no artificial junk—just pure, refreshing taste twisted into every sip.</p>',
        html
    )

    # Update Founder's Note
    html = re.sub(
        r'<p style="font-style: italic; color: var\(--color-text-main\);.*?</p>',
        r'<p style="font-style: italic; color: var(--color-text-main); font-size: 1.05rem; line-height: 1.6; margin-bottom: 24px; opacity: 0.9;">"I started Cap Squeeze because I noticed a massive problem in India: we either drink plain, boring water or sugar-loaded sodas. There was no middle ground. I wanted a way to make hydration exciting without compromising health. We spent months engineering the perfect flavor pod that fits right onto your everyday water bottle. Our mission is simple: to make zero-sugar hydration the easiest, most delicious choice you make every day."</p>',
        html, flags=re.DOTALL
    )

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("about.html updated")

def update_how_it_works():
    with open('how-it-works.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Let's just do a blanket replacement for the hero text if it exists
    html = re.sub(
        r'<p class="page-hero-eyebrow">.*?<h1',
        r'<p class="page-hero-eyebrow">The Magic Behind Cap Squeeze</p>\n    <h1',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<h1>How It Works</h1>\s*<p>.*?<',
        r'<h1>How It Works</h1>\n    <p>Hydration has never been this easy. Transform any standard 28mm water bottle into a flavor-packed experience in three simple steps.</p>\n  <',
        html, flags=re.DOTALL
    )

    with open('how-it-works.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("how-it-works.html updated")

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Update hero subtext
    html = re.sub(
        r'India\'s first flavoured bottle cap turns any regular water bottle.*?Works on any standard 28mm bottle — Bisleri, Kinley, Aquafina &amp; more.',
        r'India\'s first flavoured bottle cap turns any regular water bottle into a delicious zero-sugar drink. Twist on. Squeeze. Enjoy. Works seamlessly on any standard 28mm bottle — Bisleri, Kinley, Aquafina, and more. Hydration, revolutionized.',
        html, flags=re.DOTALL
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated")

def update_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(
        r'<p>We\'d love to hear from you.*?</p>',
        r'<p>Whether you have a question about our flavors, need help with your order, or just want to say hi, our team is here for you. We aim to respond to all inquiries within 24 hours.</p>',
        html, flags=re.DOTALL
    )

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("contact.html updated")

update_about()
update_how_it_works()
update_index()
update_contact()

