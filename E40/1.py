import pandas as pd
import matplotlib.pyplot as plt
import json

def completar_precios(datos_json):
    # Convertir el JSON a un DataFrame
    df = pd.DataFrame(datos_json)
    
    # Completar los precios nulos en el DataFrame
    df['precio_250g'] = df['precio_250g'].fillna(df['precio_1000g'] / 4)
    df['precio_500g'] = df['precio_500g'].fillna(df['precio_1000g'] / 2)
    df['precio_1000g'] = df['precio_1000g'].fillna(df['precio_1000g'])
    
    # Calcular los promedios
    promedio_250g = df['precio_250g'].mean()
    promedio_500g = df['precio_500g'].mean()
    promedio_1000g = df['precio_1000g'].mean()
    
    # Crear una fila con los promedios
    promedio_row = pd.DataFrame([['', '', '', promedio_250g, promedio_500g, promedio_1000g]], columns=['origen', 'tipo_lavado', 'precio_250g', 'precio_500g', 'precio_1000g'])
    
    # Concatenar el DataFrame con la fila de promedios
    df_con_promedios = pd.concat([df, promedio_row])
    
    # Guardar el DataFrame en un archivo CSV
    df_con_promedios.to_csv('precios_cafes.csv', index=False)
    
    # Crear un gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_con_promedios['origen'], df_con_promedios['precio_250g'], label='Cuarto de kilo')
    plt.bar(df_con_promedios['origen'], df_con_promedios['precio_500g'], label='Medio kilo')
    plt.bar(df_con_promedios['origen'], df_con_promedios['precio_1000g'], label='Kilo')
    plt.xlabel('Origen')
    plt.ylabel('Precio')
    plt.title('Precios de Cafés por Origen')
    plt.legend()
    plt.show()

# JSON con la información de los cafés
datos_json = [
    {
        "origen": "Colombia",
        "tipo_lavado": "Lavado",
        "precio_250g": null,
        "precio_500g": null,
        "precio_1000g": 50.00
    },
    {
        "origen": "Etiopía",
        "tipo_lavado": "Natural",
        "precio_250g": 18.00,
        "precio_500g": 33.00,
        "precio_1000g": null
    },
    {
        "origen": "Brasil",
        "tipo_lavado": "Honey",
        "precio_250g": null,
        "precio_500g": 26.40,
        "precio_1000g": null
    },
    {
        "origen": "Costa Rica",
        "tipo_lavado": "Natural",
        "precio_250g": null,
        "precio_500g": 34.10,
        "precio_1000g": 62.00
    },
    {
        "origen": "Kenia",
        "tipo_lavado": "Lavado",
        "precio_250g": 17.10,
        "precio_500g": 31.00,
        "precio_1000g": null
    },
    {
        "origen": "Perú",
        "tipo_lavado": "Lavado",
        "precio_250g": null,
        "precio_500g": null,
        "precio_1000g": 58.00
    },
    {
        "origen": "Honduras",
        "tipo_lavado": "Natural",
        "precio_250g": 17.70,
        "precio_500g": null,
        "precio_1000g": 59.00
    },
    {
        "origen": "México",
        "tipo_lavado": "Honey",
        "precio_250g": 15.30,
        "precio_500g": 27.00,
        "precio_1000g": null
    },
    {
        "origen": "Nicaragua",
        "tipo_lavado": "Lavado",
        "precio_250g": null,
        "precio_500g": null,
        "precio_1000g": 54.00
    }
]

# Completar los precios y generar el CSV y gráfico
completar_precios(datos_json)