import random
import csv

# Especificar el nombre del archivo CSV en el que se desea escribir los números
nombre_archivo_csv = 'numeros.csv'

while True:
    # Generar un número pseudoaleatorio en el rango (0, 1)
    numero_pseudoaleatorio = random.uniform(0, 1)

    # Abrir el archivo CSV en modo de escritura y agregar el número generado
    with open(nombre_archivo_csv, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([numero_pseudoaleatorio])

    print(f'Se ha escrito el número {numero_pseudoaleatorio} en el archivo {nombre_archivo_csv}.')
# Para detener el bucle, se puede presionar Ctrl+C en la consola.
# Este código se ejecutará infinitamente hasta que se detenga manualmente
