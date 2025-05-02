import pandas as pd
from datetime import datetime

def validar_hora(hora_entrada, hora_salida):
    try:
        # Convertir las horas a objetos de tiempo
        entrada = datetime.strptime(hora_entrada, "%S:%M:%H:%d:%m:%Y")
        salida = datetime.strptime(hora_salida, "%S:%M:%H:%d:%m:%Y")
        
        # Validar que la hora de salida es posterior a la hora de entrada
        return salida > entrada
    except ValueError:
        return False

def calcular_pago_por_dia(file_path, tasa_fija):
    # Leer el archivo CSV
    df = pd.read_csv(file_path)
    
    # Crear un diccionario para almacenar el total por día
    pagos_diarios = {}

    for index, row in df.iterrows():
        hora_entrada = row['hora_entrada']
        hora_salida = row['hora_salida']
        
        if validar_hora(hora_entrada, hora_salida):
            # Calcular el tiempo trabajado
            entrada = datetime.strptime(hora_entrada, "%S:%M:%H:%d:%m:%Y")
            salida = datetime.strptime(hora_salida, "%S:%M:%H:%d:%m:%Y")
            
            tiempo_trabajado = (salida - entrada).seconds / 3600  # Convertir a horas
            pago = tiempo_trabajado * tasa_fija
            
            # Obtener la fecha
            fecha = entrada.date()
            
            # Acumular el pago en el diccionario
            if fecha not in pagos_diarios:
                pagos_diarios[fecha] = 0
            pagos_diarios[fecha] += pago
        else:
            print(f"Registro inválido en la fila {index + 1}: {hora_entrada} - {hora_salida}")

    return pagos_diarios

# Ejemplo de uso
if __name__ == "__main__":
    file_path = 'registro_horas.csv'  # Cambia esto por la ruta de tu archivo CSV
    tasa_fija = 5000  # Pago por hora en CLP
    resumen_pagados = calcular_pago_por_dia(file_path, tasa_fija)

    # Imprimir resumen de pagos diarios
    for fecha, total in resumen_pagados.items():
        print(f"Fecha: {fecha}, Pago total: {total:.2f} CLP")