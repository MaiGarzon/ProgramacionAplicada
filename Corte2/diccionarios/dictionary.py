
diccionario={"Nombre":"Maira","Apellido":"Garzon"}.get("Nombre")#Devuelve unicamente el valor de la palabra clave seleccionado.
#Si en la funcion get() la palabra clave no esta presente en el diccionario, se arrojara un valor vacio:none
print(diccionario)

dict1={'color': 'blue', 'shape': 'circle'} 
dict2={'color':'red', 'number':42}
print("before: ",dict1)
dict1.update(dict2)
print("after: ", dict1) #el diccionario 2 actualiza al diccionario 1, la forma se conseva


#Imprimir las palabras calve dentro de un diccionario
new_dict={"A":"Ave","T":"Tucan","V":"Vaca"}
print(new_dict.keys())
#Imprimir en forma de tuplas, los valores dentro del diccionario
print(new_dict.items())

