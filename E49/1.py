import pandas as pd
import json
import matplotlib.pyplot as plt

# Datos en formato JSON
data = [
    {
        "origen": "Colombia",
        "tipo_lavado": "Lavado",
        "precio_250g": None,
        "precio_500g": None,
        "precio_1000g": 50.00
    },
    {
        "origen": "Etiopía",
        "tipo_lavado": "Natural",
        "precio_250g": 18.00,
        "precio_500g": 33.00,
        "precio_1000g": None
    },
    {
        "origen": "Brasil",
        "tipo_lavado": "Honey",
        "precio_250g": None,
        "precio_500g": 26.40,
        "precio_1000g": None
    },
    {
        "origen": "Costa Rica",
        "tipo_lavado": "Natural",
        "precio_250g": None,
        "precio_500g": 34.10,
        "precio_1000g": 62.00
    },
    {
        "origen": "Kenia",
        "tipo_lavado": "Lavado",
        "precio_250g": 17.10,
        "precio_500g": 31.00,
        "precio_1000g": None
    },
    {
        "origen": "Perú",
        "tipo_lavado": "Lavado",
        "precio_250g": None,
        "precio_500g": None,
        "precio_1000g": 58.00
    },
    {
        "origen": "Honduras",
        "tipo_lavado": "Natural",
        "precio_250g": 17.70,
        "precio_500g": None,
        "precio_1000g": 59.00
    },
    {
        "origen": "México",
        "tipo_lavado": "Honey",
        "precio_250g": 15.30,
        "precio_500g": 27.00,
        "precio_1000g": None
    },
    {
        "origen": "Nicaragua",
        "tipo_lavado": "Lavado",
        "precio_250g": None,
        "precio_500g": None,
        "precio_1000g": 54.00
    }
]

# Función para completar los valores nulos en los precios
def completar_precios(datos):
    df = pd.DataFrame(datos)
    
    # Completar los precios nulos para 250g y 500g
    df["precio_250g"] = df["precio_250g"].fillna(df["precio_1000g"] * 0.25)
    df["precio_500g"] = df["precio_500g"].fillna(df["precio_1000g"] * 0.5)
    
    # Completar los precios nulos para 1000g (si faltan 250g y 500g)
    df["precio_1000g"] = df.apply(
        lambda row: row["precio_1000g"] if not row["precio_250g"].isna() and not row["precio_500g"].isna() else (
            row["precio_250g"] * 4 if row["precio_250g"] is not None else row["precio_500g"] * 2
        ),
        axis=1
    )
    
    return df

# Completar los precios en el DataFrame
df = completar_precios(data)

# Calcular los precios promedio
promedio_250g = df["precio_250g"].mean()
promedio_500g = df["precio_500g"].mean()
promedio_1000g = df["precio_1000g"].mean()

# Agregar una fila con los precios promedio
df_promedio = pd.DataFrame([[
    "Promedio",
    "Promedio",
    promedio_250g,
    promedio_500g,
    promedio_1000g
]], columns=["origen", "tipo_lavado", "precio_250g", "precio_500g", "precio_1000g"])

# Concatenar el DataFrame original y la fila de promedios
df_final = pd.concat([df, df_promedio], ignore_index=True)

# Guardar el DataFrame en un archivo CSV
df_final.to_csv("precios_cafes.csv", index=False)

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df_final["origen"], df_final["precio_250g"], color="blue", alpha=0.7)
plt.bar(df_final["origen"], df_final["precio_500g"], bottom=df_final["precio_250g"], color="green", alpha=0.7)
plt.xlabel("Origen")
plt.ylabel("Precio")
plt.title("Precios por tipo de origen")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()