import json
from datetime import datetime

# Lista para almacenar los registros de entrenamiento
workoutLog = []

def add_workout(date, exercise, duration, caloriesBurned, notes):
    """
    Agrega un nuevo registro de entrenamiento a la lista.
    """
    workout = {
        "date": date,
        "exercise": exercise,
        "duration": duration,
        "caloriesBurned": caloriesBurned,
        "notes": notes
    }
    workoutLog.append(workout)

def calculate_total_for_date_range(start_date, end_date):
    """
    Calcula la duración total y las calorías totales quemadas para un rango de fechas.
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    total_duration = 0
    total_calories = 0
    summary = []
    
    for workout in workoutLog:
        workout_date = datetime.strptime(workout["date"], "%Y-%m-%d")
        if start_date <= workout_date <= end_date:
            total_duration += workout["duration"]
            total_calories += workout["caloriesBurned"]
            summary.append(workout)
    
    return total_duration, total_calories, summary

def get_workout_summary(start_date, end_date):
    """
    Genera un resumen en formato JSON de los entrenamientos para un rango de fechas.
    """
    total_duration, total_calories, summary = calculate_total_for_date_range(start_date, end_date)
    
    if not summary:
        return {
            "message": "No se encontraron entrenamientos para este rango de fechas"
        }
    
    return {
        "totalDuration": total_duration,
        "totalCaloriesBurned": total_calories,
        "summary": summary
    }

# Ejemplo de uso
add_workout("2024-01-10", "Running", 30, 300, "Felt great")
add_workout("2024-01-12", "Cycling", 45, 400, "Challenging ride")
add_workout("2024-01-15", "Yoga", 60, 200, "Relaxing session")

resultado = get_workout_summary("2024-01-17", "2024-01-18")
print(json.dumps(resultado, indent=4))