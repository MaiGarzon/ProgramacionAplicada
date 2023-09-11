import random
import csv

# Especifica el nombre del archivo CSV en el que deseas escribir los números
nombre_archivo_csv = 'numeros.csv'

while True:
    # Genera un número pseudoaleatorio en el rango (0, 1)
    numero_pseudoaleatorio = random.uniform(0, 1)

    # Abre el archivo CSV en modo de escritura y agrega el número generado
    with open(nombre_archivo_csv, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([numero_pseudoaleatorio])

    print(f'Se ha escrito el número {numero_pseudoaleatorio} en el archivo {nombre_archivo_csv}.')

    # Opcional: puedes agregar una condición de salida si lo deseas
    # Para detener el bucle, puedes presionar Ctrl+C en la consola.

# Este código se ejecutará infinitamente hasta que lo detengas manualmente.
