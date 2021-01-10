'''
Funciones:

-bloque de código al que le hemos puesto un nombre y unos parámetros (que pueden ser de distintos tipos) (devuelve un resultado)
-Tipos:
    -primera clase: son aquellas que pueden trabajrse con ellas como con los valores/son equivalentes a los datos > es decir pueden asignarse, meterse en funciones, pasarse a otras funciones ...
            

    -Funciones de nivel superior: es aquella que admite funciones en los parametros de entrada o cuyo resultado da una funcion
  >> esto solo lo hacen algunos códigos, como Phyton

'''

def sumaTodos (limiTo):
    resultado = 0
    for i in range (0, limiTo+1):
        # (0, limiTo+1, 2) >> esto haría que sumase solo los pares    
        resultado += i
    return resultado


def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range (limitTo+1): # si no se pone inicio, es 0
        resultado += i*i
    return resultado

print(sumaTodos(100))
print (sumaTodosLosCuadrados(3))

'''
Ejemplo de funcion de primera clase:
    -asignar la funcion a una variable y ahora se puede llamar a esa variable como la función 
    addAll = sumaTodos
    addAll(4)
'''
'''
ejemplo de funcion de nivel superior:
'''




