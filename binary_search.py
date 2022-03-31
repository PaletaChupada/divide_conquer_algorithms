'''
Titulo: Busqueda binaria recursiva
Nombre: Daniel Espinoza Bautista
Descripcion: Este programa realiza la busqueda binaria recursiva a partir de una posicion media 
'''

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
 
arr = [2, 3, 4, 10, 40]
x = 10
 
# Llamamos a la funcion
posicion = busquedaBinaria(arr, 0, len(arr)-1, x)
 
# Realizamos la evaluacion de la posicion
if posicion != -1:
    print("Elemento presente en el indice % d" % posicion)
else:
    print("No se encontro el elemento en el array")