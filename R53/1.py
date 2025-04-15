import pandas as pd

def calcular_retorno_cartera(precios, pesos):
    # Verifica que el número de activos sea el mismo en precios y pesos
    if len(precios.columns) != len(pesos):
        raise ValueError("El número de activos en los precios y los pesos debe ser el mismo.")
    
    # Calcula el retorno porcentual
    retornos = precios.pct_change()

    # Calcula el retorno de la cartera multiplicando por los pesos
    retorno_cartera = (retornos * pesos).sum(axis=1)

    # Devuelve el retorno de la cartera
    return retorno_cartera

# Datos de ejemplo
precios = pd.DataFrame({
    'Activo_A': [10, 11, 12, 13, 14],
    'Activo_B': [20, 21, 22, 23, 24]
})
pesos = [0.6, 0.4]

# Llama a la función y muestra el resultado
retorno_cartera = calcular_retorno_cartera(precios, pesos)
print(retorno_cartera)