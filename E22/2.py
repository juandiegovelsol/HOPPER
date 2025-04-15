import json
from typing import Dict

def comparar_contaminacion(datos: Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, any]]]]]) -> Dict[str, Dict[str, Dict[str, str]]]:
    """
    Compara la contaminación del aire y del agua entre diferentes ubicaciones y retorna un diccionario con los resultados.

    Parámetros:
        datos (Dict[str, Dict[str, Dict[str, Dict[str, any]]]]): Diccionario con datos de contaminación del aire y del agua.

    Retorna:
        Dict[str, Dict[str, Dict[str, str]]]: Diccionario con las comparaciones realizadas.
    """
    comparaciones = {
        "contaminacion_aire": {},
        "condiciones_meteorologicas": {},
        "contaminacion_agua": {}
    }

    # Comparación de contaminación del aire
    for ubicacion in datos["contaminacion"]["aire"]:
        pm25 = datos["contaminacion"]["aire"][ubicacion]["concentracion_particulas_suspendidas"]["PM2.5"]
        pm10 = datos["contaminacion"]["aire"][ubicacion]["concentracion_particulas_suspendidas"]["PM10"]
        co2 = datos["contaminacion"]["aire"][ubicacion]["concentracion_gases_efecto_invernadero"]["CO2"]
        no2 = datos["contaminacion"]["aire"][ubicacion]["concentracion_gases_toxicos"]["NO2"]

        if pm25 not in comparaciones["contaminacion_aire"]:
            comparaciones["contaminacion_aire"][pm25] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": pm25,
                "unidad": "µg/m³"
            }
        elif pm25 > comparaciones["contaminacion_aire"][pm25]["valor"]:
            comparaciones["contaminacion_aire"][pm25] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": pm25,
                "unidad": "µg/m³"
            }

        if pm10 not in comparaciones["contaminacion_aire"]:
            comparaciones["contaminacion_aire"][pm10] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": pm10,
                "unidad": "µg/m³"
            }
        elif pm10 > comparaciones["contaminacion_aire"][pm10]["valor"]:
            comparaciones["contaminacion_aire"][pm10] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": pm10,
                "unidad": "µg/m³"
            }

        if co2 not in comparaciones["contaminacion_aire"]:
            comparaciones["contaminacion_aire"][co2] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": co2,
                "unidad": "ppm"
            }
        elif co2 > comparaciones["contaminacion_aire"][co2]["valor"]:
            comparaciones["contaminacion_aire"][co2] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": co2,
                "unidad": "ppm"
            }

        if no2 not in comparaciones["contaminacion_aire"]:
            comparaciones["contaminacion_aire"][no2] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": no2,
                "unidad": "µg/m³"
            }
        elif no2 > comparaciones["contaminacion_aire"][no2]["valor"]:
            comparaciones["contaminacion_aire"][no2] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": no2,
                "unidad": "µg/m³"
            }

    # Comparación de condiciones meteorológicas
    for ubicacion in datos["contaminacion"]["aire"]:
        humedad_relativa = datos["contaminacion"]["aire"][ubicacion]["condiciones_meteorologicas"]["humedad_relativa"]
        temperatura = datos["contaminacion"]["aire"][ubicacion]["condiciones_meteorologicas"]["temperatura"]

        if humedad_relativa not in comparaciones["condiciones_meteorologicas"]:
            comparaciones["condiciones_meteorologicas"][humedad_relativa] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": humedad_relativa,
                "unidad": "%"
            }
        elif humedad_relativa > comparaciones["condiciones_meteorologicas"][humedad_relativa]["valor"]:
            comparaciones["condiciones_meteorologicas"][humedad_relativa] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": humedad_relativa,
                "unidad": "%"
            }

        if temperatura not in comparaciones["condiciones_meteorologicas"]:
            comparaciones["condiciones_meteorologicas"][temperatura] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": temperatura,
                "unidad": "°C"
            }
        elif temperatura > comparaciones["condiciones_meteorologicas"][temperatura]["valor"]:
            comparaciones["condiciones_meteorologicas"][temperatura] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": temperatura,
                "unidad": "°C"
            }

    # Comparación de contaminación del agua
    for ubicacion in datos["contaminacion"]["agua"]:
        nitrogeno_total = datos["contaminacion"]["agua"][ubicacion]["concentracion_sustancias_quimicas"]["nitrogeno_total"]
        fosforo_total = datos["contaminacion"]["agua"][ubicacion]["concentracion_sustancias_quimicas"]["fosforo_total"]

        if nitrogeno_total not in comparaciones["contaminacion_agua"]:
            comparaciones["contaminacion_agua"][nitrogeno_total] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": nitrogeno_total,
                "unidad": "mg/L"
            }
        elif nitrogeno_total > comparaciones["contaminacion_agua"][nitrogeno_total]["valor"]:
            comparaciones["contaminacion_agua"][nitrogeno_total] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": nitrogeno_total,
                "unidad": "mg/L"
            }

        if fosforo_total not in comparaciones["contaminacion_agua"]:
            comparaciones["contaminacion_agua"][fosforo_total] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": fosforo_total,
                "unidad": "mg/L"
            }
        elif fosforo_total > comparaciones["contaminacion_agua"][fosforo_total]["valor"]:
            comparaciones["contaminacion_agua"][fosforo_total] = {
                "ubicacion_con_mayor_valor": ubicacion,
                "valor": fosforo_total,
                "unidad": "mg/L"
            }

    return comparaciones

