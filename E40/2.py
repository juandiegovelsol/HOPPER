import pandas as pd
import json
import matplotlib.pyplot as plt

def completar_precios(json_data):
    # Convertir JSON a DataFrame
    df = pd.DataFrame(json_data)

    # Calcular precios faltantes
    df['precio_250g'] = df['precio_250g'].fillna(df['precio_1000g'] * 0.025)
    df['precio_500g'] = df['precio_500g'].fillna(df['precio_1000g'] * 0.05)
    df['precio_1000g'] = df['precio_1000g'].fillna(df['precio_250g'] * 4 + df['precio_500g'] * 2)

    # Calcular precios promedio
    promedio_df = df.groupby(['origen', 'tipo_lavado'])[['precio_250g', 'precio_500g', 'precio_1000g']].mean().reset_index()
    promedio_df['precio_250g_promedio'] = promedio_df['precio_250g'] * 4
    promedio_df['precio_500g_promedio'] = promedio_df['precio_500g'] * 2
    promedio_df['precio_1000g_promedio'] = promedio_df['precio_1000g']

    # Agregar fila de promedios
    df = pd.concat([df, promedio_df], ignore_index=True)

    return df

def guardar_csv(df, nombre_archivo):
    # Guardar DataFrame como CSV
    df.to_csv(nombre_archivo, index=False)

def crear_grafico(nombre_archivo):
    # Leer CSV
    df = pd.read_csv(nombre_archivo)

    # Excluir la fila final de promedios
    df_sin_promedios = df.drop(df.tail(1).index)

    # Crear gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(df_sin_promedios['origen'], df_sin_promedios['precio_250g'], label='250g')
    plt.bar(df_sin_promedios['origen'], df_sin_promedios['precio_500g'], label='500g')
    plt.bar(df_sin_promedios['origen'], df_sin_promedios['precio_1000g'], label='1000g')
    plt.xlabel('Origen')
    plt.ylabel('Precio')
    plt.title('Precios de Café por Origen')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('precios_cafe.png')
    plt.show()

# Datos JSON
json_data = [
    {"origen": "Colombia", "tipo_lavado": "Lavado", "precio_250g": null, "precio_500g": null, "precio_1000g": 50.00},
    {"origen": "Etiopía", "tipo_lavado": "Natural", "precio_250g": 18.00, "precio_500g": 33.00, "precio_1000g": null},
    {"origen": "Brasil", "tipo_lavado": "Honey", "precio_250g": null, "precio_500g": 26.40, "precio_1000g": null},
    {"origen": "Costa Rica", "tipo_lavado": "Natural", "precio_250g": null, "precio_500g": 34.10, "precio_1000g": 62.00},
    {"origen": "Kenia", "tipo_lavado": "Lavado", "precio_250g": 17.10, "precio_500g": 31.00, "precio_1000g": null},
    {"origen": "Perú", "tipo_lavado": "Lavado", "precio_250g": null, "precio_500g": null, "precio_1000g": 58.00},
    {"origen": "Honduras", "tipo_lavado": "Natural", "precio_250g": 17.70, "precio_500g": null, "precio_1000g": 59.00},
    {"origen": "México", "tipo_lavado": "Honey", "precio_250g": 15.30, "precio_500g": 27.00, "precio_1000g": null},
    {"origen": "Nicaragua", "tipo_lavado": "Lavado", "precio_250g": null, "precio_500g": null, "precio_1000g": 54.00}
]

# Completar precios y guardar en CSV
df = completar_precios(json_data)
guardar_csv(df, 'precios_cafe.csv')

# Crear gráfico
crear_grafico('precios_cafe.csv')
