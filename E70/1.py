import pandas as pd
import json
import os

def generar_datos_falsos(num_filas=300):
    """
    Genera datos falsos de prueba para un archivo CSV con 300 filas.
    """
    datos_falsos = {
        'id_diseno': range(1, num_filas + 1),
        'cliente': ['Cliente A', 'Cliente B', 'Cliente C', ...],
        'tamaño': ['Media carta', 'A4', 'Volante', ...],
        'impresion': ['Offset', 'Digital', 'Offset', ...],
        'colores': [3, 4, 2, ...],
        'elementos': ['textos', 'imagenes', 'textos, imagenes', ...],
        'imagenes_listas': [True, False, True, ...],
        'mensaje': [f'Nuevo producto!', 'Evento importante', 'Promoción especial', ...],
        'publico_objetivo': ['Jóvenes adultos', 'Familias', 'Niños', ...],
        'marca_logotipo': ['Logo1', 'Logo2', 'Logo3', ...],
        'marca_colores': ['Rojo, azul', 'Verde, blanco', 'Naranja, negro', ...],
        'estilo': ['Moderno', 'Clásico', 'Casual', ...],
        'textos': [f'Descubre más', 'Ven a conocer', 'Oferta exclusiva', ...],
        'llamada_a_la_accion': ['Visita nuestro sitio', 'Reserva ahora', 'Compra ahora', ...],
        'contacto_telefono': [f'123-456-{i}', f'987-654-{i}', f'555-555-{i}', ...],
        'contacto_email': [f'contacto{i}@ejemplo.com', f'info{i}@ejemplo.com', f'venta{i}@ejemplo.com', ...],
        'ruta_imagen': f'./imagenes/diseno{i}.jpg' for i in range(1, num_filas + 1)],
        'enviar_a_otro_disenador': [True, False, True, ...]
    }
    
    df = pd.DataFrame(datos_falsos)
    return df

def filtrar_y_agrupar_por_publico(df):
    """
    Filtra los diseños por impresión 'Offset' y agrupa por el público objetivo.
    """
    df_filtrado = df[df['impresion'] == 'Offset']
    agrupado = df_filtrado.groupby('publico_objetivo').apply(lambda x: {
        'publico_objetivo': x['publico_objetivo'].values[0],
        'flyers': [
            {
                'id_diseno': row['id_diseno'],
                **row.to_dict()
            }
            for _, row in x.iterrows()
        ]
    })
    return agrupado

def csv_a_json(input_csv, output_json):
    """
    Lee un archivo CSV, lo filtra, agrupa y exporta los datos a un archivo JSON.
    """
    try:
        # Generar datos falsos si el archivo CSV no existe
        if not os.path.exists(input_csv):
            print(f"El archivo {input_csv} no existe. Generando datos falsos.")
            df = generar_datos_falsos()
        else:
            df = pd.read_csv(input_csv)
        
        # Filtrar y agrupar los datos
        resultado = filtrar_y_agrupar_por_publico(df)
        
        # Convertir el resultado a formato JSON
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=4, ensure_ascii=False)
        
        print(f"Datos exportados exitosamente a {output_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
input_csv = 'datos.csv'
output_json = 'flyers.json'
csv_a_json(input_csv, output_json)