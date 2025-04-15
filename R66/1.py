import requests
import matplotlib.pyplot as plt
import datetime

def graficar_temperatura():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 41.38,
        "longitude": 2.17,
        "start_date": "2025-03-10",
        "end_date": "2025-03-25",
        "hourly": "temperature_2m",
        "timezone": "Europe/Madrid"
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    print(datos)
    fechas = []
    temperaturas_max = []

    # Recorrer los datos horarios y calcular la temperatura máxima diaria
    for i in range(0, len(datos["hourly"]["time"]), 24):
        tiempo = datos["hourly"]["time"][i]
        fecha = datetime.datetime.strptime(tiempo, "%Y-%m-%dT%H:%M")
        temperaturas_hora = datos["hourly"]["temperature_2m"][i:i+24]
        temperatura_max = max(temperaturas_hora)

        fechas.append(fecha)
        temperaturas_max.append(temperatura_max)

    plt.plot(fechas, temperaturas_max, marker='o')
    plt.xticks(rotation=45)
    plt.title("Temperatura máxima diaria en Barcelona")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.tight_layout()
    plt.show()

graficar_temperatura()