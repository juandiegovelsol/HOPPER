import requests
import matplotlib.pyplot as plt
from datetime import datetime

def graficar_lluvia_diaria():
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    # Parámetros necesarios para la solicitud
    params = {
        "latitude": 40.42,
        "longitude": -3.70,
        "start_date": "2024-08-01",
        "end_date": "2024-09-30",
        "timezone": "auto",
        "daily": "rain_sum"  # Solicitar específicamente la lluvia acumulada
    }

    # Realizar la solicitud a la API
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()

    # Verificar que la clave 'rain_sum' exista en los datos diarios
    if 'rain_sum' not in datos['daily']:
        print("Error: La clave 'rain_sum' no está presente en los datos. Revisa los parámetros de la solicitud.")
        return
    
    # Extraer las fechas y convertir el formato a datetime
    fechas = [datetime.fromisoformat(fecha) for fecha in datos['daily']['time']]
    lluvia = datos['daily']['rain_sum']

    # Configurar el gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(fechas, lluvia, color='skyblue')
    plt.title("Precipitación diaria en Madrid (mm)")
    plt.xlabel("Fecha")
    plt.ylabel("Lluvia acumulada (mm)")
    
    # Rotar las etiquetas del eje X para evitar superposición
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ajustar el layout para que las etiquetas no se salgan
    plt.show()

# Llamar a la función para graficar los datos de lluvia
graficar_lluvia_diaria()