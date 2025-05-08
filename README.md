# 💳 Mobile Money Payment Mock-Up API

A simple mock STK Push payment API using Python, designed to be deployed on [Vercel](https://vercel.com) as a serverless function.

This API accepts POST requests with a phone number and an amount, and returns a mock response indicating a successful STK push initiation.

---

## 🚀 Live API Endpoint

```http
POST https://payment-mock-up-api.vercel.app/stk-push

### ✅ Request Body

{
  "phone": "0712345678",
  "amount": 500
}

### ✅ Response

{
  "status": "success",
  "message": "STK Push initiated for 0712345678 of amount 500"
}

### 👨‍💻 Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.