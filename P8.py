'''
import time
contador =15
while contador > 5 :
    print(contador)
    time.sleep(1)#Tiempo
    contador -=1
'''
'''EJERCICIO: CREAR UN TEMPORIZADOR QUE TENGA DE ENTRADA
LOS MINUTOS Y LOS SEGUNDOS Y QUE IMPRIMA EL DESCENSO DEL TIEMPO HASTA LLEGAR A "00 min:00 seg" '''

# Necesitamos controlar el tiempo
import time 


minutos=int(input('Ingrese el numero de minutos: '))
print(type(minutos))
segundos=int(input('Ingrese el numero de segundos: '))

while minutos*60+segundos: #90s
    time.sleep(0.01)
    segundos-=1#89s
    Total_segundos=minutos*60+segundos #89s
    if Total_segundos < 60:
        minutos, segundos=divmod(Total_segundos,60)
    print(f'{minutos}min: {segundos}seg')



