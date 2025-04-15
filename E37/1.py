import json
from collections import defaultdict, Counter

def analizar_festival(datos_json):
    # Deserializar los datos JSON
    bandas = datos_json["bandas"]
    horarios_de_actuacion = datos_json["horarios_de_actuacion"]
    preferencias_del_público = datos_json["preferencias_del_público"]
    
    # Calcular popularidad de cada banda
    popularidad_bandas = {}
    for banda in bandas:
        popularidad_bandas[banda["id"]] = 0
    
    for preferencia in preferencias_del_público:
        for banda_id in preferencia["bandas_favoritas"]:
            popularidad_bandas[banda_id] += 1
    
    # Ordenar bandas por popularidad
    bandas_ordenadas = sorted(popularidad_bandas.items(), key=lambda x: x[1], reverse=True)
    
    # Optimizar horarios de actuaciones
    horario_optimizado = []
    
    # Ordenar horarios por popularidad de las bandas
    for horario in horarios_de_actuacion:
        banda_id = horario["id_banda"]
        popularidad = popularidad_bandas[banda_id]
        
        # Si hay suficientes asistentes para que la banda tenga su propio escenario, asignarla
        if popularidad >= 3:  # Suponiendo que 3 asistentes son suficientes
            horario_optimizado.append(horario)
        else:
            # Si no hay suficientes asistentes, la banda actúa en el escenario secundario
            horario_optimizado.append({
                "id": horario["id"],
                "id_banda": banda_id,
                "escenario": "Escenario Secundario",
                "fecha": horario["fecha"],
                "hora_inicio": horario["hora_inicio"],
                "duracion": horario["duracion"]
            })
    
    # Identificar géneros musicales más populares
    generos_populares = Counter(pref["generos_musicales_favoritos"] for pref in preferencias_del_público)
    top_generos = generos_populares.most_common()
    
    return {
        "bandas_popularidad": bandas_ordenadas,
        "horario_optimizado": horario_optimizado,
        "generos_populares": top_generos
    }

# Ejemplo de uso
datos_json = {
  "bandas": [
    {
      "id": 1,
      "nombre": "Rockers Unidos",
      "genero_musical": "Rock",
      "numero_miembros": 4,
      "contacto_principal": {
        "nombre": "Juan Pérez",
        "telefono": "+56987654321",
        "correo_electronico": "juan.perez@rockersunidos.com"
      }
    },
    {
      "id": 2,
      "nombre": "Bailarines de Jazz",
      "genero_musical": "Jazz",
      "numero_miembros": 3,
      "contacto_principal": {
        "nombre": "María López",
        "telefono": "+56987654322",
        "correo_electronico": "maria.lopez@bailarinesdejazz.com"
      }
    },
    {
      "id": 3,
      "nombre": "Hip Hop Crew",
      "genero_musical": "Hip Hop",
      "numero_miembros": 5,
      "contacto_principal": {
        "nombre": "Carlos Martínez",
        "telefono": "+56987654323",
        "correo_electronico": "carlos.martinez@hiphopcrew.com"
      }
    },
    {
      "id": 4,
      "nombre": "Pop Stars",
      "genero_musical": "Pop",
      "numero_miembros": 6,
      "contacto_principal": {
        "nombre": "Ana Gómez",
        "telefono": "+56987654324",
        "correo_electronico": "ana.gomez@popstars.com"
      }
    },
    {
      "id": 5,
      "nombre": "Rock en Vivo",
      "genero_musical": "Rock",
      "numero_miembros": 4,
      "contacto_principal": {
        "nombre": "Luis Fernández",
        "telefono": "+56987654325",
        "correo_electronico": "luis.fernandez@rockenvivo.com"
      }
    }
  ],
  "horarios_de_actuacion": [
    {
      "id": 1,
      "id_banda": 1,
      "escenario": "Escenario Principal",
      "fecha": "2024-11-15",
      "hora_inicio": "19:00",
      "duracion": 60
    },
    {
      "id": 2,
      "id_banda": 2,
      "escenario": "Escenario Secundario",
      "fecha": "2024-11-15",
      "hora_inicio": "20:00",
      "duracion": 45
    },
    {
      "id": 3,
      "id_banda": 3,
      "escenario": "Escenario Principal",
      "fecha": "2024-11-15",
      "hora_inicio": "21:00",
      "duracion": 90
    },
    {
      "id": 4,
      "id_banda": 4,
      "escenario": "Escenario Secundario",
      "fecha": "2024-11-15",
      "hora_inicio": "22:00",
      "duracion": 75
    }
  ],
  "preferencias_del_publico": [
    {
      "id": 1,
      "id_asistente": 101,
      "nombre_asistente": "Carlos García",
      "bandas_favoritas": [
        1,
        5
      ],
      "generos_musicales_favoritos": [
        "Rock",
        "Hip Hop"
      ]
    },
    {
      "id": 2,
      "id_asistente": 102,
      "nombre_asistente": "Ana Rodríguez",
      "bandas_favoritas": [
        2,
        3
      ],
      "generos_musicales_favoritos": [
        "Jazz",
        "Pop"
      ]
    },
    {
      "id": 3,
      "id_asistente": 103,
      "nombre_asistente": "Luis Pérez",
      "bandas_favoritas": [
        4,
        1
      ],
      "generos_musicales_favoritos": [
        "Pop",
        "Rock"
      ]
    },
    {
      "id": 4,
      "id_asistente": 104,
      "nombre_asistente": "María López",
      "bandas_favoritas": [
        5,
        2
      ],
      "generos_musicales_favoritos": [
        "Rock",
        "Jazz"
      ]
    },
    {
      "id": 5,
      "id_asistente": 105,
      "nombre_asistente": "Javier Martínez",
      "bandas_favoritas": [
        3,
        4
      ],
      "generos_musicales_favoritos": [
        "Hip Hop",
        "Pop"
      ]
    }
  ]
}


print(analizar_festival(datos_json))
            