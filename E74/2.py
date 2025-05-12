import json

def add_travel_plan(travelPlans, destination, start_date, end_date, budget):
    expenses = []
    while True:
        description = input("Ingrese la descripción del gasto (o 'done' para finalizar): ")
        if description.lower() == 'done':
            break
        try:
            amount = float(input("Ingrese el monto del gasto: "))
            expenses.append({"description": description, "amount": amount})
        except ValueError:
            print("Formato de entrada inválido. Por favor, ingrese un número.")

    travel_plan = {
        "destination": destination,
        "startDate": start_date,
        "endDate": end_date,
        "budget": budget,
        "expenses": expenses
    }
    travelPlans.append(travel_plan)
    print(f"Plan de viaje agregado para {destination}.")

def calculate_total_expenses(travelPlans, destination):
    for plan in travelPlans:
        if plan["destination"] == destination:
            total_expenses = sum(expense["amount"] for expense in plan["expenses"])
            remaining_budget = plan["budget"] - total_expenses
            return {
                "totalExpenses": total_expenses,
                "remainingBudget": remaining_budget
            }
    return {"message": "No se encontraron gastos para este viaje"}

def generate_json_summary(travelPlans):
    json_summary = []
    for plan in travelPlans:
        summary = {
            "destination": plan["destination"],
            "totalExpenses": sum(expense["amount"] for expense in plan["expenses"]),
            "remainingBudget": plan["budget"] - sum(expense["amount"] for expense in plan["expenses"])
        }
        json_summary.append(summary)
    return json.dumps(json_summary, indent=4)

if __name__ == "__main__":
    travelPlans = []
    while True:
        print("\nPlanificar un nuevo viaje o revisar planes existentes:")
        print("1. Agregar un nuevo plan de viaje")
        print("2. Generar resumen de viajes")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            destination = input("Ingrese el destino: ")
            start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            end_date = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")
            budget = float(input("Ingrese el presupuesto: "))
            add_travel_plan(travelPlans, destination, start_date, end_date, budget)
        elif choice == '2':
            if not travelPlans:
                print("No hay planes de viaje disponibles.")
            else:
                destination = input("Ingrese el destino para el resumen (o 'all' para todos los destinos): ")
                summary = calculate_total_expenses(travelPlans, destination)
                if isinstance(summary, dict):
                    print(json.dumps(summary, indent=4))
                else:
                    print(summary)
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")