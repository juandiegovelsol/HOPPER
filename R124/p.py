#!pip install pulp
import pulp 

def optimizacion_stock():

    # Definimos el problema de maximización
    problema = pulp.LpProblem('produccion', pulp.LpMaximize)
    
    # Definimos productos, composiciones, precios de venta y stocks máximos
    productos = ['Producto_1', 'Producto_2', 'Producto_3', 'Producto_4']
    precios_venta = {'Producto_1': 26, 'Producto_2': 40, 'Producto_3': 38, 'Producto_4': 52}
    composiciones = ['cacahuetes', 'almendras', 'pistachos', 'avellanas']
    stock_maximos = {'cacahuetes': 550, 'almendras': 90, 'pistachos': 150, 'avellanas': 70}

    # Definimos variables para asignación de ingredientes por producto
    var_asignacion_stock = pulp.LpVariable.dicts('kg_composicion_por_producto', (productos, composiciones), lowBound=0, cat='Continuous') 
    # Definimos variables para la producción de cajas
    var_produccion_cajas =  pulp.LpVariable.dicts('Cajas_producidas', productos, lowBound=0, cat='Integer')

    # Función objetivo: maximizar ingresos
    problema += (
        precios_venta['Producto_1'] * var_produccion_cajas['Producto_1'] +
        precios_venta['Producto_2'] * var_produccion_cajas['Producto_2'] +
        precios_venta['Producto_3'] * var_produccion_cajas['Producto_3'] +
        precios_venta['Producto_4'] * var_produccion_cajas['Producto_4']
    )

    # Cada caja producida contiene medio kilo
    problema += var_asignacion_stock['Producto_1']['cacahuetes'] == 0.5 * var_produccion_cajas['Producto_1']
    problema += (
        var_asignacion_stock['Producto_2']['cacahuetes'] + 
        var_asignacion_stock['Producto_2']['almendras'] + 
        var_asignacion_stock['Producto_2']['pistachos'] + 
        var_asignacion_stock['Producto_2']['avellanas'] 
        == 0.5 * var_produccion_cajas['Producto_2']
    )
    problema += var_asignacion_stock['Producto_3']['pistachos'] == 0.5 * var_produccion_cajas['Producto_3']
    problema += (
        var_asignacion_stock['Producto_4']['cacahuetes'] + 
        var_asignacion_stock['Producto_4']['almendras'] + 
        var_asignacion_stock['Producto_4']['pistachos'] + 
        var_asignacion_stock['Producto_4']['avellanas'] 
        == 0.5 * var_produccion_cajas['Producto_4']
    )
   
    # Restricciones específicas del Producto_2
    problema += var_asignacion_stock['Producto_2']['cacahuetes'] <= 0.25 * var_produccion_cajas['Producto_2']
    problema += var_asignacion_stock['Producto_2']['almendras'] >= 0.05 * var_produccion_cajas['Producto_2']
    problema += var_asignacion_stock['Producto_2']['pistachos'] >= 0.075 * var_produccion_cajas['Producto_2']
    
    # Restricciones específicas del Producto_4
    problema += var_asignacion_stock['Producto_4']['almendras'] >= 0.15 * var_produccion_cajas['Producto_4']
    problema += var_asignacion_stock['Producto_4']['pistachos'] >= 0.15 * var_produccion_cajas['Producto_4']
    problema += var_asignacion_stock['Producto_4']['avellanas'] >= 0.15 * var_produccion_cajas['Producto_4']

    # Restricciones de disponibilidad de ingredientes
    problema += (
        var_asignacion_stock['Producto_1']['cacahuetes'] +
        var_asignacion_stock['Producto_2']['cacahuetes'] +
        var_asignacion_stock['Producto_4']['cacahuetes']
        <= stock_maximos['cacahuetes']
    )
    problema += (
        var_asignacion_stock['Producto_2']['almendras'] +
        var_asignacion_stock['Producto_4']['almendras']
        <= stock_maximos['almendras']
    )
    problema += (
        var_asignacion_stock['Producto_2']['pistachos'] +
        var_asignacion_stock['Producto_3']['pistachos'] +
        var_asignacion_stock['Producto_4']['pistachos']
        <= stock_maximos['pistachos']
    )
    problema += (
        var_asignacion_stock['Producto_2']['avellanas'] +
        var_asignacion_stock['Producto_4']['avellanas']
        <= stock_maximos['avellanas']
    )

    # Resolución del problema y resultados
    problema.solve()
    print('Kilos totales disponibles:', sum(list(stock_maximos.values())))
    resultados_produccion = [
        var_produccion_cajas['Producto_1'].varValue,
        var_produccion_cajas['Producto_2'].varValue,
        var_produccion_cajas['Producto_3'].varValue,
        var_produccion_cajas['Producto_4'].varValue
    ]
    print('Total de cajas producidas:', sum(resultados_produccion), '\n')
    for i, prod in enumerate(productos): 
        print('Cajas de', prod, 'producidas:', resultados_produccion[i])
    print('\n')
    for prod in productos:
        for comp in composiciones:
            if var_asignacion_stock[prod][comp].varValue is not None and var_asignacion_stock[prod][comp].varValue > 0:
                print('Para producir', prod, 'se usaron', var_asignacion_stock[prod][comp].varValue, 'kilos de', comp)

    print('\nGanancia total:', sum(precios_venta[prod] * resultados_produccion[i] for i, prod in enumerate(productos)))

optimizacion_stock()