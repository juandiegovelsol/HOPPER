import pandas as pd
import numpy as np
from datetime import date, timedelta
import random

# Modelos de Volkswagen
modelos = ['Golf', 'Passat', 'Tiguan', 'Polo', 'Arteon', 'T-Roc', 'Jetta', 'Touran', 'Touareg', 'Atlas']

# Simular 2000 ventas
np.random.seed(42)  # Para reproducibilidad
fechas = [date(2023, 1, 1) + timedelta(days=random.randint(0, 364)) for _ in range(2000)]
modelos_vendidos = [random.choice(modelos) for _ in range(2000)]
precios = [random.randint(10_000_000, 60_000_000) for _ in range(2000)]

# Crear DataFrame original
df = pd.DataFrame({'Fecha': fechas, 'Modelo': modelos_vendidos, 'Precio': precios})

# Agrupar por mes y modelo, y calcular el monto total de ventas
df['Mes'] = df['Fecha'].dt.month
df['Año'] = df['Fecha'].dt.year

ventas_agrupadas = df.groupby(['Mes', 'Modelo'])['Precio'].sum().reset_index()

# Encontrar el modelo con mayor monto total por mes
modelo_top_por_mes = ventas_agrupadas.loc[ventas_agrupadas.groupby('Mes')['Precio'].idxmax()]

# Ordenar el resultado final por mes
modelo_top_por_mes = modelo_top_por_mes.sort_values('Mes')

# Imprimir resultados
print(modelo_top_por_mes)