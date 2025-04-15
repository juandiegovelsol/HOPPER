import pandas as pd

# Creamos un DataFrame de ejemplo
data = {
    'cliente': ['Ana', 'Luis', 'María', 'Pedro'],
    'servicios_solicitados': [
        'internet',    # set con 2 servicios
        'tv',                       # set con 1 servicio
        'internet',                   # string, no es set
    ]
}

df = pd.DataFrame(data)

# Aplicamos la función corregida
df['tendencia_consumo'] = df['servicios_solicitados'].apply(lambda x: len(x) if isinstance(x, set) else 0)

print(df)
