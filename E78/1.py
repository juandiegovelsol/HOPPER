import pandas as pd
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

# Crear DataFrame
df = pd.DataFrame(data)

# Calcular precios según regla
for col in ["precio_250g", "precio_500g", "precio_1000g"]:
    if df[col].isnull().any():
        # Si alguno de los precios es nulo, calcular el precio del kilo
        df.loc[(df[col].isnull()), col] = df.loc[(df[col].isnull()), "precio_1000g"] / 1000 * 100

        # Si el precio del kilo es nulo, usar el precio del cuarto de kilo
        if df["precio_1000g"].isnull().any():
            df.loc[(df["precio_1000g"].isnull()), "precio_1000g"] = df.loc[(df["precio_1000g"].isnull()), "precio_250g"] * 4 / 100

        # Si el precio del kilo sigue siendo nulo, usar el precio del medio kilo
        if df["precio_1000g"].isnull().any():
            df.loc[(df["precio_1000g"].isnull()), "precio_1000g"] = df.loc[(df["precio_1000g"].isnull()), "precio_500g"] * 5 / 100

# Agregar fila de promedios
promedios = df[["precio_250g", "precio_500g", "precio_1000g"]].mean()
df = pd.concat([df, pd.DataFrame([promedios], columns=["precio_250g", "precio_500g", "precio_1000g"])])

# Guardar DataFrame en CSV
df.to_csv("precios_cafe.csv", index=False)

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
bar_width = 0.25

# Posiciones de las barras
r1 = [i + bar_width for i in range(3)]  # Para 250g, 500g y 1000g
r2 = [i + bar_width + bar_width for i in range(3)]  # Para la fila de promedios

# Altura de las barras
alturas = df["precio_250g"]
alturas2 = df["precio_500g"]
alturas3 = df["precio_1000g"]

# Dibujar barras
plt.bar(r1, alturas, width=bar_width, label="250g", color='skyblue')
plt.bar(r2, alturas2, width=bar_width, label="500g", color='lightcoral')
plt.bar(r3, alturas3, width=bar_width, label="1000g", color='lightgreen')

# Etiquetas en las barras
for i, altura in enumerate(alturas):
    plt.text(r1[i] + bar_width/2, altura + 2, f'{altura:.2f}', ha='center', va='bottom')
for i, altura in enumerate(alturas2):
    plt.text(r2[i] + bar_width/2, altura + 2, f'{altura:.2f}', ha='center', va='bottom')
for i, altura in enumerate(alturas3):
    plt.text(r3[i] + bar_width/2, altura + 2, f'{altura:.2f}', ha='center', va='bottom')

# Etiquetas en las barras de promedios
for i, altura in enumerate(alturas3):
    plt.text(r3[i] + bar_width/2, altura + 2, f'{alturas3[i]:.2f}', ha='center', va='bottom')

# Leyenda
plt.legend()
plt.title("Precios de Café por Origen y Tipo de Lavado")
plt.xlabel("Unidades")
plt.ylabel("Precio (USD)")
plt.xticks([r + bar_width/2 for r in range(3)], ["250g", "500g", "1000g"])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
