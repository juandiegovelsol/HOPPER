import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Función para cargar el CSV
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return None

# Función para clasificar las columnas del DataFrame
def classify_columns(df):
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    
    return numeric_cols, categorical_cols, datetime_cols

# Función para plotear columnas numéricas
def plot_numeric(df, columns):
    selected_cols = [col for col in columns if col in df.columns]
    
    if not selected_cols:
        print("No se encontraron columnas numéricas coincidentes.")
        return
    
    df[selected_cols].plot(kind='histogram', subplots=True, layout=(2, int(len(selected_cols)/2 + 0.5)), figsize=(15, 10))
    plt.suptitle('Histogramas de Variables Numéricas')
    plt.show()

# Función para plotear columnas categóricas
def plot_categorical(df, columns):
    selected_cols = [col for col in columns if col in df.columns]
    
    if not selected_cols:
        print("No se encontraron columnas categóricas coincidentes.")
        return
    
    for col in selected_cols:
        plt.figure(figsize=(10, 5))
        df[col].value_counts().plot(kind='bar')
        plt.title(f'Frecuencia de Categorías en {col}')
        plt.xticks(rotation=45)
        plt.show()

# Función para plotear columnas de tiempo
def plot_datetime(df, columns):
    selected_cols = [col for col in columns if col in df.columns]
    
    if not selected_cols:
        print("No se encontraron columnas de tiempo coincidentes.")
        return
    
    for col in selected_cols:
        plt.figure(figsize=(15, 5))
        df[col].value_counts().sort_index().plot()
        plt.title(f'Distribución Temporal de {col}')
        plt.xlabel('Tiempo')
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=45)
        plt.show()

# Mock de DataFrame para simulación
def mock_csv_data():
    data = {
        'edad': [23, 45, 31, 35, 22, 33],
        'nombre': ['Alicia', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
        'fecha_compra': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-01', '2021-01-04', '2021-01-05'],
        'monto': [250, 320, 150, 400, 180, 220],
        'estado': ['A', 'B', 'A', 'B', 'A', 'C']
    }
    return pd.DataFrame(data)

# Simular guardar en CSV
def save_mock_csv(df, file_path):
    df.to_csv(file_path, index=False)

# Uso del módulo
if __name__ == "__main__":
    # Crear un DataFrame de prueba
    df_mock = mock_csv_data()
    
    # Guardar el DataFrame en un CSV
    csv_file_path = 'mock_data.csv'
    save_mock_csv(df_mock, csv_file_path)
    
    # Cargar el CSV
    df = load_csv(csv_file_path)
    
    if df is not None:
        # Clasificar las columnas
        numeric_cols, categorical_cols, datetime_cols = classify_columns(df)
        
        # Graficar columnas
        plot_numeric(df, numeric_cols)
        plot_categorical(df, categorical_cols)
        plot_datetime(df, datetime_cols)