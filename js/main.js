document.addEventListener('DOMContentLoaded', () => {

  // ---- Quantity Steppers ----
  document.querySelectorAll('.qty-stepper').forEach(stepper => {
    stepper.querySelector('.qty-dec').addEventListener('click', () => {
      const input = stepper.querySelector('.qty-val');
      const val = parseInt(input.value);
      if (val > 1) input.value = val - 1;
    });
    stepper.querySelector('.qty-inc').addEventListener('click', () => {
      const input = stepper.querySelector('.qty-val');
      const val = parseInt(input.value);
      if (val < 99) input.value = val + 1;
    });
  });

  // ---- Carousel Arrows ----
  document.querySelectorAll('.carousel-arrow').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.dataset.target;
      const carousel = document.getElementById(targetId);
      if (!carousel) return;
      const card = carousel.querySelector('.product-card');
      const scrollAmount = card ? card.offsetWidth + 18 : 240;
      if (btn.classList.contains('carousel-arrow--next')) {
        carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
      } else {
        carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
      }
    });
  });

  // ---- Cart counter & Razorpay Integration ----
  let cartCount = 0;
  const cartBadge = document.querySelector('.cart-badge');

  // Razorpay public test key matching env parameters
  const RAZORPAY_PUBLIC_KEY = 'rzp_test_TBlhSKk7xUBKyj';

  const triggerRazorpayCheckout = (productName, amount) => {
    // Standard validation
    const amountInPaise = amount * 100;
    if (amountInPaise < 100) {
      alert('Error: Minimum transaction amount is ₹1 (100 paise).');
      return;
    }

    // Attempt backend POST call to order endpoint, fallback gracefully if serverless environment is local static
    fetch('/api/create-order', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        amount: amountInPaise,
        receipt: `rcpt_${Date.now()}`
      })
    })
    .then(res => {
      if (!res.ok) {
        throw new Error('API server unavailable. Initiating standalone client fallback.');
      }
      return res.json();
    })
    .then(orderData => {
      // Step 2: Open Razorpay checkout modal with order_id
      const options = {
        key: RAZORPAY_PUBLIC_KEY,
        amount: orderData.amount,
        currency: orderData.currency,
        name: 'Cap Squeeze',
        description: `Order: ${productName}`,
        order_id: orderData.order_id,
        handler: function (response) {
          // Send signature and verification payload to verify backend
          fetch('/api/verify-payment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              razorpay_order_id: response.razorpay_order_id,
              razorpay_payment_id: response.razorpay_payment_id,
              razorpay_signature: response.razorpay_signature
            })
          })
          .then(vRes => vRes.json())
          .then(vData => {
            if (vData.status === 'success') {
              alert(`Payment Verified successfully! Order ID: ${response.razorpay_order_id}`);
            } else {
              alert('Payment signature verification failed.');
            }
          })
          .catch(() => alert('Verification endpoint request failed. Payment completed.'));
        },
        prefill: {
          name: 'Customer Name',
          email: 'capsqueeze.co@gmail.com',
          contact: '9999999999'
        },
        theme: { color: '#ff7759' } // Accent coral matching Cohere theme
      };
      const rzp1 = new Razorpay(options);
      rzp1.open();
    })
    .catch(err => {
      console.log(err.message);
      // Fallback: Launch standalone Razorpay Checkout modal without order_id when running static S3 build
      const standaloneOptions = {
        key: RAZORPAY_PUBLIC_KEY,
        amount: amountInPaise,
        currency: 'INR',
        name: 'Cap Squeeze',
        description: `Standalone checkout: ${productName}`,
        handler: function (response) {
          alert(`Payment completed! ID: ${response.razorpay_payment_id}`);
        },
        prefill: {
          name: 'Customer Name',
          email: 'capsqueeze.co@gmail.com',
          contact: '9999999999'
        },
        theme: { color: '#ff7759' }
      };
      const rzp1 = new Razorpay(standaloneOptions);
      rzp1.open();
    });
  };

  document.querySelectorAll('.btn-addcart, .pfc-atc').forEach(btn => {
    btn.addEventListener('click', () => {
      cartCount++;
      if (cartBadge) cartBadge.textContent = cartCount;
      
      const productName = btn.getAttribute('data-name') || 'Cap Squeeze Item';
      const price = parseFloat(btn.getAttribute('data-price')) || 449;

      const origText = btn.textContent;
      btn.textContent = 'Opening Payment...';
      
      // Trigger checkout
      triggerRazorpayCheckout(productName, price);

      setTimeout(() => {
        btn.textContent = origText;
      }, 2000);
    });
  });

  // ---- Count-Up Statistics Animation ----
  const countUps = document.querySelectorAll('.count-up');
  if (countUps.length > 0) {
    const runCounter = (el) => {
      const target = parseInt(el.getAttribute('data-target'));
      const suffix = el.getAttribute('data-suffix') || '';
      let current = 0;
      const duration = 2000; // 2s duration
      const stepTime = Math.max(Math.floor(duration / target), 15);
      const timer = setInterval(() => {
        current += Math.ceil(target / (duration / stepTime));
        if (current >= target) {
          el.textContent = target + suffix;
          clearInterval(timer);
        } else {
          el.textContent = current + suffix;
        }
      }, stepTime);
    };

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            runCounter(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      countUps.forEach(el => observer.observe(el));
    } else {
      countUps.forEach(el => runCounter(el));
    }
  }

});

// Newsletter Form Handler
document.addEventListener('DOMContentLoaded', () => {
  const newsletterForm = document.getElementById('newsletter-form');
  if(newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      newsletterForm.style.display = 'none';
      document.getElementById('newsletter-success').style.display = 'block';
    });
  }
});
