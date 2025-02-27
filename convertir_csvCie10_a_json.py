import csv
import json

csv_file = 'datos.csv'
json_file = 'cie10.json'

# Leer el CSV y estructurar mejor los datos
datos = []
with open(csv_file, newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';')
    for fila in lector:
        if len(fila) == 3:
            datos.append({
                "codigo": fila[0],
                "grupo": fila[1],
                "segmento": fila[2]
            })

# Escribir los datos en JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

print(f"Se han convertido {len(datos)} registros de CSV a JSON correctamente.")
