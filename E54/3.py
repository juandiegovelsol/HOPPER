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

def calculateTotalExpenses(travel_plans, destination):
    total_expenses = 0
    for plan in travel_plans:
        if plan["destination"] == destination:
            total_expenses += sum(expense["amount"] for expense in plan["expenses"])
    return total_expenses

def generateExpenseReport(travel_plans, destination):
    total_expenses = calculateTotalExpenses(travel_plans, destination)
    remaining_budget = travel_plans[0]["budget"] - total_expenses
    return {
        "totalExpenses": total_expenses,
        "remainingBudget": remaining_budget
    }

def getExpenseReport(destination):
    report = generateExpenseReport(travel_plans, destination)
    if "totalExpenses" in report:
        return report
    else:
        return {
            "message": "No se encontraron gastos para este viaje"
        }

# Ejemplo de uso
destination = "Paris"
report = getExpenseReport(destination)
print(report)

destination = "Tokyo"
report = getExpenseReport(destination)
print(report)