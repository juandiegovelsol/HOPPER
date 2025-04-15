import json
from collections import defaultdict
from datetime import datetime

def parse_date(date_str):
    """Convierte una cadena de fecha en un objeto datetime."""
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

def calculate_total_sales(sales):
    """Calcula las ventas totales y las ganancias brutas por categoría."""
    total_sales = 0
    category_sales = defaultdict(float)
    category_products = defaultdict(int)

    for sale in sales:
        order_date = parse_date(sale['orderDate'])
        order_month = order_date.month
        order_year = order_date.year

        total_sales += sale['totalAmount']

        for product in sale['products']:
            category = product['product']['category']
            category_sales[category] += product['price']
            category_products[category] += product['quantity']

    return total_sales, category_sales, category_products

def get_average_price(category_sales, category_products):
    """Calcula el precio promedio por producto en una categoría."""
    total_sales_in_category = sum(category_sales.values())
    total_products_in_category = sum(category_products.values())

    if total_products_in_category == 0:
        return 0

    return total_sales_in_category / total_products_in_category

def analyze_sales(json_data):
    """Analiza las ventas y calcula las ganancias brutas por categoría."""
    try:
        sales = json.loads(json_data)
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el JSON.")
        return

    total_sales, category_sales, category_products = calculate_total_sales(sales['sales'])

    # Obtener las categorías con las mayores ganancias brutas
    top_categories = sorted(category_sales.items(), key=lambda x: x[1], reverse=True)[:2]

    # Calcular el precio promedio para cada categoría
    average_prices = {category: get_average_price(category_sales, category_products) for category in category_sales}

    # Calcular las ventas por mes para cada categoría
    monthly_sales = defaultdict(lambda: defaultdict(float))
    monthly_products = defaultdict(lambda: defaultdict(int))

    for sale in sales['sales']:
        order_date = parse_date(sale['orderDate'])
        order_month = order_date.month
        order_year = order_date.year

        category = sale['products'][0]['product']['category']
        monthly_sales[category][order_month] += sale['totalAmount']
        monthly_products[category][order_month] += sale['products'][0]['quantity']

    # Preparar los datos para la tabla
    table_data = []
    for category, (_, total_sales) in top_categories:
        total_products = sum(monthly_products[category].values())
        total_sales_by_month = sum(monthly_sales[category].values())

        # Calcular el precio promedio para el mes de abril
        average_price_april = get_average_price(category_sales, category_products) if category in average_prices else 0
        # Calcular el precio promedio para el mes de mayo
        average_price_mayo = get_average_price(category_sales, category_products) if category in average_prices else 0
        # Calcular el precio promedio para el mes de junio
        average_price_junio = get_average_price(category_sales, category_products) if category in average_prices else 0

        table_data.append([
            category,
            average_price_april,
            average_price_mayo,
            average_price_junio,
            total_sales_by_month,
            total_products,
            total_sales
        ])

    # Imprimir la tabla
    print("\nResumen de Ventas por Categoría (2do Trimestre 2024):")
    print("=" * 60)
    print(f"Categoría | Precio Promedio Abril | Precio Promedio Mayo | Precio Promedio Junio | Ventas Totales Mês | Total de Productos | Ventas Totales")
    print("=" * 60)
    for row in table_data:
        print(f"{row[0]:<15} | {row[1]:.2f} | {row[2]:.2f} | {row[3]:.2f} | {row[4]:<15} | {row[5]:<15} | {row[6]:<15}")

# Ejemplo de uso
json_data = '''
{
  "sales": [
    {
      "orderID": "ORD123456",
      "orderDate": "2024-07-27T14:35:45",
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
'''

analyze_sales(json_data)