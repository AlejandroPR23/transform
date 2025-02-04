import csv
import json

# Nombre del archivo CSV de entrada y el archivo JSON de salida
csv_file = 'datos.csv'
json_file = 'cie10.json'

# Leer el CSV y almacenar los datos en una lista de diccionarios
with open(csv_file, newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    datos = list(lector)

# Escribir los datos en el archivo JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

print(f"Se han convertido {len(datos)} registros de CSV a JSON correctamente.")
