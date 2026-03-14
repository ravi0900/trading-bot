from flask import Flask, render_template, request, jsonify
from bot.orders import execute_order
import logging

# We can reuse the existing logging config, but we also want to catch Flask errors if needed
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/order', methods=['POST'])
def place_order():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "No data provided"}), 400
            
        symbol = data.get('symbol', 'BTCUSDT')
        side = data.get('side')
        order_type = data.get('order_type')
        quantity = data.get('quantity')
        price = data.get('price')

        if not all([side, order_type, quantity]):
            return jsonify({"success": False, "error": "Missing required fields"}), 400

        # Convert to appropriate types
        quantity = float(quantity)
        price = float(price) if price else None

        # Execute
        result = execute_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        return jsonify({"success": True, "data": result})

    except ValueError as ve:
        return jsonify({"success": False, "error": str(ve)}), 400
    except Exception as e:
        # e.g. Binance API Error
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True, port=5000)
