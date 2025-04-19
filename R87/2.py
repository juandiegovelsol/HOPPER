# Función para clasificar el promedio de MP2.5
def clasificar_promedio_mp(promedio):
    """
    Clasifica la calidad del aire según el promedio de MP2.5.
    
    Args:
        promedio (float): Promedio de concentración de MP2.5.
    
    Returns:
        str: Clasificación de la calidad del aire.
    """
    if promedio < 20:
        return "Buena"
    elif promedio <= 40:
        return "Regular"
    elif promedio <= 60:
        return "Alerta Amarilla"
    else:
        return "Alerta Roja"

# Diccionario con los datos de mediciones por comuna
mediciones = {
    "Cerrillos": [21, 38, 40, 55, 61, 42, 35],
    "La Pintana": [29, 33, 36, 48, 52, 47, 45],
    "Talagante": [12, 18, 19, 23, 21, 17, 15],
    "San José de Maipo": [9, 14, 11, 13, 15, 12, 10],
    "Independencia": [40, 42, 43, 49, 52, 56, 61]
}

# Diccionarios para almacenar alertas y clasificaciones
alertas = {}
clasificaciones = {}

# Análisis de cada comuna
for comuna, valores_diarios in mediciones.items():
    promedio = sum(valores_diarios) / len(valores_diarios)
    clasificacion = clasificar_promedio_mp(promedio)
    clasificaciones[comuna] = clasificacion

    # Evaluación de días críticos
    for valor_dia in valores_diarios:
        if valor_dia > 60:
            if comuna not in alertas:
                alertas[comuna] = 0
            alertas[comuna] += 1

# Presentación de resultados
print("Clasificación promedio por comuna:")
for c, clas in clasificaciones.items():
    print(f"{c}: {clas}")

print("\nComunas con episodios críticos registrados:")
for comuna, cantidad in alertas.items():
    print(f"{comuna}: {cantidad} días")