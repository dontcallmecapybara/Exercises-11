import json
from solution02 import Load, Product, ShoppingCart


with open('barcodes.txt', 'r') as f:
    codes = f.read().split('\n')

load = Load()

item1 = Product(codes[0], 100)
print(item1)
item2 = Product(codes[1], 200)
print(item2)
item3 = Product(codes[2], 300)
print(item3)
item4 = Product(codes[3], 400)
print(item4)
item5 = Product(codes[4], 500)
print(item5)
print(Product.products)
cart = ShoppingCart()
cart.add_product(item1)
cart.add_product(item2)
cart.add_product(item3)
cart.add_product(item4)
cart.add_product(item5)
print(cart.view_cart())
cart.del_product(4)
print(cart.view_cart())
