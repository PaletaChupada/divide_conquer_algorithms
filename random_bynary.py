'''
Titulo: Busqueda binaria aleatoria recursiva
Nombre: Daniel Espinoza Bautista
Descripcion: Este programa realiza la busqueda binaria a partir de una posicion media generada aleatoriamente, con llamadas recursivas
'''

import numpy as np
from time import time

# Funcion para generar un numero aleatorio a partir de los
# numeros que nos den como parametros
import random
def obtRandom(x,y):
    tmp=(x + random.randint(0,100000) % (y-x+1))
    return tmp
     
# Funcion recursiva de busqueda binaria aleatoria
# Regresa la posicion del valor
# en un arreglo dado, si no se encuentra regresa un -1
 
def randomBusquedaBin(arr,l,r,x) :
    if r>=l:
        # Definimos la posicion media con un numero random entre 0
        # Y el valor total de numeros en el arreglo
        mid=obtRandom(l,r)
         
        # Si el elemento esta en la mitad, regresamos esta posicion
        if arr[mid] == x:
            return mid
             
        # Si el elemento es menor a la mitad, entonces buscamos solo 
        # en la parte izquierda del arreglo
        if arr[mid]>x:
            return randomBusquedaBin(arr, l, mid-1, x)
             
        # Si no se cumple la condicion de arriba, entonces buscamos
        # en la parte derecha del arreglo 
        return randomBusquedaBin(arr, mid+1,r, x)
         
    # Si el elemento no se encuentra, regresamos -1
    return -1
     
# Solicitamos el valor de la posicion a buscar y le restamos 1
print("Elemento a buscar: ")
pos = int(input())
pos = pos-1

# Inicializamos el arreglo de numeros
numeros = []

# Leemos los numeros del archivo, y lo agregamos a un arreglo
arch = np.loadtxt("./numeros.txt", dtype="str", delimiter=" ")

# Inicializamos la variable para el ciclo
i=0

# Mediante el ciclo convertimos el arreglo a enteros para
# poder trabajar de una manera mas eficiente con el
while i<len(arch)-1:
    aux = int(arch[i])
    numeros.append(aux)
    i+=1

# Ordenamos el arreglo
numeros.sort()

# Inicializamos la variable tiempo_in que nos ayudara a
# contar el tiempo de ejecucion del programa
tiempo_in = time()

# Llamamos a la funcion
posicion = randomBusquedaBin(numeros, 0, len(numeros)-1, pos)

# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in

# Realizamos la evaluacion de la posicion
if posicion==-1:
    print("No se encontro el elemento")
else:
    print("Elemento encontrado en la posicion:", posicion+1)

# Imprimimos el tiempo de ejecucion
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)
         