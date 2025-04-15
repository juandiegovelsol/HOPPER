import json

def comparar_contaminacion(datos):
    """
    Compara los niveles de contaminación del aire y del agua entre diferentes ubicaciones.

    Args:
        datos (dict): Diccionario con los datos de contaminación del aire y del agua.

    Returns:
        dict: Diccionario con las comparaciones de contaminación.
    """

    # Inicializar el diccionario para almacenar comparaciones
    comparaciones = {
        "contaminacion_aire": {},
        "condiciones_meteorologicas": {},
        "contaminacion_agua": {}
    }

    try:
        # Comparar contaminación del aire
        for parametro in ["PM2.5", "PM10", "CO2", "NO2"]:
            valores_aire = {
                location["ubicacion_1"]["fecha"]: {
                    "valor": location["contaminacion"]["aire"]["ubicacion_1"]["fecha"]["concentracion_particulas_suspendidas"][parametro]["valor"],
                    "unidad": location["contaminacion"]["aire"]["ubicacion_1"]["fecha"]["concentracion_particulas_suspendidas"][parametro]["unidad"]
                },
                location["ubicacion_2"]["fecha"]: {
                    "valor": location["contaminacion"]["aire"]["ubicacion_2"]["fecha"]["concentracion_particulas_suspendidas"][parametro]["valor"],
                    "unidad": location["contaminacion"]["aire"]["ubicacion_2"]["fecha"]["concentracion_particulas_suspendidas"][parametro]["unidad"]
                },
                location["ubicacion_3"]["fecha"]: {
                    "valor": location["contaminacion"]["aire"]["ubicacion_3"]["fecha"]["concentracion_particulas_suspendidas"][parametro]["valor"],
                    "unidad": location["contaminacion"]["aire"]["ubicacion_3"]["fecha"]["concentracion_particulas_suspendidas"][parametro]["unidad"]
                }
            }

            ubicacion_con_mayor_valor = max(valores_aire.items(), key=lambda x: x[1]['valor'])[0]
            comparaciones["contaminacion_aire"][parametro] = {
                "ubicacion_con_mayor_valor": ubicacion_con_mayor_valor,
                "valor": valores_aire[ubicacion_con_mayor_valor]["valor"],
                "unidad": valores_aire[ubicacion_con_mayor_valor]["unidad"]
            }

        # Comparar condiciones meteorológicas
        valores_meteorologia = {
            location["contaminacion"]["aire"]["ubicacion_1"]["fecha"]["condiciones_meteorologicas"]["humedad_relativa"]["valor"]: {
                "ubicacion": "ubicacion_1"
            },
            location["contaminacion"]["aire"]["ubicacion_2"]["fecha"]["condiciones_meteorologicas"]["humedad_relativa"]["valor"]: {
                "ubicacion": "ubicacion_2"
            },
            location["contaminacion"]["aire"]["ubicacion_3"]["fecha"]["condiciones_meteorologicas"]["humedad_relativa"]["valor"]: {
                "ubicacion": "ubicacion_3"
            }
        }

        ubicacion_con_mayor_humedad = max(valores_meteorologia.items(), key=lambda x: x[1]['ubicacion'])[0]
        comparaciones["condiciones_meteorologicas"]["humedad_relativa"] = {
            "ubicacion_con_mayor_valor": ubicacion_con_mayor_humedad,
            "valor": valores_meteorologia[ubicacion_con_mayor_humedad]["ubicacion"],
            "unidad": "%"
        }

        valores_meteorologia = {
            location["contaminacion"]["aire"]["ubicacion_1"]["fecha"]["condiciones_meteorologicas"]["temperatura"]["valor"]: {
                "ubicacion": "ubicacion_1"
            },
            location["contaminacion"]["aire"]["ubicacion_2"]["fecha"]["condiciones_meteorologicas"]["temperatura"]["valor"]: {
                "ubicacion": "ubicacion_2"
            },
            location["contaminacion"]["aire"]["ubicacion_3"]["fecha"]["condiciones_meteorologicas"]["temperatura"]["valor"]: {
                "ubicacion": "ubicacion_3"
            }
        }

        ubicacion_con_mayor_temperatura = max(valores_meteorologia.items(), key=lambda x: x[1]["ubicacion"])[0]
        comparaciones["condiciones_meteorologicas"]["temperatura"] = {
            "ubicacion_con_mayor_valor": ubicacion_con_mayor_temperatura,
            "valor": valores_meteorologia[ubicacion_con_mayor_temperatura]["ubicacion"],
            "unidad": "°C"
        }

        # Comparar contaminación del agua
        for parametro in ["nitrogeno_total", "fosforo_total"]:
            valores_agua = {
                location["contaminacion"]["agua"]["ubicacion_1"]["fecha"]: {
                    "valor": location["contaminacion"]["agua"]["ubicacion_1"]["concentracion_sustancias_quimicas"][parametro]["nitrogeno_total"]["valor"],
                    "unidad": location["contaminacion"]["agua"]["ubicacion_1"]["concentracion_sustancias_quimicas"][parametro]["nitrogeno_total"]["unidad"]
                },
                location["contaminacion"]["agua"]["ubicacion_2"]["fecha"]: {
                    "valor": location["contaminacion"]["agua"]["ubicacion_2"]["concentracion_sustancias_quimicas"][parametro]["nitrogeno_total"]["valor"],
                    "unidad": location["contaminacion"]["agua"]["ubicacion_2"]["concentracion_sustancias_quimicas"][parametro]["nitrogeno_total"]["unidad"]
                },
                location["contaminacion"]["agua"]["ubicacion_3"]["fecha"]: {
                    "valor": location["contaminacion"]["agua"]["ubicacion_3"]["concentracion_sustancias_quimicas"][parametro]["nitrogeno_total"]["valor"],
                    "unidad": location["contaminacion"]["agua"]["ubicacion_3"]["concentracion_sustancias_quimicas"][parametro]["nitrogeno_total"]["unidad"]
                }
            }

            ubicacion_con_mayor_valor = max(valores_agua.items(), key=lambda x: x[1]['valor'])[0]
            comparaciones["contaminacion_agua"][parametro] = {
                "ubicacion_con_mayor_valor": ubicacion_con_mayor_valor,
                "valor": valores_agua[ubicacion_con_mayor_valor]["valor"],
                "unidad": valores_agua[ubicacion_con_mayor_valor]["unidad"]
            }

            # Repetir para fósforo total
            parametro_sustituto = "fosforo_total"
            parametros = [parametro, parametro_sustituto]
            valores_agua = {
                location["contaminacion"]["agua"]["ubicacion_1"