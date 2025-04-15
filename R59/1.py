#!pip install  pulp 
import pulp 

def producción_optimal_dulces(stock, precios):
    # Validación de las entradas
    if not isinstance(stock, list) or not isinstance(precios, list):
        raise ValueError("Tanto las existencias como los precios deben ser listas.")

    if len(stock) != 4 or len(precios) != 4:
        raise ValueError("Las listas de existencias y precios deben tener una longitud de 4.")

    if any(s <= 0 for s in stock):
        raise ValueError("Todos los valores de existencias deben ser estrictamente positivos.")

    if any(p <= 0 for p in precios):
        raise ValueError("Todos los precios deben ser estrictamente positivos.")

    # Definamos el problema de maximización
    problem = pulp.LpProblem('producción_dulces', pulp.LpMaximize)

    # Definimos productos, composiciones, precios de venta y stocks máximos 
    productos = ['Mems', 'Numy', 'Perls', 'Candy']
    composiciones = ['cacahuetes', 'almendras', 'pistacho', 'avellanas']
    existencias_máximas = {'cacahuetes': stock[0], 'almendras': stock[1], 'pistacho': stock[2], 'avellanas': stock[3]}

    # Definamos las variables para asignar stocks de ingredientes a cada producto
    var_asignación_stock = pulp.LpVariable.dicts('asignación_stock', (productos, composiciones), lowBound=0, cat='Continuous') 

    # Definamos las variables de producción
    var_producción_cajas =  pulp.LpVariable.dicts('producción_cajas',productos,lowBound=0, cat='Integer')

    # Definamos la función objetivo: maximizar las ventas dado el precio y la cantidad producida.
    obj = 0
    for i, prod in enumerate(productos):
        obj += precios[i] * var_producción_cajas[prod]
    problem += obj 

    # Cada caja producida corresponde a medio kilo de productos
    problem += var_asignación_stock['Mems']['cacahuetes'] == 0.5*var_producción_cajas['Mems']
    problem += var_asignación_stock['Numy']['cacahuetes'] + var_asignación_stock['Numy']['almendras'] + var_asignación_stock['Numy']['pistacho'] + var_asignación_stock['Numy']['avellanas'] == 0.5*var_producción_cajas['Numy']
    problem += var_asignación_stock['Perls']['pistacho'] == 0.5*var_producción_cajas['Perls']
    problem += var_asignación_stock['Candy']['cacahuetes'] + var_asignación_stock['Candy']['almendras'] + var_asignación_stock['Candy']['pistacho'] + var_asignación_stock['Candy']['avellanas'] == 0.5*var_producción_cajas['Candy']

    # producción Numy
    problem += var_asignación_stock['Numy']['cacahuetes'] <= 0.5 * var_producción_cajas['Numy']
    problem += var_asignación_stock['Numy']['almendras'] >= 0.1 * var_producción_cajas['Numy'] 
    problem += var_asignación_stock['Numy']['pistacho'] >= 0.15 * var_producción_cajas['Numy'] 

    # producción Candy
    problem += var_asignación_stock['Candy']['almendras'] >= 0.3 * var_producción_cajas['Candy']  
    problem += var_asignación_stock['Candy']['pistacho'] >= 0.3 * var_producción_cajas['Candy']   
    problem += var_asignación_stock['Candy']['avellanas'] >= 0.3 * var_producción_cajas['Candy']  


    # Restricciones de existencias
    for comp in composiciones:
        problem += pulp.lpSum(var_asignación_stock[prod][comp] for prod in productos) <= existencias_máximas[comp]

    # Resolución del problema y impresión de resultados
    estado = problem.solve()
    print('Estado:', pulp.LpStatus[estado])
    print('Total de kilos de mercancías:', sum(list(existencias_máximas.values())))
    resultados_producción = [var_producción_cajas['Mems'].varValue, var_producción_cajas['Numy'].varValue, var_producción_cajas['Perls'].varValue, var_producción_cajas['Candy'].varValue]
    print('Total de cajas producidas:', sum(list(resultados_producción)),'\n')
    for i, prod in enumerate(productos):
        print('Cajas de', prod, 'producidas:', resultados_producción[i])
    for prod in productos:
        for comp in composiciones:
            if var_asignación_stock[prod][comp].varValue>0:
                print('Se utilizaron',var_asignación_stock[prod][comp].varValue, 'kilos de', prod,'para producir', comp)
    print('\nGano total:', sum(precios[i] * resultados_producción[i] for i, prod in enumerate(productos)))




