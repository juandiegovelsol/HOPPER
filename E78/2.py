import pandas as pd
import json
import matplotlib.pyplot as plt

# JSON con la información de los precios
json_data = '''
[
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
'''

# Convertir el JSON en un DataFrame
df = pd.read_json(json_data)

# Función para calcular el precio del kilo si el precio del cuarto o medio kilo es nulo
def calcular_precio_kilo(fila):
    if fila['precio_250g'] is None:
        return fila['precio_500g'] * 2
    elif fila['precio_500g'] is None:
        return fila['precio_250g'] * 4
    else:
        return (fila['precio_250g'] + fila['precio_500g']) / 2

# Aplicar la función a cada fila del DataFrame
df['precio_1000g'] = df.apply(calcular_precio_kilo, axis=1)

# Completar valores nulos en el DataFrame
df.fillna({'precio_250g': df['precio_500g'] / 2,
           'precio_500g': df['precio_1000g'] / 2,
           'precio_1000g': df['precio_250g'] * 4}, inplace=True)

# Calcular promedios
promedios = df[['precio_250g', 'precio_500g', 'precio_1000g']].mean()

# Crear una nueva fila con los promedios
df = pd.concat([df[['origen', 'tipo_lavado', 'precio_250g', 'precio_500g', 'precio_1000g']],
               pd.DataFrame([promedios], columns=['precio_250g', 'precio_500g', 'precio_1000g'])],
              axis=0)

# Guardar el DataFrame en un archivo CSV
df.to_csv('precios_cafes.csv', index=False)

# Leer el archivo CSV para generar el gráfico
df = pd.read_csv('precios_cafes.csv')

# Seleccionar las columnas relevantes para el gráfico
df_grafico = df[['origen', 'precio_250g', 'precio_500g', 'precio_1000g']]

# Ordenar los datos por origen
df_grafico = df_grafico.sort_values(by='origen')

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
df_grafico.plot(x='origen', y=['precio_250g', 'precio_500g', 'precio_1000g'], kind='bar', stacked=True, alpha=0.7)
plt.title('Precios del Café por Origen y Tamaño')
plt.xlabel('Origen')
plt.ylabel('Precio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()