# Nombre del archivo que deseas crear
nombre_archivo = "hola.txt"

# Contenido que deseas escribir en el archivo
contenido = "Este es el contenido que se escribirá en el archivo de texto."

# Abre el archivo en modo escritura ("w" significa escribir)
with open(nombre_archivo, "w") as archivo:
    archivo.write(contenido)

print(f"Se ha creado el archivo '{nombre_archivo}' con el contenido deseado.")
