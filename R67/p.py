import requests
import matplotlib.pyplot as plt

def graficar_lluvia_diaria():
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 40.42,
        "longitude": -3.70,
        "daily": "rain_sum",
        "start_date": "2024-08-01",
        "end_date": "2024-09-30",
        "timezone": "auto"
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    print(datos.keys())
    print(datos)
    print(datos["daily"].keys())

    fechas = datos["daily"]["time"]
    lluvia = datos["rain_sum"]

    plt.figure(figsize=(12, 6))
    plt.bar(fechas, lluvia, color='skyblue')
    plt.title("Precipitación diaria en Madrid (mm)")
    plt.xlabel("Fecha")
    plt.ylabel("Lluvia acumulada (mm)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

graficar_lluvia_diaria()