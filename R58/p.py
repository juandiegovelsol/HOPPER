#!pip install pulp
import pulp 
import pandas as pd 
from collections import Counter

def optimization_descanso_emepleados(empleados,dias,min_empleados_en_cada_turno_manana,min_empleados_en_cada_turno_tarde):
    max_dias_seguido_de_trabajo = 6 
    max_dias_seguido_de_descanso = 4
    try:
        empleados = int(empleados)
        if empleados <= 0 :
            raise ValueError("El numero de empleados tiene que ser un numero positivo.")
    except ValueError as e:
        raise ValueError(f"La entrada no es valida: {e}")

    try:
        dias = int(dias)
        if dias <= 0 :
            raise ValueError("El numero de días por la planificacion tiene que ser un numero mayor de 0.")
    except ValueError as e:
        raise ValueError(f"La entrada no es valida: {e}")
    
    var_M = pulp.LpVariable.dicts('Manana', (range(dias), range(empleados)), 0, 1, 'Binary') 
    var_T = pulp.LpVariable.dicts('Tarde', (range(dias), range(empleados)), 0, 1, 'Binary') 
    var_D = pulp.LpVariable.dicts('Descanso', (range(dias), range(empleados)), 0, 1, 'Binary') 

    problem = pulp.LpProblem('optimization_turnos_hotel',  pulp.LpMaximize)

    obj = 0
    for i in range(dias): 
        for j in range(empleados): 
            obj += var_D[i][j]
    problem += obj 

    for i in range(dias): 
        for j in range(empleados): 
            c = 0 
            c += var_M[i][j] + var_T[i][j] + var_D[i][j] 
            problem += c == 1

    for i in range(0, dias): 
        c = 0 
        d = 0 
        for j in range(empleados): 
            c += var_M[i][j] 
            d += var_T[i][j] 
        problem += c >= min_empleados_en_cada_turno_manana 
        problem += d >= min_empleados_en_cada_turno_tarde

    for j in range(empleados): 
        for i in range(0, dias-max_dias_seguido_de_descanso): 
            c = 0 
            for w in range(max_dias_seguido_de_descanso+1): 
                c += var_D[i+w][j] 
                problem +=  c <= max_dias_seguido_de_descanso

    for j in range(empleados): 
        for i in range(0, dias-max_dias_seguido_de_trabajo): 
            c = 0 
            for w in range(max_dias_seguido_de_trabajo+1): 
                c += var_M[i+w][j] + var_T[i+w][j] 
                problem += c  <= max_dias_seguido_de_trabajo

    status = problem.solve() 
    print('Estado:',pulp.LpStatus[status])
    if pulp.LpStatus[status]=='Infeasible':
        print('El número de empleados indicado no es suficientemente grande para cumplir con las restricciones establecidas.')
    else:
        solution_M = [[int(pulp.value(var_M[i][j])) for j in range(empleados)] for i in range(dias)]
        solution_T = [[int(pulp.value(var_T[i][j])) for j in range(empleados)] for i in range(dias)]

        def sacar_las_soluciones(solution_M, solution_T):
            df = pd.DataFrame(index=[f"empleado {i+1}" for i in range(len(solution_M[0]))], columns=[f"Día {i+1}" for i in range(len(solution_M))])
            for i in range(len(solution_M)):
                for j in range(len(solution_M[i])):
                    if solution_M[i][j] == 1:
                        df.at[f"empleado {j+1}", f"Día {i+1}"] = "M"
                    elif solution_T[i][j] == 1:
                        df.at[f"empleado {j+1}", f"Día {i+1}"] = "T"
                    else:
                        df.at[f"empleado {j+1}", f"Día {i+1}"] = "OFF"
            return df

        tunros_df = sacar_las_soluciones(solution_M, solution_T)
        resultado = tunros_df.transpose()
        for i, día in enumerate(resultado.index[:3]): 
            print('En el día', str(i), 'tenemos:\n', list(resultado.loc[día]),Counter(resultado.loc[día]))



## Test Entrada 1
""" empleados = 10
dias = 25
min_empleados_en_cada_turno_manana = 3 
min_empleados_en_cada_turno_tarde = 4 
optimization_descanso_emepleados(empleados,dias,min_empleados_en_cada_turno_manana,min_empleados_en_cada_turno_tarde) """
## Test Entrada 2
""" empleados = 6
dias = 25
min_empleados_en_cada_turno_manana = 3 
min_empleados_en_cada_turno_tarde = 4 
optimization_descanso_emepleados(empleados,dias,min_empleados_en_cada_turno_manana,min_empleados_en_cada_turno_tarde) """
## Test Entrada 3
empleados = 10
dias = 10
min_empleados_en_cada_turno_manana = 3 
min_empleados_en_cada_turno_tarde = 2 
optimization_descanso_emepleados(empleados,dias,min_empleados_en_cada_turno_manana,min_empleados_en_cada_turno_tarde)