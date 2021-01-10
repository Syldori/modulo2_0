'''
Funcion que primer nivel -Que devuelva funciones

-Creamos una función que devuelva el nº máximo de los parámetros de entrada
    - tiene que recorrer todos los elementos que le demos y selecciones el más alto
 (*l) > significa que coja todos los parametros separados por comas y los procese como un array
    -Si la longitud del array es 0, return 0
    -Luego coje la posición 0 de los elementos del array para comparar (la llmamos m) y empezamos a recorrer
    -Recorrer: para indice en rango 1 (porque el 0 ya lo ha comprobado) hast ala longitud de la entrada
        -si el elemento en el que estoy es mayor que el máximo (m), máximo será el elemento en el que estoy
        -cuando acabe, devolverá m

-Función que devuelva el nº minimo
-Función que devuelva la media:
    -coger los valores de l, los va metiendo en un acumulador (suma) y lo divide por la longitud de l
    
-Creamos un diccionario con nombres
-Creamos una funcion returnF(nombres)
    -si el nombre existe en funciones, devuelve el valor de funciones del nombre que haya metido
    >>>Esta funcion DEVUELVE UNA FUNCION (ya que si ponemos max, nos devuelve maxi y esta a su vez llama a la funcion maxi
'''

def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m


def media(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for valor in l:
        suma += valor
    return suma/len(l)

funciones = {
    'max' : maxi,
    'min' : mini,
    'med' : media
    }


def returnF (nombre):
    nombre = nombre.lower()# para evitar problemas con mayúsculas
    if nombre in funciones.keys(): #.keys() devuelve las claves
        return funciones[nombre]
    return None # si no encuentra el nombre

#llamamos a la funcion de primer nivel, que nos devuelve como resultado una función
#y si queremos ejecutarla, hay que poner la array con los numeros que queremos que nos devuelva el maximo
print (returnF ('max')(1,3,-1,15,9))
