import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def graficar_temperatura():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 41.38,
        "longitude": 2.17,
        "start_date": "2025-03-10",
        "end_date": "2025-03-25",
        "daily": "temperature_2m_max_forecast",  # Corrección aquí
        "timezone": "Europe/Madrid"
    }

    respuesta = requests.get(url, params=params)
    print(respuesta)
    datos = respuesta.json()

    # Crear una lista de fechas
    start_date = datetime.strptime(params["start_date"], "%Y-%m-%d")
    fechas = [start_date + timedelta(days=i) for i in range((datetime.strptime(params["end_date"], "%Y-%m-%d") - start_date).days + 1)]
    
    # Extraer las temperaturas máximas
    temperaturas = datos["daily"]["temperature_2m_max_forecast"]

    # Graficar los datos
    plt.plot(fechas, temperaturas, marker='o')
    plt.xticks(rotation=45)
    plt.title("Temperatura máxima diaria en Barcelona")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.tight_layout()
    plt.show()

graficar_temperatura()