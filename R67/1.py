import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def graficar_lluvia_diaria():
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 40.42,
        "longitude": -3.70,
        "start_date": "2024-08-01",
        "end_date": "2024-09-30",
        "timezone": "auto"
    }

    # Realizar la solicitud a la API
    try:
        respuesta = requests.get(url, params=params)
        respuesta.raise_for_status()  # Levanta una excepción si la solicitud no fue exitosa
        datos = respuesta.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return

    # Verificar que los datos de lluvia estén presentes
    if "daily" not in datos or "rain_sum" not in datos["daily"]:
        print("Error: Los datos de lluvia no están disponibles.")
        return

    # Extraer las fechas y los datos de lluvia
    fechas_str = datos["daily"]["time"]
    lluvia = datos["daily"]["rain_sum"]
    
    # Convertir las fechas de string a objetos datetime
    fechas = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas_str]

    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(fechas, lluvia, color='skyblue')
    plt.title("Precipitación diaria en Madrid (mm)")
    plt.xlabel("Fecha")
    plt.ylabel("Lluvia acumulada (mm)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

graficar_lluvia_diaria()