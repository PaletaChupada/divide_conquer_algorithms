'''
Titulo: Busqueda binaria aleatoria recursiva
Nombre: Daniel Espinoza Bautista
Descripcion: Este programa realiza la busqueda binaria a partir de una posicion media generada aleatoriamente, con llamadas recursivas
'''

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
     
arr = [2, 3, 4, 10, 40]
n=len(arr)
x=10

# Llamamos a la funcion
posicion = randomBusquedaBin(arr, 0, n-1, x)

# Realizamos la evaluacion de la posicion
if posicion==-1:
    print('No se encontro el elemento')
else:
    print('Elemento encontrado en el array', posicion)
         