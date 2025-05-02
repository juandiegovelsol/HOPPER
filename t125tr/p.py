import pandas as pd
from datetime import datetime

def validar_hora(hora_entrada, hora_salida):
    try:
        entrada = datetime.strptime(hora_entrada, "%H:%M:%S:%m:%d:%Y")
        salida = datetime.strptime(hora_salida, "%H:%M:%S:%m:%d:%Y")
        return salida > entrada
    except ValueError:
        return False

def calcular_pago_por_dia(file_path, tasa_fija):
    df = pd.read_csv(file_path)
    pagos_diarios = {}
    
    for index, row in df.iterrows():
        hora_entrada = row['hora_entrada']
        hora_salida = row['hora_salida']
        
        if validar_hora(hora_entrada, hora_salida):
            entrada = datetime.strptime(hora_entrada, "%H:%M:%S:%m:%d:%Y")
            salida = datetime.strptime(hora_salida, "%H:%M:%S:%m:%d:%Y")
            diferencia = salida - entrada
            tiempo_trabajado = diferencia.total_seconds() / 3600 
            pago = tiempo_trabajado * tasa_fija  

            if hora_salida not in pagos_diarios:
                pagos_diarios[hora_salida] = 0
            pagos_diarios[hora_salida] += pago
        else:
            print(f"Registro inválido en la fila {index + 1}: {hora_entrada} - {hora_salida}")
    
    return pagos_diarios

if __name__ == "__main__":
    file_path = 'registro_horas.csv'
    tasa_fija = 50 
    resumen_pagados = calcular_pago_por_dia(file_path, tasa_fija)
    
    for hora_salida, total in resumen_pagados.items():
        print(f"Pago hasta: {hora_salida}, Pago total: ${total:.2f}")