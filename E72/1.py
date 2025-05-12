import json
from datetime import datetime

workoutLog = [
    {"date": "2024-01-10", "exercise": "Running", "duration": 30, "caloriesBurned": 300, "notes": "Felt great"},
    {"date": "2024-01-12", "exercise": "Cycling", "duration": 45, "caloriesBurned": 400, "notes": "Challenging ride"},
    {"date": "2024-01-15", "exercise": "Yoga", "duration": 60, "caloriesBurned": 200, "notes": "Relaxing session"}
]

def add_workout(date, exercise, duration, caloriesBurned, notes):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        workoutLog.append({"date": date, "exercise": exercise, "duration": duration, "caloriesBurned": caloriesBurned, "notes": notes})
        print("Sesión de entrenamiento agregada exitosamente.")
    except ValueError:
        print(f"Fecha inválida: {date}. Utilice el formato YYYY-MM-DD.")

def calculate_total_duration_and_calories(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        total_duration = sum(workout["duration"] for workout in workoutLog if start_date <= datetime.strptime(workout["date"], "%Y-%m-%d") <= end_date)
        total_calories = sum(workout["caloriesBurned"] for workout in workoutLog if start_date <= datetime.strptime(workout["date"], "%Y-%m-%d") <= end_date)

        summary = [workout for workout in workoutLog if start_date <= datetime.strptime(workout["date"], "%Y-%m-%d") <= end_date]

        return {"totalDuration": total_duration, "totalCaloriesBurned": total_calories, "summary": summary}
    except ValueError:
        print("Formato de fecha inválido. Utilice YYYY-MM-DD.")
        return None

def generate_workout_summary(start_date, end_date):
    summary = calculate_total_duration_and_calories(start_date, end_date)
    if summary:
        return json.dumps(summary, indent=4)
    else:
        return json.dumps({"message": "No se encontraron entrenamientos para este rango de fechas"}, indent=4)

# Ejemplo de uso:
add_workout("2024-02-01", "Swimming", 60, 450, "Felt refreshed")
print(generate_workout_summary("2024-01-16", "2024-01-17"))