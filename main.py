from flask import Flask, request, render_template, redirect, url_for
from threading import Lock

app = Flask(__name__)

# In-memory data store for products and a lock for thread safety
products = {}
lock = Lock()

# Homepage with product creation and management forms
@app.route('/')
def api_home():
    with lock:
        all_products = list(products.values())
    return render_template('index.html', products=all_products)

# Create a product (POST)
@app.route('/products/create', methods=['POST'])
def create_product():
    name = request.form.get('name')
    description = request.form.get('description')
    price = float(request.form.get('price', 0.0))
    
    with lock:
        if name in products:
            return "Product with this name already exists", 400
        products[name] = {
            'name': name,
            'description': description,
            'price': price
        }

    return redirect(url_for('api_home'))

# Get a product by name (POST)
@app.route('/products/get', methods=['POST'])
def get_product():
    name = request.form.get('name')

    with lock:
        product = products.get(name)
        if product is None:
            return "Product not found", 404
    
    return f"Product found: {product}"

# Update a product by name (POST)
@app.route('/products/update', methods=['POST'])
def update_product():
    name = request.form.get('name')
    description = request.form.get('description')
    price = float(request.form.get('price', 0.0))

    with lock:
        product = products.get(name)
        if product is None:
            return "Product not found", 404

        product['description'] = description
        product['price'] = price

    return redirect(url_for('api_home'))

# Delete a product by name (POST)
@app.route('/products/delete', methods=['POST'])
def delete_product():
    name = request.form.get('name')

    with lock:
        if name in products:
            del products[name]
        else:
            return "Product not found", 404

    return redirect(url_for('api_home'))

if __name__ == '__main__':
    app.run(debug=True)
