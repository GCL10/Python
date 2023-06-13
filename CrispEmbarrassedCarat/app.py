from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate the total price of an item
def calculate_item_total(price, quantity):
    return price * quantity

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']

        cart_items = []
        cart_total = 0.0

        product_name = request.form['product_name']
        product_price = float(request.form['product_price'])
        product_quantity = int(request.form['product_quantity'])

        item_total = calculate_item_total(product_price, product_quantity)
        cart_items.append((product_name, product_price, product_quantity, item_total))
        cart_total += item_total

        return render_template('index.html', user_name=user_name, user_email=user_email, cart_items=cart_items, cart_total=cart_total)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)