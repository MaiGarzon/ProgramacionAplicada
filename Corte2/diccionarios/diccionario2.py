#students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"], "geografia": "juan", 20:[24, 21, 32]}
#print(students_in_classes)

#powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3} #lo que se esta ingresando como palabra clave es una lista, por ello es un error

diccionario_vacio = {}
print(diccionario_vacio)
diccionario_vacio["salas vacias"]=7
print(diccionario_vacio)

animal={"mono":2, "cebra":5 }
print(animal)
animal["gato"]=8
print(animal)


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "No te metas con"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"



drinks =["expresso", "chai", "decaf", "drip"]
caffeine=[65,35,19,75]
zipped_drinks = zip(caffeine, drinks)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

