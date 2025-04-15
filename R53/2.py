import pandas as pd

def calcular_retorno_cartera(precios, pesos):
    # Validación de la dimensión de los pesos
    if len(precios.columns) != len(pesos):
        raise ValueError("El número de activos en los precios y los pesos debe ser el mismo.")
    
    # Cálculo de los retornos diarios (o periódicos) de cada activo
    retornos = precios.pct_change().dropna()

    # Cálculo del retorno ponderado de la cartera
    retorno_cartera = pd.Series(index=retornos.index)
    for i, columna in enumerate(retornos.columns):
        retorno_cartera += retornos[columna] * pesos[i]
    
    return retorno_cartera

# Definición de datos de prueba
precios = pd.DataFrame({
    'Activo_A': [10, 11, 12, 13, 14],
    'Activo_B': [20, 21, 22, 23, 24]
})
pesos = [0.6, 0.4]

# Calculando el retorno de la cartera
retorno_cartera = calcular_retorno_cartera(precios, pesos)
print(retorno_cartera)