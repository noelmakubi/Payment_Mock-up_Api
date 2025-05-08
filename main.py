from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/stk-push/', methods=['POST'])
def stk_push():
    data = request.get_json()
    phone = data.get('phone')
    amount = data.get('amount')

    # For testing purposes, we return a mock success response
    return jsonify({
        "status": "success",
        "message": f"STK Push initiated for {phone} of amount {amount}"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
