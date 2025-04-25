import pandas as pd
import json
import os

# Función para generar datos falsos de prueba
def generar_datos_falsos(num_filas=300):
    datos = {
        'id_diseno': range(1, num_filas + 1),
        'cliente': [f'Cliente {i}' for i in range(1, num_filas + 1)],
        'tamaño': ['Media carta', 'A4', 'Volante'] * 10 + ['A5', 'B6'] * 5,
        'impresion': ['Offset', 'Digital', 'Impresión Flexo'] * 10 + ['Serigrafía'] * 5,
        'colores': [4, 3, 2] * 15 + [1, 5],
        'elementos': ['textos', 'imagenes', 'textos, imagenes'] * 20,
        'imagenes_listas': [True, False, True] * 15 + [True, False],
        'mensaje': [f'¡Oferta especial!' for _ in range(20)] + [f'Nuevo producto disponible!' for _ in range(10)] + [f'Evento importante'] * 5,
        'publico_objetivo': [
            'Familias jóvenes con niños de 0 a 5 años',
            'Amantes de la tecnología',
            'Personas interesadas en el fitness',
            'Viajeros',
            'Profesionales'
        ] * 10 + ['Otros'] * 5,
        'marca_logotipo': [f'Logo {i}' for i in range(1, 6)],
        'marca_colores': ['azul, rojo', 'verde, amarillo', 'naranja, gris'] * 10 + ['negro, blanco'] * 5,
        'estilo': ['Colorido y divertido', 'Elegante y moderno', 'Motivador'] * 10 + ['Minimalista'] * 5,
        'textos': [f'Texto {i}' for i in range(1, 21)],
        'llamada_a_la_accion': ['Visita nuestro sitio', 'Compra ahora', 'Únete a nosotros'] * 10 + ['Descubre más'] * 5,
        'contacto_telefono': ['123-456-7890', '987-654-3210'] * 10 + ['555-555-5555'],
        'contacto_email': ['info@ejemplo.com'] * 10 + ['contacto@ejemplo.com'],
        'ruta_imagen': [f'./imagenes/diseno{i}.jpg' for i in range(1, num_filas + 1)],
        'enviar_a_otro_disenador': [True, False] * 30
    }
    return pd.DataFrame(datos)

# Función para filtrar y agrupar los diseños por público objetivo y tipo de impresión
def filtrar_y_agrupar_disenos(df):
    df['tamaño'] = df['tamaño'].map({'Media carta': 'M', 'A4': 'A', 'Volante': 'V', 'A5': 'A5', 'B6': 'B6'})
    grouped = df.groupby(['publico_objetivo', 'impresion', 'tamaño']).agg({
        'id_diseno': 'first',
        'cliente': 'first',
        'detalles_flyer': 'last',
        'contenido_flyer': 'last',
        'ruta_imagen': 'last'
    }).reset_index()
    return grouped

# Función para convertir el DataFrame a JSON
def df_a_json(df, nombre_archivo):
    grouped_data = df.groupby('publico_objetivo').apply(lambda x: list(x.to_dict(orient='records')))
    resultado = {publico: flyers for público, flyers in grouped_data.items()}
    with open(nombre_archivo, 'w') as f:
        json.dump(resultado, f, indent=4)

# Función principal
def main():
    # Generar datos falsos si no existe el directorio de imágenes
    imagenes_dir = './imagenes'
    if not os.path.exists(imagenes_dir):
        os.makedirs(imagenes_dir)

    # Generar datos falsos de prueba
    df = generar_datos_falsos()

    print(df)

    # Filtrar y agrupar los diseños
    df_agrupado = filtrar_y_agrupar_disenos(df)

    # Seleccionar solo los diseños con impresión 'Offset'
    df_filtrado = df_agrupado[df_agrupado['impresion'] == 'Offset']

    # Convertir al JSON
    nombre_archivo_json = 'disenos_filtrados.json'
    df_a_json(df_filtrado, nombre_archivo_json)

    print(f'Archivo JSON generado exitosamente: {nombre_archivo_json}')

if __name__ == "__main__":
    main()