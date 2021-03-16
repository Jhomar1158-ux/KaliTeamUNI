'''TIPOS DE DATOS.'''

# Tipo de dato entero: 

var_ent_posi=10
var_ent_nega=-10

#Usamos la función print para imprimiral: 

# print(var_ent_nega) # -10

# Tipo de dato flotante:

var_float_posi=20.0
var_float_nega=-20.3

# Usamos la función print para imprimirlo: 

# print(var_float_nega)#-20.3

var_entera=0
var_flotante=2.2
# Si queremos convertirlo a flotante
var_entera_convertida=float(var_entera)
# print(var_entera_convertida)
# Si queremos convertirlo a entero
var_flotante_convertida=int(var_flotante)
# print(var_flotante_convertida)

''' Si no sabemos de qué tipo de dato hablamos hacemos uso de la función type()'''

print(type(var_entera_convertida))

# print('*'*100)

# Tipo de dato: String 

user_1='Jhomar'
user_2='Elias'
user_3='Cristian'

# Si queremos imprimir hacemos uso de la función print()

# print(user_1)

# Si quieres borrar todo en la terminal haces uso de CTRL + L

'''La función dir() nos muestra las propiedades que queremos hacer con nuestro objeto.'''

# Si por alguna razón no recordamos algún método o método mágico podemos hacer uso de esta función. 
# print(dir(user_1))

# Método upper()
'''Convierte a mayúscula el texto'''
var_1='jhomar'
var_1_upper=var_1.upper()

print(var_1_upper) #JHOMAR

# Métofo lower()
'''Convierte a minúscula el texto'''

var_1_uppertolower=var_1_upper.lower()
print(var_1_uppertolower)

var_member='jhomar astuyauri'

# Método capitalize()
# Convierte la letra inicial a mayúscula de todo el String.
print(var_member.capitalize())

# Método title()
# Convierte las iniciales de cada palabra a String.
print(var_member.title())

# Método replace()
# 

var_user='Cristian Elias'
new_var_user=var_user.replace('Elias','Jhomar')
print(new_var_user)

# Método find()
# Nos brinda la posición del string que buscamos.
print(var_user.find('Elias'))

# -1, es cuando no encuentra el string. 

