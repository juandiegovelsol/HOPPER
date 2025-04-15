import polars as pl
import json

# Datos de ciudades
ciudades_usa_json = '''
[
    {"nombre": "Nueva York", "poblacion": 8468000, "estado": "Nueva York"},
    {"nombre": "Los Ángeles", "poblacion": 3849000, "estado": "California"},
    {"nombre": "Chicago", "poblacion": 2697000, "estado": "Illinois"},
    {"nombre": "Houston", "poblacion": 2288000, "estado": "Texas"},
    {"nombre": "Phoenix", "poblacion": 1645000, "estado": "Arizona"},
    {"nombre": "Filadelfia", "poblacion": 1576000, "estado": "Pensilvania"},
    {"nombre": "San Antonio", "poblacion": 1493000, "estado": "Texas"},
    {"nombre": "San Diego", "poblacion": 1383000, "estado": "California"},
    {"nombre": "Dallas", "poblacion": 1318000, "estado": "Texas"},
    {"nombre": "San José", "poblacion": 1013000, "estado": "California"}
]
'''

def main():
    try:
        ciudades = pl.from_dicts(json.loads(ciudades_usa_json))
        
        ciudades = ciudades.with_columns(
            pl.col("poblacion").apply(
                lambda p: (
                    "Metrópolis" if p >= 5000000 
                    else "Gran ciudad" if p >= 1000000 
                    else "Ciudad mediana"
                )
            ).alias("categoria")
        )
        
        ciudades = ciudades.with_columns(
            pl.struct(["poblacion", "nombre"]).apply(
                lambda x: (
                    f"Alta densidad ({x['nombre']})" 
                    if x["poblacion"] > 2000000 
                    else f"Media densidad ({x['nombre']})"
                )
            ).alias("densidad_categoria")
        )
        def formato_presentacion(poblacion, nombre):
            return f"{nombre.upper()}: {poblacion/1000000:.1f}M hab."
            
        ciudades = ciudades.with_columns(
            pl.struct(["poblacion", "nombre"]).apply(
                lambda x: formato_presentacion(x["poblacion"], x["nombre"])
            ).alias("presentacion")
        )
        
        print("Ciudades con categorización:")
        print(ciudades.select(["nombre", "poblacion", "categoria", "densidad_categoria", "presentacion"]))
        
        ciudades.write_csv("ciudades_analizadas.csv")
        print("\nDatos guardados en 'ciudades_analizadas.csv'")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()