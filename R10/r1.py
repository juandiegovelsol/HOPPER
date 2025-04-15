import pandas as pd
import numpy as np
import random

# Configuración de los modelos y el rango de precios
modelos = ['Golf', 'Passat', 'Tiguan', 'Polo', 'Arteon', 'T-Roc', 'Jetta', 'Touran', 'Touareg', 'Atlas']
precio_min = 10_000_000
precio_max = 60_000_000

# Generar fechas aleatorias en 2023
fechas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
fechas_aleatorias = np.random.choice(fechas, size=2000)

# Generar datos simulados de ventas
datos_ventas = {
    'Fecha': fechas_aleatorias,
    'Modelo': np.random.choice(modelos, size=2000),
    'Precio': [random.randint(precio_min, precio_max) for _ in range(2000)]
}

# Crear DataFrame
df_ventas = pd.DataFrame(datos_ventas)

# Crear tabla resumen por mes
df_ventas['Mes'] = df_ventas['Fecha'].dt.to_period('M')
resumen_mensual = df_ventas.groupby(['Mes', 'Modelo']).agg({'Precio': 'sum'}).reset_index()

# Encontrar el modelo con mayor venta por mes
idx_max_por_mes = resumen_mensual.groupby('Mes')['Precio'].idxmax()
resultado_mensual = resumen_mensual.loc[idx_max_por_mes].reset_index(drop=True)

# Renombrar columnas para claridad
resultado_mensual.rename(columns={'Precio': 'Monto Total de Ventas'}, inplace=True)

# Convertir el período a fecha (primer día del mes) y formatear como DD/MM/YYYY
resultado_mensual['Mes'] = resultado_mensual['Mes'].dt.to_timestamp().dt.strftime('%d/%m/%Y')

# Imprimir resultado
print(resultado_mensual)