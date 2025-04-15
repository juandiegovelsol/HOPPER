import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import random
import datetime

# Función para generar datos falsos para testear el código
def generar_datos_falsos(num_filas=1000, rango_fecha=("2023-01-01", "2023-12-31"), rango_datos=(100, 5000)):
    np.random.seed(42)  # Para reproducibilidad
    fecha_inicial = datetime.datetime.strptime(rango_fecha[0], "%Y-%m-%d")
    fecha_final = datetime.datetime.strptime(rango_fecha[1], "%Y-%m-%d")

    datos = []
    while len(datos) < num_filas:
        fecha = fecha_inicial + datetime.timedelta(days=random.randint(0, 365))
        cliente_id = str(random.randint(10000, 99999))
        uso_datos = round(random.uniform(*rango_datos), 2)
        hora_dia = str(fecha.hour).zfill(2) + ":" + str(fecha.minute).zfill(2)

        datos.append({
            "fecha": fecha.strftime("%Y-%m-%d"),
            "cliente_id": cliente_id,
            "uso_datos_mb": uso_datos,
            "hora_dia": hora_dia
        })

    return pd.DataFrame(datos)

# Función para validar y limpiar los datos
def validar_limpiar_datos(df):
    # Eliminar filas con valores faltantes
    df.dropna(subset=["fecha", "cliente_id", "uso_datos_mb", "hora_dia"], inplace=True)

    # Convertir fecha a formato ISO si es posible
    try:
        df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d", errors="coerce")
    except Exception as e:
        print(f"Error al convertir fechas: {e}")
        df.dropna(subset=["fecha"], inplace=True)

    # Convertir uso_datos a numérico
    df["uso_datos_mb"] = pd.to_numeric(df["uso_datos_mb"], errors="coerce")
    df.dropna(subset=["uso_datos_mb"], inplace=True)

    # Convertir cliente_id a numérico
    df["cliente_id"] = pd.to_numeric(df["cliente_id"], errors="coerce")
    df.dropna(subset=["cliente_id"], inplace=True)

    # Eliminar filas con datos erróneos
    df = df[(df["uso_datos_mb"] > 0) & (df["cliente_id"] > 0)]

    return df

# Función para analizar el uso de datos y generar el resumen mensual
def analizar_uso_datos(df):
    # Convertir la columna fecha a datetime
    df["fecha"] = pd.to_datetime(df["fecha"])

    # Agrupar por cliente y día, sumar uso de datos y calcular promedio diario
    resumen = df.groupby(["cliente_id", df["fecha"].dt.date]).agg({
        "uso_datos_mb": ["sum", "mean"]
    }).reset_index()

    # Identificar días con uso anómalo
    resumen["dias_anomalo"] = resumen["uso_datos_mb"] > (resumen["uso_datos_mb"].mean() * 1.2)

    # Calcular porcentaje de días anómalos
    resumen["porcentaje_dias_anomalo"] = (resumen["dias_anomalo"].mean() * 100)

    return resumen

# Función para generar el gráfico de líneas del uso de datos
def generar_grafico(resumen):
    plt.figure(figsize=(10, 6))
    for _, fila in resumen.iterrows():
        plt.plot(fila["fecha"], fila["uso_datos_mb"], label=f"Cliente {fila['cliente_id']}")

    plt.xlabel("Fecha")
    plt.ylabel("Uso de Datos (MB)")
    plt.title("Tendencia del Uso de Datos por Cliente")
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para guardar el resumen en formato JSON
def guardar_json(resumen, nombre_archivo="resumen_uso_datos.json"):
    with open(nombre_archivo, "w") as f:
        json.dump(resumen.to_dict(orient="records"), f, indent=4)

# Función principal para ejecutar el análisis
def main():
    # Generar datos falsos
    df_falsos = generar_datos_falsos()
    print(df_falsos)
    print("Datos falsos generados:", len(df_falsos))

    # Limpiar y validar los datos
    df_limpio = validar_limpiar_datos(df_falsos)
    print("Datos limpiados:", len(df_limpio))

    # Analizar el uso de datos
    resumen = analizar_uso_datos(df_limpio)

    # Guardar el resumen en JSON
    guardar_json(resumen)

    # Generar el gráfico de líneas
    generar_grafico(resumen)

# Ejecutar la función principal
if __name__ == "__main__":
    main()