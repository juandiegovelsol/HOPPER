import pandas as pd

def calcular_retorno_cartera(precios, pesos):
   if len(precios.columns) != len(pesos):
      raise ValueError("El número de activos en los precios y los pesos debe ser el mismo.")
retornos = precios.pct_change()
retorno_cartera = retornos.mean(axis=1) 
      return retorno_cartera
      precios = pd.DataFrame({
    'Activo_A': [10, 11, 12, 13, 14],
    'Activo_B': [20, 21, 22, 23, 24]
})
pesos = [0.6, 0.4]
           retorno_cartera = calcular_retorno_cartera(precios, pesos)
print(retorno_cartera)