import json
import pandas as pd
from collections import defaultdict
from datetime import datetime, timedelta

# Función para cargar y procesar los datos JSON
def load_sales_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    sales = data['sales']

    sales_df = []

    for sale in sales:
        order_date = datetime.strptime(sale['orderDate'], '%Y-%m-%dT%H:%M:%S')
        if order_date.month in [4, 5, 6]:
            sales_df.append({
                'orderID': sale['orderID'],
                'orderDate': order_date,
                'status': sale['status'],
                'paymentMethod': sale['paymentMethod'],
                'bank': sale['bank'],
                'client': {
                    'clientID': sale['client']['clientID'],
                    'name': sale['client']['name'],
                    'email': sale['client']['email'],
                    'phone': sale['client']['phone'],
                    'address': sale['client']['address']
                },
                'products': sale['products'],
                'category': sale['products'][0]['product']['category']
            })

    return pd.DataFrame(sales_df)

# Función para calcular las ganancias brutas y el precio promedio por categoría
def calculate_category_statistics(df):
    category_stats = defaultdict(lambda: {
        'total_revenue': 0.0,
        'product_count': 0,
        'monthly_totals': defaultdict(lambda: {'total_revenue': 0.0, 'product_count': 0})
    })

    for _, row in df.iterrows():
        category = row['category']
        total_revenue = row['products'][0]['price'] * row['products'][0]['quantity']

        category_stats[category]['total_revenue'] += total_revenue
        category_stats[category]['product_count'] += row['products'][0]['quantity']

        month = row['orderDate'].month
        year = row['orderDate'].year
        category_stats[category]['monthly_totals'][(month, year)]['total_revenue'] += total_revenue
        category_stats[category]['monthly_totals'][(month, year)]['product_count'] += row['products'][0]['quantity']

    return category_stats

# Función para calcular el precio promedio de productos por categoría
def calculate_average_price_by_category(df):
    category_prices = defaultdict(list)

    for _, row in df.iterrows():
        category = row['category']
        price = row['products'][0]['price']
        category_prices[category].append(price)

    average_prices = {category: sum(prices) / len(prices) for category, prices in category_prices.items()}

    return average_prices

# Función para generar el informe
def generate_report(category_stats, average_prices):
    report = []

    # Calcular las dos categorías con mayores ganancias
    sorted_categories = sorted(category_stats.items(), key=lambda x: x[1]['total_revenue'], reverse=True)
    top_categories = sorted_categories[:2]

    for category, stats in top_categories:
        total_revenue = stats['total_revenue']
        product_count = stats['product_count']
        monthly_totals = stats['monthly_totals']

        # Calcular el precio promedio por mes
        average_price_by_month = {
            (month, year): avg_price
            for (month, year), avg_price in average_prices[category].items()
        }

        # Preparar la tabla de reporte
        report.append({
            'Category': category,
            'Total Revenue': total_revenue,
            'Product Count': product_count,
            'April Revenue': monthly_totals[(4, 2024)]['total_revenue'],
            'April Products': monthly_totals[(4, 2024)]['product_count'],
            'May Revenue': monthly_totals[(5, 2024)]['total_revenue'],
            'May Products': monthly_totals[(5, 2024)]['product_count'],
            'June Revenue': monthly_totals[(6, 2024)]['total_revenue'],
            'June Products': monthly_totals[(6, 2024)]['product_count'],
            'Average Price April': average_price_by_month[(4, 2024)],
            'Average Price May': average_price_by_month[(5, 2024)],
            'Average Price June': average_price_by_month[(6, 2024)]
        })

    return pd.DataFrame(report)

# Cargar y procesar los datos
file_path = 'sales_data.json'
df = load_sales_data(file_path)

# Calcular las estadísticas
category_stats = calculate_category_statistics(df)
average_prices = calculate_average_price_by_category(df)

# Generar el informe
report = generate_report(category_stats, average_prices)

# Mostrar el informe
print(report)
