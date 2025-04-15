class sistemaEstudiantes:
    def __init__(self, estudiantes):
        self.estudiantes = estudiantes

    def clasificar_1_a_7(self):
        """
        Clasifica a los estudiantes que están entre el semestre 1 y el 7
        en categorías según su promedio: Sobresaliente, Estándar o Bajo rendimiento.

        Returns:
            dict: Diccionario con los códigos de los estudiantes como llaves y sus categorías como valores.
        """
        clasificacion = {}

        for estudiante in self.estudiantes:
            codigo = estudiante['codigo_estudiante']
            promedio = estudiante['promedio']
            semestre = estudiante['semestre']

            if promedio < 0:
                raise ValueError(f"El promedio para el estudiante {codigo} no puede ser negativo.")
            if semestre < 0 or semestre > 15:
                raise ValueError(f"El semestre para el estudiante {codigo} está fuera del rango permitido.")
            if semestre >= 1 and semestre <= 7:
                if promedio >= 7:
                    clasificacion[codigo] = 'Sobresaliente'
                elif 4 <= promedio <= 6:
                    clasificacion[codigo] = 'Estándar'
                elif 0 <= promedio <= 3:
                    clasificacion[codigo] = 'Bajo rendimiento'
        
        return clasificacion

    def clasificar_mayor_a_7(self):
        """
        Clasifica a los estudiantes que se encuentran en semestres mayores a 7,
        en Apto para graduarse o No apto para graduarse según su promedio.

        Returns:
            dict: Diccionario con los códigos de los estudiantes como llaves y sus categorías como valores.
        """
        clasificacion = {}

        for estudiante in self.estudiantes:
            codigo = estudiante['codigo_estudiante']
            promedio = estudiante['promedio']
            semestre = estudiante['semestre']
            
            if promedio < 0:
                raise ValueError(f"El promedio para el estudiante {codigo} no puede ser negativo.")
            if semestre < 0 or semestre > 15:
                raise ValueError(f"El semestre para el estudiante {codigo} está fuera del rango permitido.")
            if semestre > 7:
                if promedio > 5:
                    clasificacion[codigo] = 'Apto para graduarse'
                else:
                    clasificacion[codigo] = 'No apto para graduarse'

        return clasificacion

# Ejemplo de uso:
estudiantes = [
    {'codigo_estudiante': '001', 'promedio': 1, 'semestre': 3},
    {'codigo_estudiante': '002', 'promedio': 6.5, 'semestre': 5},
    {'codigo_estudiante': '003', 'promedio': 3, 'semestre': 14},
]

sistema = sistemaEstudiantes(estudiantes)
print(sistema.clasificar_1_a_7())
print(sistema.clasificar_mayor_a_7())