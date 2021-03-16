''' Tipo de dato: diccionario'''

json_jhomasterizado = {
    # Argumentos o items
    #clave    #valor
    "name":"Sebastian",
    "lastname":"Nizama",
    "Age":20,
    "DNI":77148832,
    "email": "sebaf79@hotmail.com",
    "lenguajes_progra":['python','javascript','c','m'],
}

print(json_jhomasterizado)

#Metodo copy()
json_jhomasterizado_NEW = json_jhomasterizado.copy()
print(json_jhomasterizado_NEW)


# SI QUEREMOS AGREGAR UN NUEVO ITEAM A NUESTRO DICCIONARIO
json_jhomasterizado['celular'] = 991600210
print(json_jhomasterizado)
print(json_jhomasterizado_NEW)

#print(dir(json_jhomasterizado))
print("#"*100)
print(json_jhomasterizado.keys())