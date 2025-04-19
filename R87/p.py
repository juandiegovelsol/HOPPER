mediciones = {
    "Cerrillos": [21, 38, 40, 55, 61, 42, 35],
    "La Pintana": [29, 33, 36, 48, 52, 47, 45],
    "Talagante": [12, 18, 19, 23, 21, 17, 15],
    "San José de Maipo": [9, 14, 11, 13, 15, 12, 10],
    "Independencia": [40, 42, 43, 49, 52, 56, 61]
}

alertas = {}
clasificaciones = {}

for comuna, valores in mediciones.items():  
    promedio = sum(valores) / len(valores)
    clasificacion = ""

    if promedio < 20:  
        clasificacion = "Buena"
    elif promedio <= 40:  
        clasificacion = "Regular"
    elif promedio <= 60:  
        clasificacion = "Alerta Amarilla"
    else:  
        clasificacion = "Alerta Roja"

    clasificaciones[comuna] = clasificacion

    for valor in valores:  
        if valor > 60:  
            if comuna not in alertas:  
                alertas[comuna] = 0
            alertas[comuna] += 1

print("Clasificación promedio por comuna:")
for c, clas in clasificaciones.items():  
    print(f"{c}: {clas}")

print("\nComunas con episodios críticos registrados:")
for comuna, cantidad in alertas.items():  
    print(f"{comuna}: {cantidad} días")