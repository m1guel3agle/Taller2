import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('movies_initial.csv')

# Convertir a JSON
df.to_json('movies.json', orient='records', indent=4)

print("Archivo movies.json creado correctamente.")