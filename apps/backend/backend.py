# This code imports the Flask and jsonify modules
from flask import Flask, jsonify
# The os module is also imported to allow access to environment variables
import os

# A new Flask application is created
app = Flask(__name__)

# A list of products is defined in a variable
products = [
    { "id": 1, "name": "Product 1" },
    { "id": 2, "name": "Product 2" },
    { "id": 3, "name": "Product 3" },
]

# This route returns a JSON representation of the list of products
@app.route('/api/products')
def get_products():
    return jsonify(products)

# This route returns a JSON representation of a specific product
@app.route('/api/products/<int:product_id>')
def get_product(product_id):
    for p in products:
        if p['id'] == product_id:
            return jsonify(p)
    return jsonify({"message": "Product not found"}), 200

# This block of code sets the port number for the app to listen on
# If the PORT environment variable is set, its value is used, otherwise it defaults to 3000
# If the DEBUG environment variable is set, its value is used, otherwise it defaults to False
if __name__ == '__main__':
    debug = bool(os.environ.get("DEBUG", False))
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=debug)
