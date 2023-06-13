# Gym Clothing E-commerce Application

# Function to calculate the total price of an item
def calculate_item_total(price, quantity):
    return price * quantity

# User details
user_name = input("Enter your name: ")
user_email = input("Enter your email address: ")

# Cart details
cart_items = []  # List to store items in the cart
cart_total = 0.0  # Float to keep track of the total cart value

# Repetition structure to allow multiple items to be added to the cart
while True:
    # Product details
    product_name = input("Enter the product name (or 'q' to quit): ")
    if product_name == 'q':
        break

    product_price = float(input("Enter the product price: "))
    product_quantity = int(input("Enter the product quantity: "))

    # Add product to the cart
    item_total = calculate_item_total(product_price, product_quantity)
    cart_items.append((product_name, product_price, product_quantity, item_total))
    cart_total += item_total

# Decision structure to determine if the cart is empty or not
if len(cart_items) == 0:
    print("Cart is empty.")
else:
    # Display cart details
    print("---------- Cart Summary ----------")
    print(f"Customer: {user_name} ({user_email})")
    print("Items:")
    for index, item in enumerate(cart_items, start=1):
        name, price, quantity, item_total = item
        print(f"{index}. {name}: ${price} x {quantity} = ${item_total}")
    print(f"Total: ${cart_total}")
