import pandas as pd

def analisis_descriptivo(df):
    """
    Calcula estadísticas descriptivas de las ventas agrupadas por fecha.
    Agrupa el dataset por la columna 'fecha' y suma las ventas de cada día.
    
    Retorna un diccionario con:
      - 'total_ventas': Un string con el formato "Las ventas en {número de periodos} periodos fueron de {total de ventas}".
      - 'media_ventas': Promedio de las ventas diarias.
      - 'max_ventas': Valor máximo de ventas diarias.
      - 'fecha_max': Fecha en la que se obtuvo el valor máximo.
      - 'min_ventas': Valor mínimo de ventas diarias.
      - 'fecha_min': Fecha en la que se obtuvo el valor mínimo.
      
    :param df: DataFrame que contiene al menos las columnas 'fecha' y 'ventas'.
    :return: Diccionario con los indicadores descriptivos.
    """
    # Agrupar los datos por fecha y sumar las ventas de cada día
    ventas_diarias = df.groupby('fecha')['ventas'].sum().reset_index()
    
    # Calcular total, media, máximo y mínimo de ventas diarias
    total = ventas_diarias['ventas'].sum()
    media = ventas_diarias['ventas'].mean()
    
    idx_max = ventas_diarias['ventas'].idxmax()
    idx_min = ventas_diarias['ventas'].idxmin()
    
    max_ventas = ventas_diarias.loc[idx_max, 'ventas']
    fecha_max = ventas_diarias.loc[idx_max, 'fecha']
    
    min_ventas = ventas_diarias.loc[idx_min, 'ventas']
    fecha_min = ventas_diarias.loc[idx_min, 'fecha']
    
    # Número de periodos (días únicos)
    num_periodos = ventas_diarias.shape[0]
    total_str = f"Las ventas en {num_periodos} periodos fueron de {total}"
    
    return {
        'total_ventas': total_str,
        'media_ventas': media,
        'max_ventas': max_ventas,
        'fecha_max': fecha_max,
        'min_ventas': min_ventas,
        'fecha_min': fecha_min
    }

if __name__ == "__main__":
    # Caso de Prueba 1: Datos de ventas distribuidos de forma regular.
    datos1 = {
        'fecha': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-03'],
        'producto': ['A', 'B', 'A', 'B', 'A'],
        'ventas': [100, 150, 120, 130, 140]
    }
    df1 = pd.DataFrame(datos1)
    resumen1 = analisis_descriptivo(df1)
    print("Caso de Prueba 1:")
    print(resumen1)
    
    # Caso de Prueba 2: Datos de ventas con un valor atípico.
    datos2 = {
        'fecha': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-03', '2022-01-03'],
        'producto': ['A', 'B', 'A', 'B', 'A', 'B'],
        'ventas': [100, 150, 120, 130, 140, 1000]  # El valor 1000 es un outlier en la fecha 2022-01-03.
    }
    df2 = pd.DataFrame(datos2)
    resumen2 = analisis_descriptivo(df2)
    print("\nCaso de Prueba 2:")
    print(resumen2)