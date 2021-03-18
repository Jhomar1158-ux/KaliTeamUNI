
'''BUCLES'''

# Importamos el modulo time
import time 

# Bucle while

items=[]

while True:
    print('Jhomar')
    items.append('Astuyauri')
    print(len(items))
    if len(items) > 100:
        break
'''
# CTRL + C: Interrumpe el intérprete de Py


for n in range(5):
    if n==2:
        # Un semibreak
        continue      
    print(n)

list_1=list(range(20))  #Tenemos 20 términos

while len(list_1)>10:
    print(list_1)
    list_1.pop()
print('chema es kbro')
'''
''' Ejemplo: Contador'''

contador =15
while contador > 5 :
    print(contador)
    time.sleep(1)#Tiempo
    contador -=1
    













