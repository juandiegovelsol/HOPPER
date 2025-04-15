import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

# Función para generar datos falsos
def generar_datos_falsos(num_filas=1000):
    np.random.seed(42)  # Para reproducibilidad
    fechas = [f"2023-{random.randint(1, 12)}-{random.randint(1, 28)}" for _ in range(num_filas)]
    clientes_ids = [f"{random.randint(10000, 99999)}" for _ in range(num_filas)]
    usos_datos_mb = [random.randint(100, 5000) for _ in range(num_filas)]
    horas_dia = [random.choice(["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]) for _ in range(num_filas)]
    
    return pd.DataFrame({
        "fecha": fechas,
        "cliente_id": clientes_ids,
        "uso_datos_mb": usos_datos_mb,
        "hora_dia": horas_dia
    })

# Función para validar y procesar datos
def validar_y_procesar_datos(df):
    # Convertir la columna 'fecha' a formato ISO
    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d", errors='coerce')
    
    # Convertir las columnas 'uso_datos_mb' y 'cliente_id' a numéricos
    df["uso_datos_mb"] = pd.to_numeric(df["uso_datos_mb"], errors='coerce')
    df["cliente_id"] = pd.to_numeric(df["cliente_id"], errors='coerce')
    
    # Eliminar filas con valores faltantes o erróneos
    df = df.dropna(subset=["fecha", "cliente_id", "uso_datos_mb", "hora_dia"])
    df = df.dropna(subset=["uso_datos_mb", "cliente_id"])
    
    return df

# Función para calcular el uso total de datos, el promedio diario y los días anómalos
def calcular_metricas(df):
    df["dia"] = df["fecha"].dt.date
    df = df.groupby(["cliente_id", "dia"])["uso_datos_mb"].sum().reset_index()
    
    # Calcular el promedio diario
    df["promedio_diario"] = df.groupby("cliente_id")["uso_datos_mb"].transform("mean")
    
    # Calcular los días con uso anómalo
    df["uso_anomalo"] = df["uso_datos_mb"] > df["promedio_diario"] * 1.2
    df["dias_anomalo"] = df["uso_anomalo"].astype(int)
    
    return df

# Función para generar el resumen mensual y el gráfico de líneas
def generar_resumen_y_grafico(df):
    resumen_mensual = {}
    for cliente_id in df["cliente_id"].unique():
        cliente_data = df[df["cliente_id"] == cliente_id].groupby("dia")["uso_datos_mb"].sum().reset_index()
        uso_total_datos = cliente_data["uso_datos_mb"].sum()
        promedio_diario = cliente_data["uso_datos_mb"].mean()
        dias_anomalo = cliente_data["uso_anomalo"].sum()
        porcentaje_dias_anomalo = (dias_anomalo / len(cliente_data)) * 100
        
        resumen_mensual[cliente_id] = {
            "uso_total_datos_mb": uso_total_datos,
            "promedio_diario_mb": promedio_diario,
            "dias_uso_anomalo": dias_anomalo,
            "porcentaje_dias_anomalo": porcentaje_dias_anomalo
        }
    
    # Generar gráfico de líneas
    plt.figure(figsize=(14, 7))
    for cliente_id in df["cliente_id"].unique():
        cliente_data = df[df["cliente_id"] == cliente_id]
        plt.plot(cliente_data["fecha"], cliente_data["uso_datos_mb"], label=f"Cliente {cliente_id}")
    
    plt.title("Tendencia del uso de datos por cliente")
    plt.xlabel("Fecha")
    plt.ylabel("Uso de datos (MB)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return resumen_mensual

# Función principal para ejecutar el análisis
def analizar_uso_datos(archivo_csv):
    # Generar datos falsos si no hay archivo de entrada
    """ if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no existe. Generando datos falsos.")
        df = generar_datos_falsos()
    else: """
    df = pd.read_csv(archivo_csv)
    
    # Validar y procesar los datos
    df = validar_y_procesar_datos(df)
    
    # Calcular métricas
    df = calcular_metricas(df)
    
    # Generar resumen y gráfico
    resumen_mensual = generar_resumen_y_grafico(df)
    
    # Guardar el resumen en un archivo JSON
    with open("resumen_uso_datos.json", "w") as f:
        json.dump(resumen_mensual, f, indent=4)
    
    print("Análisis completado. El resumen se ha guardado en 'resumen_uso_datos.json'.")

# Ejemplo de uso
archivo_csv = "uso_datos.csv"
analizar_uso_datos(archivo_csv)
