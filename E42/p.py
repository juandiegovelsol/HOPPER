from datetime import datetime

date = datetime.strptime("2024-01-10", '%Y-%m-%d')
month = date.strftime('%B %Y')
print(month)