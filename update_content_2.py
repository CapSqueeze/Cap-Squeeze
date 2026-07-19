import re

def update_flavors():
    with open('flavors.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Starter Kit
    html = re.sub(
        r'<p class="pfc-desc".*?>Everything you need to start. 1 premium Cap Squeeze flavour cap \+ 6 natural zero-sugar flavour pods.</p>',
        r'<p class="pfc-desc" style="font-size: 0.9rem; color: var(--color-text-muted); line-height: 1.5; margin-bottom: 20px;">The ultimate gateway to guilt-free hydration. Includes our premium reusable flavor-infusion cap and 6 of our best-selling zero-sugar pods.</p>',
        html
    )

    # Mega pack
    html = re.sub(
        r'<p class="pfc-desc".*?>Stock up and save big. 12 recyclable natural flavour pods - no cap included. Perfect for regular customers.</p>',
        r'<p class="pfc-desc" style="font-size: 0.9rem; color: var(--color-text-muted); line-height: 1.5; margin-bottom: 20px;">Never run out of your favorite taste. 12 organic, eco-friendly refill pods designed to keep you hydrated and refreshed all month long.</p>',
        html
    )

    # Single flavor
    html = re.sub(
        r'<p class="pfc-desc".*?>Found your go-to flavour\? Get 6 of the same pod. Perfect for your daily routine hydration.</p>',
        r'<p class="pfc-desc" style="font-size: 0.9rem; color: var(--color-text-muted); line-height: 1.5; margin-bottom: 20px;">Obsessed with just one flavor? We get it. Get a 6-pack of your absolute favorite zero-calorie pod for uninterrupted daily enjoyment.</p>',
        html
    )

    with open('flavors.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("flavors.html updated")

def update_faq():
    with open('faq.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(
        r'<h1>Got <span class="gradient-text">questions</span>\? We\'ve got answers.</h1>\s*</section>',
        r'<h1>Got <span class="gradient-text">questions</span>? We\'ve got answers.</h1>\n    <p>Everything you need to know about Cap Squeeze, from how it works to our shipping policies. If you can\'t find your answer here, just reach out to us!</p>\n  </section>',
        html
    )

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("faq.html updated")

update_flavors()
update_faq()

