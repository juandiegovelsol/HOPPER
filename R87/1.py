def clasificar_promedio_mp(promedio):
    """
    Clasifica el nivel de contaminación según el promedio de MP2.5.
    
    Parámetros:
    promedio (float): Promedio de las mediciones de MP2.5.
    
    Retorna:
    str: Clasificación de la calidad del aire ("Buena", "Regular", "Alerta Amarilla", "Alerta Roja").
    """
    if promedio < 20:
        return "Buena"
    elif promedio <= 40:
        return "Regular"
    elif promedio <= 60:
        return "Alerta Amarilla"
    else:
        return "Alerta Roja"

mediciones = {
    "Cerrillos": [21, 38, 40, 55, 61, 42, 35],
    "La Pintana": [29, 33, 36, 48, 52, 47, 45],
    "Talagante": [12, 18, 19, 23, 21, 17, 15],
    "San José de Maipo": [9, 14, 11, 13, 15, 12, 10],
    "Independencia": [40, 42, 43, 49, 52, 56, 61]
}

alertas = {}
clasificaciones = {}

for comuna, valores_diarios in mediciones.items():
    promedio = sum(valores_diarios) / len(valores_diarios)
    clasificacion = clasificar_promedio_mp(promedio)
    clasificaciones[comuna] = clasificacion

    for valor_diario in valores_diarios:  
        if valor_diario > 60:  
            if comuna not in alertas:  
                alertas[comuna] = 0
            alertas[comuna] += 1

print("Clasificación promedio por comuna:")
for c, clas in clasificaciones.items():  
    print(f"{c}: {clas}")

print("\nComunas con episodios críticos registrados:")
for comuna, cantidad in alertas.items():  
    print(f"{comuna}: {cantidad} días")