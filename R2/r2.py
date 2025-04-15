class SistemaEstudiantes:
    def clasificar_semestres_1_a_7(self, estudiantes):
        """
        Clasifica estudiantes en semestres del 1 al 7 según su promedio:
        - Sobresaliente si el promedio es igual o mayor a 7.
        - Estándar si el promedio está entre 4 y 6.
        - Bajo rendimiento si el promedio está entre 0 y 3.

        :param estudiantes: Lista de diccionarios con llaves "codigo_estudiante", "promedio", "semestre".
        :return: Lista de diccionarios con las categorías asignadas a los estudiantes.
        """
        clasificaciones = []
        for estudiante in estudiantes:
            promedio = estudiante["promedio"]
            semestre = estudiante["semestre"]

            # Manejo de errores
            if promedio < 0:
                raise ValueError(f"El promedio no puede ser negativo para el estudiante {estudiante['codigo_estudiante']}.")
            if not (1 <= semestre <= 7):
                raise ValueError(f"Semestre fuera de rango permitido (1-7) para el estudiante {estudiante['codigo_estudiante']}.")

            if promedio >= 7:
                categoria = 'Sobresaliente'
            elif 4 <= promedio < 7:
                categoria = 'Estándar'
            else:
                categoria = 'Bajo rendimiento'

            clasificaciones.append({**estudiante, "categoria": categoria})

        return clasificaciones

    def clasificar_semestres_mayor_a_7(self, estudiantes):
        """
        Clasifica estudiantes en semestres mayores a 7 según su promedio:
        - Apto para graduarse si el promedio es mayor a 5.
        - No apto para graduarse si el promedio es menor o igual a 5.

        :param estudiantes: Lista de diccionarios con llaves "codigo_estudiante", "promedio", "semestre".
        :return: Lista de diccionarios con las categorías asignadas a los estudiantes.
        """
        clasificaciones = []
        for estudiante in estudiantes:
            promedio = estudiante["promedio"]
            semestre = estudiante["semestre"]

            # Manejo de errores
            if promedio < 0:
                raise ValueError(f"El promedio no puede ser negativo para el estudiante {estudiante['codigo_estudiante']}.")
            if not (8 <= semestre <= 15):
                raise ValueError(f"Semestre fuera de rango permitido (8-15) para el estudiante {estudiante['codigo_estudiante']}.")

            if promedio > 5:
                categoria = 'Apto para graduarse'
            else:
                categoria = 'No apto para graduarse'

            clasificaciones.append({**estudiante, "categoria": categoria})

        return clasificaciones

# Ejemplo de uso
estudiantes = [
    {"codigo_estudiante": "E001", "promedio": 8, "semestre": 5},
    {"codigo_estudiante": "E002", "promedio": 6.5, "semestre": 2},
    {"codigo_estudiante": "E003", "promedio": 6, "semestre": 9},
    {"codigo_estudiante": "E004", "promedio": 4, "semestre": 10},
]

sistema = SistemaEstudiantes()

# Clasificación para semestres 1 a 7
clasificacion_1_a_7 = sistema.clasificar_semestres_1_a_7(
    [est for est in estudiantes if 1 <= est["semestre"] <= 7]
)
print(clasificacion_1_a_7)

# Clasificación para semestres mayores a 7
clasificacion_mayor_a_7 = sistema.clasificar_semestres_mayor_a_7(
    [est for est in estudiantes if est["semestre"] > 7]
)
print(clasificacion_mayor_a_7)