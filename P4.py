'''Tipo de dato lista o diccionario'''

mylist= [2021, "Nicolas", ["Silva", "Matute"]]

#print(dir(mylist))

#Metodo append()

print(mylist)
#Despues de modificar con el metodo
mylist.append("Nico")
#Resultado final
print(mylist)

#Metodo clear()
#Borra todo lo que tiene la lista
mylist.clear()
print(mylist)

#Metodo insert()
#Inserta un String o caracter en la posicion que quieras
list1= ['Nicolas', True]
list1.insert(0, "Nico")
print(list1)

#Metodo sort()
list3=[2,4,1,9,3]
list3.sort()
print(list3)
