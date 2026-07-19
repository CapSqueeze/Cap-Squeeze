// Razorpay API handlers for Node.js serverless functions (e.g. Vercel api/create-order.js)
const Razorpay = require('razorpay');
const crypto = require('crypto');

// Initialize Razorpay client with environment variables
const razorpay = new Razorpay({
  key_id: process.env.RAZORPAY_KEY_ID || 'rzp_test_TBlhSKk7xUBKyj',
  key_secret: process.env.RAZORPAY_KEY_SECRET || 'ZdJNeGTvBDycOcl9e3r5Vk57'
});

// CREATE ORDER HANDLER (POST /api/create-order)
exports.createOrder = async (req, res) => {
  try {
    const { amount, receipt } = req.body;

    if (!amount || amount < 100) {
      return res.status(400).json({ error: 'Minimum amount must be 100 paise (₹1).' });
    }

    const options = {
      amount: parseInt(amount), // in paise
      currency: 'INR',
      receipt: receipt || `receipt_${Date.now()}`
    };

    const order = await razorpay.orders.create(options);
    return res.status(200).json({
      order_id: order.id,
      amount: order.amount,
      currency: order.currency
    });
  } catch (error) {
    console.error('Error creating Razorpay order:', error);
    return res.status(500).json({ error: 'Failed to create order' });
  }
};

// VERIFY SIGNATURE HANDLER (POST /api/verify-payment)
exports.verifyPayment = async (req, res) => {
  try {
    const { razorpay_order_id, razorpay_payment_id, razorpay_signature } = req.body;

    if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature) {
      return res.status(400).json({ error: 'Missing signature verification parameters' });
    }

    const hmac = crypto.createHmac('sha256', process.env.RAZORPAY_KEY_SECRET || 'ZdJNeGTvBDycOcl9e3r5Vk57');
    hmac.update(razorpay_order_id + '|' + razorpay_payment_id);
    const generated_signature = hmac.digest('hex');

    if (generated_signature === razorpay_signature) {
      return res.status(200).json({ status: 'success', message: 'Payment signature verified successfully.' });
    } else {
      return res.status(400).json({ status: 'failure', message: 'Payment signature verification failed.' });
    }
  } catch (error) {
    console.error('Error verifying Razorpay signature:', error);
    return res.status(500).json({ error: 'Internal verification failure' });
  }
};
