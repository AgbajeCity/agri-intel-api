from flask import Flask, jsonify

app = Flask(__name__)

# This is our hard-coded "AI" data, just like in the PDF
market_data = {
    "coffee": {
        "product": "Premium Coffee Beans",
        "fair_market_price_usd": 4.85,
        "ai_insight": "Projected 5% price increase next week.",
        "demand_signal": "High demand in Asian markets.",
        "last_updated": "5 minutes ago"
    },
    "maize": {
        "product": "Maize",
        "fair_market_price_usd": 0.32,
        "ai_insight": "Projected -2% price decrease due to local oversupply.",
        "demand_signal": "High demand in local processing centers.",
        "last_updated": "2 minutes ago"
    }
}

@app.route('/')
def home():
    return "AI Market Insight API is live."

@app.route('/api/market-insight/<product_name>')
def get_insight(product_name):
    insight = market_data.get(product_name.lower())

    if not insight:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(insight)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)