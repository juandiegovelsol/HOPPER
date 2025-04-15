import requests
import matplotlib.pyplot as plt

def graficar_temperatura():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 41.38,
        "longitude": 2.17,
        "start_date": "2025-03-10",
        "end_date": "2025-03-25",
        "daily": "temperature_2m_max",
        "timezone": "Europe/Madrid"
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    print(datos)

    fechas = datos["daily"]["time"]
    temperaturas = datos["temperature_2m_max"]

    plt.plot(fechas, temperaturas, marker='o')
    plt.xticks(rotation=45)
    plt.title("Temperatura máxima diaria en Barcelona")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.tight_layout()
    plt.show()

graficar_temperatura()