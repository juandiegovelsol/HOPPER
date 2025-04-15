import json

travelPlans = []

def add_travel_plan(destination, start_date, end_date, budget, expenses):
    """
    Agrega un plan de viaje a la lista de viajes.
    
    Parámetros:
    - destination (str): Destino del viaje.
    - start_date (str): Fecha de inicio del viaje en formato 'YYYY-MM-DD'.
    - end_date (str): Fecha de finalización del viaje en formato 'YYYY-MM-DD'.
    - budget (float): Presupuesto total del viaje.
    - expenses (list): Lista de diccionarios con la descripción y el monto de los gastos.
    """
    travelPlans.append({
        "destination": destination,
        "startDate": start_date,
        "endDate": end_date,
        "budget": budget,
        "expenses": expenses
    })

def calculate_expenses(destination):
    """
    Calcula los gastos totales de un viaje según el destino.
    
    Parámetros:
    - destination (str): Destino del viaje.
    
    Retorna:
    - dict: Un diccionario con los gastos totales y el presupuesto restante.
    - str: Mensaje si no se encontraron gastos.
    """
    total_expenses = 0
    for plan in travelPlans:
        if plan["destination"] == destination:
            total_expenses += sum(expense["amount"] for expense in plan["expenses"])
            remaining_budget = plan["budget"] - total_expenses
            return {
                "totalExpenses": total_expenses,
                "remainingBudget": remaining_budget
            }
    return "No se encontraron gastos para este viaje"

def generate_expenses_json(destination):
    """
    Genera un JSON con los gastos totales y el presupuesto restante para un viaje.
    
    Parámetros:
    - destination (str): Destino del viaje.
    
    Retorna:
    - str: Un JSON bien estructurado o un mensaje de error.
    """
    result = calculate_expenses(destination)
    if isinstance(result, dict):
        return json.dumps(result, indent=4)
    else:
        return result

# Ejemplo de uso
add_travel_plan("Paris", "2024-03-01", "2024-03-10", 1500, [
    {"description": "Flight", "amount": 600},
    {"description": "Hotel", "amount": 400},
    {"description": "Food", "amount": 100}
])

add_travel_plan("Tokyo", "2024-04-05", "2024-04-12", 2000, [])

# Generar JSON para París
print(generate_expenses_json("Paris"))

# Generar JSON para Tokio
print(generate_expenses_json("Tokyo"))