# Ejemplo de uso
""" datos_ejemplo = {
    "contaminacion": {
        "aire": {
            "ubicacion_1": {
                "fecha": "20/04/2024",
                "concentracion_particulas_suspendidas": {
                    "PM2.5": { """

datos_ejemplo = {
  "contaminacion": {
    "aire": {
      "ubicacion_1": {
        "fecha": "20/04/2024",
        "concentracion_particulas_suspendidas": {
          "PM2.5": {
            "valor": 12.5,
            "unidad": "µg/m³",
            "descripcion": "Partículas finas en el aire con diámetro menor a 2.5 micrómetros."
          },
          "PM10": {
            "valor": 30,
            "unidad": "µg/m³",
            "descripcion": "Partículas en el aire con diámetro menor a 10 micrómetros."
          }
        },
        "concentracion_gases_efecto_invernadero": {
          "CO2": {
            "valor": 400,
            "unidad": "ppm",
            "descripcion": "Dióxido de carbono, principal gas de efecto invernadero."
          },
          "CH4": {
            "valor": 1.8,
            "unidad": "ppm",
            "descripcion": "Metano, gas de efecto invernadero con alta capacidad de calentamiento."
          },
          "N2O": {
            "valor": 0.3,
            "unidad": "ppm",
            "descripcion": "Óxido nitroso, gas de efecto invernadero con efectos a largo plazo."
          }
        },
        "concentracion_gases_toxicos": {
          "NO2": {
            "valor": 50,
            "unidad": "µg/m³",
            "descripcion": "Dióxido de nitrógeno, gas tóxico que contribuye a la formación de ozono troposférico."
          },
          "SO2": {
            "valor": 20,
            "unidad": "µg/m³",
            "descripcion": "Dióxido de azufre, gas tóxico que puede causar problemas respiratorios."
          },
          "O3": {
            "valor": 180,
            "unidad": "µg/m³",
            "descripcion": "Ozono, gas tóxico en la atmósfera que puede irritar las vías respiratorias."
          }
        },
        "condiciones_meteorologicas": {
          "humedad_relativa": {
            "valor": 65,
            "unidad": "%",
            "descripcion": "Porcentaje de humedad relativa en el aire."
          },
          "temperatura": {
            "valor": 22,
            "unidad": "°C",
            "descripcion": "Temperatura del aire en grados Celsius."
          }
        }
      },
      "ubicacion_2": {
        "fecha": "20/04/2024",
        "concentracion_particulas_suspendidas": {
          "PM2.5": {
            "valor": 15,
            "unidad": "µg/m³",
            "descripcion": "Partículas finas en el aire con diámetro menor a 2.5 micrómetros."
          },
          "PM10": {
            "valor": 35,
            "unidad": "µg/m³",
            "descripcion": "Partículas en el aire con diámetro menor a 10 micrómetros."
          }
        },
        "concentracion_gases_efecto_invernadero": {
          "CO2": {
            "valor": 420,
            "unidad": "ppm",
            "descripcion": "Dióxido de carbono, principal gas de efecto invernadero."
          },
          "CH4": {
            "valor": 2,
            "unidad": "ppm",
            "descripcion": "Metano, gas de efecto invernadero con alta capacidad de calentamiento."
          },
          "N2O": {
            "valor": 0.4,
            "unidad": "ppm",
            "descripcion": "Óxido nitroso, gas de efecto invernadero con efectos a largo plazo."
          }
        },
        "concentracion_gases_toxicos": {
          "NO2": {
            "valor": 55,
            "unidad": "µg/m³",
            "descripcion": "Dióxido de nitrógeno, gas tóxico que contribuye a la formación de ozono troposférico."
          },
          "SO2": {
            "valor": 25,
            "unidad": "µg/m³",
            "descripcion": "Dióxido de azufre, gas tóxico que puede causar problemas respiratorios."
          },
          "O3": {
            "valor": 190,
            "unidad": "µg/m³",
            "descripcion": "Ozono, gas tóxico en la atmósfera que puede irritar las vías respiratorias."
          }
        },
        "condiciones_meteorologicas": {
          "humedad_relativa": {
            "valor": 70,
            "unidad": "%",
            "descripcion": "Porcentaje de humedad relativa en el aire."
          },
          "temperatura": {
            "valor": 24,
            "unidad": "°C",
            "descripcion": "Temperatura del aire en grados Celsius."
          }
        }
      },
      "ubicacion_3": {
        "fecha": "20/04/2024",
        "concentracion_particulas_suspendidas": {
          "PM2.5": {
            "valor": 10,
            "unidad": "µg/m³",
            "descripcion": "Partículas finas en el aire con diámetro menor a 2.5 micrómetros."
          },
          "PM10": {
            "valor": 25,
            "unidad": "µg/m³",
            "descripcion": "Partículas en el aire con diámetro menor a 10 micrómetros."
          }
        },
        "concentracion_gases_efecto_invernadero": {
          "CO2": {
            "valor": 390,
            "unidad": "ppm",
            "descripcion": "Dióxido de carbono, principal gas de efecto invernadero."
          },
          "CH4": {
            "valor": 1.5,
            "unidad": "ppm",
            "descripcion": "Metano, gas de efecto invernadero con alta capacidad de calentamiento."
          },
          "N2O": {
            "valor": 0.2,
            "unidad": "ppm",
            "descripcion": "Óxido nitroso, gas de efecto invernadero con efectos a largo plazo."
          }
        },
        "concentracion_gases_toxicos": {
          "NO2": {
            "valor": 45,
            "unidad": "µg/m³",
            "descripcion": "Dióxido de nitrógeno, gas tóxico que contribuye a la formación de ozono troposférico."
          },
          "SO2": {
            "valor": 15,
            "unidad": "µg/m³",
            "descripcion": "Dióxido de azufre, gas tóxico que puede causar problemas respiratorios."
          },
          "O3": {
            "valor": 170,
            "unidad": "µg/m³",
            "descripcion": "Ozono, gas tóxico en la atmósfera que puede irritar las vías respiratorias."
          }
        },
        "condiciones_meteorologicas": {
          "humedad_relativa": {
            "valor": 60,
            "unidad": "%",
            "descripcion": "Porcentaje de humedad relativa en el aire."
          },
          "temperatura": {
            "valor": 20,
            "unidad": "°C",
            "descripcion": "Temperatura del aire en grados Celsius."
          }
        }
      }
    },
    "agua": {
      "ubicacion_1": {
        "fecha": "20/04/2024",
        "concentracion_sustancias_quimicas": {
          "pH": {
            "valor": 7.2,
            "unidad": "unitario",
            "descripcion": "Medida de la acidez o alcalinidad del agua."
          },
          "conductividad": {
            "valor": 500,
            "unidad": "µS/cm",
            "descripcion": "Medida de la capacidad del agua para conducir electricidad, relacionada con la concentración de sales."
          },
          "nutrientes": {
            "nitrogeno_total": {
              "valor": 1.5,
              "unidad": "mg/L",
              "descripcion": "Concentración de nitrógeno total en el agua."
            },
            "fosforo_total": {
              "valor": 0.3,
              "unidad": "mg/L",
              "descripcion": "Concentración de fósforo total en el agua."
            }
          }
        },
        "concentracion_microorganismos": {
          "coliformes_totales": {
            "valor": 10,
            "unidad": "CFU/100 mL",
            "descripcion": "Concentración de bacterias coliformes totales en el agua."
          },
          "escherichia_coli": {
            "valor": 0,
            "unidad": "CFU/100 mL",
            "descripcion": "Concentración de Escherichia coli en el agua, indicador de contaminación fecal."
          }
        },
        "niveles_contaminantes": {
          "organicos": {
            "BOD5": {
              "valor": 3.5,
              "unidad": "mg/L",
              "descripcion": "Demanda bioquímica de oxígeno durante 5 días, indicador de materia orgánica biodegradable."
            },
            "COD": {
              "valor": 15,
              "unidad": "mg/L",
              "descripcion": "Demanda química de oxígeno, indicador de la cantidad de materia orgánica total en el agua."
            }
          },
          "inorganicos": {
            "metales_pesados": {
              "plomo": {
                "valor": 0.05,
                "unidad": "mg/L",
                "descripcion": "Concentración de plomo en el agua."
              },
              "cadmio": {
                "valor": 0.01,
                "unidad": "mg/L",
                "descripcion": "Concentración de cadmio en el agua."
              }
            }
          }
        }
      },
      "ubicacion_2": {
        "fecha": "20/04/2024",
        "concentracion_sustancias_quimicas": {
          "pH": {
            "valor": 7.4,
            "unidad": "unitario",
            "descripcion": "Medida de la acidez o alcalinidad del agua."
          },
          "conductividad": {
            "valor": 550,
            "unidad": "µS/cm",
            "descripcion": "Medida de la capacidad del agua para conducir electricidad, relacionada con la concentración de sales."
          },
          "nutrientes": {
            "nitrogeno_total": {
              "valor": 1.8,
              "unidad": "mg/L",
              "descripcion": "Concentración de nitrógeno total en el agua."
            },
            "fosforo_total": {
              "valor": 0.4,
              "unidad": "mg/L",
              "descripcion": "Concentración de fósforo total en el agua."
            }
          }
        },
        "concentracion_microorganismos": {
          "coliformes_totales": {
            "valor": 15,
            "unidad": "CFU/100 mL",
            "descripcion": "Concentración de bacterias coliformes totales en el agua."
          },
          "escherichia_coli": {
            "valor": 1,
            "unidad": "CFU/100 mL",
            "descripcion": "Concentración de Escherichia coli en el agua, indicador de contaminación fecal."
          }
        },
        "niveles_contaminantes": {
          "organicos": {
            "BOD5": {
              "valor": 4,
              "unidad": "mg/L",
              "descripcion": "Demanda bioquímica de oxígeno durante 5 días, indicador de materia orgánica biodegradable."
            },
            "COD": {
              "valor": 18,
              "unidad": "mg/L",
              "descripcion": "Demanda química de oxígeno, indicador de la cantidad de materia orgánica total en el agua."
            }
          },
          "inorganicos": {
            "metales_pesados": {
              "plomo": {
                "valor": 0.07,
                "unidad": "mg/L",
                "descripcion": "Concentración de plomo en el agua."
              },
              "cadmio": {
                "valor": 0.02,
                "unidad": "mg/L",
                "descripcion": "Concentración de cadmio en el agua."
              }
            }
          }
        }
      },
      "ubicacion_3": {
        "fecha": "20/04/2024",
        "concentracion_sustancias_quimicas": {
          "pH": {
            "valor": 7.1,
            "unidad": "unitario",
            "descripcion": "Medida de la acidez o alcalinidad del agua."
          },
          "conductividad": {
            "valor": 480,
            "unidad": "µS/cm",
            "descripcion": "Medida de la capacidad del agua para conducir electricidad, relacionada con la concentración de sales."
          },
          "nutrientes": {
            "nitrogeno_total": {
              "valor": 1.2,
              "unidad": "mg/L",
              "descripcion": "Concentración de nitrógeno total en el agua."
            },
            "fosforo_total": {
              "valor": 0.25,
              "unidad": "mg/L",
              "descripcion": "Concentración de fósforo total en el agua."
            }
          }
        },
        "concentracion_microorganismos": {
          "coliformes_totales": {
            "valor": 8,
            "unidad": "CFU/100 mL",
            "descripcion": "Concentración de bacterias coliformes totales en el agua."
          },
          "escherichia_coli": {
            "valor": 0,
            "unidad": "CFU/100 mL",
            "descripcion": "Concentración de Escherichia coli en el agua, indicador de contaminación fecal."
          }
        },
        "niveles_contaminantes": {
          "organicos": {
            "BOD5": {
              "valor": 3,
              "unidad": "mg/L",
              "descripcion": "Demanda bioquímica de oxígeno durante 5 días, indicador de materia orgánica biodegradable."
            },
            "COD": {
              "valor": 12,
              "unidad": "mg/L",
              "descripcion": "Demanda química de oxígeno, indicador de la cantidad de materia orgánica total en el agua."
            }
          },
          "inorganicos": {
            "metales_pesados": {
              "plomo": {
                "valor": 0.04,
                "unidad": "mg/L",
                "descripcion": "Concentración de plomo en el agua."
              },
              "cadmio": {
                "valor": 0.01,
                "unidad": "mg/L",
                "descripcion": "Concentración de cadmio en el agua."
              }
            }
          }
        }
      }
    }
  }
}

comparar_contaminacion(datos_ejemplo)