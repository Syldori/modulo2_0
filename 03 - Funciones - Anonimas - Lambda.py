'''
Funciones - Anónimas-Lambdaç

-bloque de código sin nombre pero que se peuden situar en sitios que resulta útil (se llaman lambdas)

>Tomando el ejercicio de funciones
    > Imaginemos que queremos ejecutar un usmatodos pero del cubo, en vez de cuadrado:
        -una de las soluciones es hacer una función def cubo con return x**3 (elevado)
        - otra solución es importar la función sumaTodos de funciones 
        >Problema es que tendríamos que crear la funcion cubo
    --Se soluciona utilizando una función anónima (en phyton se llama lambda)
        -Se crea poniendo lambda, ponemos los parametros que queramos (x en este caso), ponemos dos puntos y lo que queremos que haga
            (en nuestro caso, x : x**3 -elevado a 3-
            
lambda (parametros : bloque de código) > el return no se pone, ya devuelve el resultado de la función

tb podemos poner una lambda en una función
    ej: doble = lambda x: x*2
    
    
>>si la función va a ser reutilizable, lo lógico es definir con def y meterla en la base del programa (xk se usa mucho)
    > lambda se usa para ocasiones puntuales y sencillas
'''

from Funciones import sumaTodos

def sumaTodos (limitTo, f): # f va a hacere referencia a la funcion que queremos usar
    resultado = 0
    for i in range (limitTo+1):
        resultado += f(i) # se le suma a resultado el resultado de realizar la funcion normal(i)
    return resultado


print(sumaTodos(3, lambda x: x**3)) # la función que habría que meter es una lambda en este caso

print(sumaTodos(3, lambda x: x*2)) # esto es para que sume del 1 al 3 pero los dobles