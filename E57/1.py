import json
from collections import defaultdict
from tabulate import tabulate

# Datos de ejemplo
data = {
    "sales": [
        {
            "orderID": "ORD123456",
            "orderDate": "2024-04-27T14:35:45",
            "status": "complete",
            "paymentMethod": "credit_card",
            "bank": "Banco Nación",
            "client": {
                "clientID": "CL789012",
                "name": "Juan Perez",
                "email": "juan.perez@example.com",
                "phone": "+1234567890",
                "address": {
                    "street": "123 Main St",
                    "city": "Anytown",
                    "state": "CA",
                    "zip": "12345",
                    "country": "USA"
                }
            },
            "products": [
                {
                    "productID": "PROD123",
                    "quantity": 2,
                    "price": "$450.99",
                    "lastPriceModificationDate": "2024-05-21T17:39:45",
                    "product": {
                        "productID": "PROD123",
                        "name": "Wireless Headphones",
                        "brand": "SoundBrand",
                        "category": "Electronics",
                        "size": "N/A",
                        "weight": "0.5 kg",
                        "color": "Black"
                    }
                }
            ]
        }
    ]
}

# Diccionario para almacenar los datos por categoría
category_data = defaultdict(lambda: {'total_gross': 0, 'products': []})

# Procesar ventas
for sale in data['sales']:
    order_date = sale['orderDate']
    if '2024-Q2' in order_date:
        month = order_date.split('-')[1]
        category = next(product['product']['category'] for product in sale['products'] if product['product']['category'])
        
        # Acumular datos por categoría y mes
        for product in sale['products']:
            print(product)
            category_data[category]['total_gross'] += float(product['price'].replace('$', '').replace(',', '')) * product['quantity]']
            category_data[category]['products'].append(
                {
                    'productID': product['product']['productID'],
                    'quantity': product['quantity'],
                    'price': product['price'],
                    'lastPriceModificationDate': product['lastPriceModificationDate']
                }
            )

# Calcular promedios y preparar datos para la tabla
result = []
total_gross_by_category_month = defaultdict(lambda: {'total_gross': 0, 'products_count': 0})

for category, info in category_data.items():
    total_gross = info['total_gross']
    products = info['products']
    
    # Calcular el precio promedio por producto en este trimestre
    avg_price = total_gross / len(products) if products else 0
    
    # Acumular ventas totales por categoría y mes para cada categoría
    for product in products:
        month = order_date.split('-')[1]
        total_gross_by_category_month[category]['total_gross'] += float(product['price'].replace('$', '').replace(',', '')) * product['quantity']
        total_gross_by_category_month[category]['products_count'] += product['quantity']

    # Preparar datos para la tabla
    for month in ['April', 'May', 'June']:
        mg = total_gross_by_category_month[category]['total_gross']
        pc = total_gross_by_category_month[category]['products_count']
        result.append(
            [
                category,
                f"{avg_price:.2f}",
                len(products),
                f"{mg:.2f}",
                f"{pc}"
            ]
        )
        total_gross_by_category_month[category]['total_gross'] = 0
        total_gross_by_category_month[category]['products_count'] = 0

# Mostrar resultados en formato de tabla
print(tabulate(result, headers=["Category", "Average Price", "Products Count", "Total Gross April", "Total Products April"], tablefmt="grid"))