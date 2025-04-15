import pandas as pd
from scipy import stats
import json

def analizar_precipitaciones(archivo_csv, archivo_resultados):
    try:
        # Cargar datos históricos y de 2023
        datos_historicos = pd.read_csv(archivo_csv)
        datos_2023 = pd.read_csv(archivo_csv)
        
        # Verificar que los archivos tengan las mismas columnas
        columnas_esperadas = {"fecha", "estacion", "milimetros_lluvia", "duracion_horas"}
        if not columnas_esperadas.issubset(datos_historicos.columns).issubset(datos_2023.columns):
            raise ValueError("Los archivos CSV no contienen las columnas esperadas.")
        
        # Convertir la columna de fecha a datetime
        datos_historicos['fecha'] = pd.to_datetime(datos_historicos['fecha'])
        datos_2023['fecha'] = pd.to_datetime(datos_2023['fecha'])
        
        # Agrupar por estación y año, y calcular promedios
        promedios_historicos = datos_historicos.groupby(['estacion', 'fecha.year'])[['milimetros_lluvia', 'duracion_horas']].agg({
            'milimetros_lluvia': 'mean',
            'duracion_horas': 'mean'
        }).reset_index()
        
        promedios_2023 = datos_2023.groupby(['estacion'])[['milimetros_lluvia', 'duracion_horas']].agg({
            'milimetros_lluvia': 'mean',
            'duracion_horas': 'mean'
        }).reset_index()
        
        # Calcular diferencias significativas usando t-test
        diferencias_significativas = {}
        for _, grupo in promedios_historicos.groupby('estacion'):
            media_hist, std_hist = grupo['milimetros_lluvia'].mean(), grupo['milimetros_lluvia'].std()
            media_2023 = promedios_2023[promedios_2023['estacion'] == grupo['estacion']]['milimetros_lluvia'].mean()
            t_stat, p_valor = stats.ttest_ind(grupo['milimetros_lluvia'], promedios_2023[promedios_2023['estacion'] == grupo['estacion']]['milimetros_lluvia'])
            diferencias_significativas[grupo['estacion']] = {
                'media_hist': media_hist,
                'std_hist': std_hist,
                'media_2023': media_2023,
                't_stat': t_stat,
                'p_valor': p_valor,
                'hay_diferencia': p_valor < 0.05
            }
        
        # Crear el diccionario de resultados
        resultados_2023 = {
            'mm_lluvia': promedios_2023[['estacion', 'milimetros_lluvia']].to_dict('records'),
            'horas_lluvia': promedios_2023[['estacion', 'duracion_horas']].to_dict('records')
        }
        
        hay_diferencia_significativa = any(d['hay_diferencia'] for d in diferencias_significativas.values())
        
        resultados_finales = {
            "mm_lluvia_historico": promedios_historicos[['estacion', 'milimetros_lluvia']].to_dict('records'),
            "horas_lluvia_historico": promedios_historicos[['estacion', 'duracion_horas']].to_dict('records'),
            "resultados_2023": resultados_2023,
            "hay_diferencia_significativa": hay_diferencia_significativa
        }
        
        # Guardar los resultados en un archivo JSON
        with open(archivo_resultados, 'w') as f:
            json.dump(resultados_finales, f, indent=4)
        
        print(f"Análisis completado y guardado en {archivo_resultados}")
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no se encontró.")
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejemplo de uso
archivo_csv = 'datos_precipitaciones.csv'
archivo_resultados = 'resultados_analisis.json'
analizar_precipitaciones(archivo_csv, archivo_resultados)issubset