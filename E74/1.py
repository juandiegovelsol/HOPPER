
def add_travel_plan(travelPlans, destination, start_date, end_date, budget, expenses):
    travel_plan = {
        "destination": destination,
        "startDate": start_date,
        "endDate": end_date,
        "budget": budget,
        "expenses": expenses
    }
    travelPlans.append(travel_plan)

def calculate_total_expenses(travelPlans, destination):
    for plan in travelPlans:
        if plan["destination"] == destination:
            return sum(exp["amount"] for exp in plan["expenses"])
    return None

def generate_expense_report(travelPlans, destination):
    total_expenses = calculate_total_expenses(travelPlans, destination)
    if total_expenses is None:
        return {"message": "No se encontraron gastos para este viaje"}
    remaining_budget = travelPlans[0]["budget"] - total_expenses
    return {
        "totalExpenses": total_expenses,
        "remainingBudget": remaining_budget
    }

def main():
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

    # Add a new travel plan
    add_travel_plan(travelPlans, "Sydney", "2024-05-15", "2024-05-25", 1800, [
        {"description": "Flight", "amount": 800},
        {"description": "Hotel", "amount": 500},
        {"description": "Food", "amount": 300}
    ])

    # Calculate and print the expense report for "Paris"
    report = generate_expense_report(travelPlans, "Paris")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()