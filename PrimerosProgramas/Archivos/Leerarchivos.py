#m=open("leerarchivo.txt", "r") #open es para abrir el achivo, en este caso el archivo se llama leerarchivo y es
#un txt, el "r" es para indicar que se va a leer (read)
#print(m.readline()) #con esto nos lee la primera linea
#para leer todas las lineas del archivo :
m=open("leerarchivo.txt", "r")
for x in m:
  print(x)
m.close