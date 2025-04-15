import json

def add_travel_plan(travelPlans, destination, start_date, end_date, budget, expenses=None):
    if expenses is None:
        expenses = []
    
    travel_plan = {
        "destination": destination,
        "startDate": start_date,
        "endDate": end_date,
        "budget": budget,
        "expenses": expenses
    }
    
    travelPlans.append(travel_plan)

def calculate_total_expenses(travelPlans, destination):
    total_expenses = 0
    for plan in travelPlans:
        if plan["destination"] == destination:
            total_expenses += sum(expense["amount"] for expense in plan["expenses"])
            break
    return total_expenses

def generate_expenses_report(travelPlans, destination):
    total_expenses = calculate_total_expenses(travelPlans, destination)
    
    if total_expenses == 0:
        return {"message": "No se encontraron gastos para este viaje"}
    
    remaining_budget = travelPlans[0]["budget"] - total_expenses
    report = {
        "totalExpenses": total_expenses,
        "remainingBudget": remaining_budget
    }
    
    return json.dumps(report, indent=4)

# Ejemplo de uso
travelPlans = [
    {
        "destination": "Paris",
        "startDate": "2024-03-01",
        "endDate": "2024-03-10",
        "budget": 1500,
        "expenses": [
            {"description": "Flight", "amount": 600},
            {"description": "Hotel", "amount": 400},
            {"description": "Food", "amount": 200}
        ]
    },
    {
        "destination": "Tokyo",
        "startDate": "2024-04-05",
        "endDate": "2024-04-12",
        "budget": 2000,
        "expenses": []
    }
]

# Añadir un nuevo plan de viaje
add_travel_plan(travelPlans, "New York", "2024-05-15", "2024-05-25", 1800, [
            {"description": "Flight", "amount": 100},
            {"description": "Hotel", "amount": 400},
            {"description": "Food", "amount": 200}
        ])

# Generar informe de gastos para París
report = generate_expenses_report(travelPlans, "Paris")
print(report)

print(generate_expenses_report(travelPlans, "Tokio"))
print(generate_expenses_report(travelPlans, "New York"))