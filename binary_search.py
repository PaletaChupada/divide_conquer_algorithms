'''
Titulo: Busqueda binaria recursiva
Nombre: Daniel Espinoza Bautista
Descripcion: Este programa realiza la busqueda binaria recursiva a partir de una posicion media 
'''

import numpy as np
from time import time

def busquedaBinaria(arr, l, r, x):
    
    # Obtenemos el caso base
    if r >= l:
 
        # Calculamos la mitad del arreglo
        mid = l + (r - l) // 2
 
        # Si el elemento esa en la posicion media, regresamos esta posicion
        if arr[mid] == x:
            return mid
 
        # Si el elemento es menor a la mitad, entonces buscamos solo 
        # en la parte izquierda del arreglo
        elif arr[mid] > x:
            return busquedaBinaria(arr, l, mid-1, x)
 
        # Si no se cumple la condicion de arriba, entonces buscamos
        # en la parte derecha del arreglo 
        else:
            return busquedaBinaria(arr, mid + 1, r, x)
 
    else:
        # Regresamos -1 si el elemento no se encontro en el arreglo
        return -1
 
# Solicitamos el valor de la posicion a buscar y le restamos 1
print("Elemento a buscar: ")
pos = int(input())

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
posicion = busquedaBinaria(numeros, 0, len(numeros)-1, pos)
 
# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in

# Realizamos la evaluacion de la posicion
if posicion != -1:
    print("Elemento presente en la posicion:",posicion+1)
else:
    print("No se encontro el elemento en el array")

# Imprimimos el tiempo de ejecucion
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)