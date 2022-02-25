i = 1
products = []
n = int(input('Enter the number of products: '))
for _ in range(n):
    name = input('Enter the product name: ')
    price = input('Enter the product price: ')
    quantity = input('Enter the product quantity: ')
    measure = input('Enter the units of measurement: ')
    products.append((i, {'name': name, 'price': price, 'quantity': quantity, 'units': measure}))
    i += 1
print(products)
products_dict = {'name': [], 'price': [], 'quantity': [], 'measure': []}
for product in products:
    products_dict['name'].append(product[1]['name'])
    products_dict['price'].append(product[1]['price'])
    products_dict['quantity'].append(product[1]['quantity'])
    if product[1]['units'] not in products_dict['units']:
        products_dict['units'].append(product[1]['units'])
print(products_dict)