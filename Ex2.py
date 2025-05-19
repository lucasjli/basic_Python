def calculate_total(cart):
    total = 0
    for product in cart:
        total += product['price'] * product['quantity']
    #total = sum(item['price'] * item['quantity'] for item in cart)
    return total


cart = [{'name': 'banana', 'price': 0.99, 'quantity': 5}, {'name': 'milk', 'price': 1.50, 'quantity': 2}]

print(calculate_total(cart))