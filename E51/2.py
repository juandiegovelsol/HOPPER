import json
from collections import defaultdict
from datetime import datetime, timedelta

def calculate_category_statistics(data):
    sales = data.get("sales", [])
    category_data = defaultdict(lambda: {"total_sales": 0, "total_revenue": 0, "product_count": defaultdict(int), "months": defaultdict(lambda: {"count": 0, "total_revenue": 0})})
    
    for sale in sales:
        order_date = datetime.strptime(sale["orderDate"], "%Y-%m-%dT%H:%M:%S")
        month = order_date.strftime("%Y-%m")
        
        for product in sale["products"]:
            product_category = product["product"]["category"]
            category_data[product_category]["total_sales"] += 1
            category_data[product_category]["total_revenue"] += product["price"] * product["quantity"]
            category_data[product_category]["product_count"][month] += product["quantity"]
            category_data[product_category]["months"][month]["count"] += 1
            category_data[product_category]["months"][month]["total_revenue"] += product["price"] * product["quantity"]
    
    return category_data

def find_top_categories(category_data, top_n=2):
    category_revenue = {category: data["total_revenue"] for category, data in category_data.items()}
    sorted_categories = sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)
    top_categories = sorted_categories[:top_n]
    
    return top_categories, category_data

def calculate_average_price_and_monthly_stats(category_data):
    results = []
    for category, data in category_data.items():
        total_products = sum(data["product_count"].values())
        monthly_stats = []
        
        for month, stats in data["months"].items():
            avg_price = stats["total_revenue"] / stats["count"]
            monthly_stats.append({
                "month": month,
                "average_price": avg_price,
                "product_count": stats["product_count"],
                "total_revenue": stats["total_revenue"]
            })
        
        results.append({
            "category": category,
            "total_sales": data["total_sales"],
            "total_revenue": data["total_revenue"],
            "average_price": total_products > 0 and data["total_revenue"] / total_products or 0,
            "monthly_stats": monthly_stats
        })
    
    return results

def process_sales_data(json_data):
    try:
        data = json.loads(json_data)
        category_data = calculate_category_statistics(data)
        top_categories, category_data = find_top_categories(category_data)
        results = calculate_average_price_and_monthly_stats(category_data)
        
        return results, top_categories
    except json.JSONDecodeError:
        print("Error: Invalid JSON data")
        return [], []
    except Exception as e:
        print(f"Error processing data: {e}")
        return [], []

def main():
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
    
    results, top_categories = process_sales_data(json_data)
    
    if results:
        print("\nCategory Statistics:")
        for result in results:
            print(f"Category: {result['category']}")
            print(f"  Total Sales: {result['total_sales']}")
            print(f"  Total Revenue: ${result['total_revenue']:.2f}")
            print(f"  Average Price: ${result['average_price']:.2f}")
            print("  Monthly Stats:")
            for month_stat in result['monthly_stats']:
                print(f"    Month: {month_stat['month']}")
                print(f"      Average Price: ${month_stat['average_price']:.2f}")
                print(f"      Product Count: {month_stat['product_count']}")
                print(f"      Total Revenue: ${month_stat['total_revenue']:.2f}")
            print("-" * 40)
    
    if top_categories:
        print("\nTop Categories by Revenue:")
        for category, revenue in top_categories:
            print(f"  Category: {category}")
            print(f"    Total Revenue: ${revenue[0]['total_revenue']:.2f}")
    
if __name__ == "__main__":
    main()