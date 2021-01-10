'''
Ejemplo de funcion de nivel superior/primer nivel:
Usando funciones como parámetros de entrada > la funcion irá solo por su nombre, y cuando se ejecuta dentro, se le pone el parametro de entrada

-Funcion que haga lo mismo que las anteriores:
    1º-definimos una funcion y le decimos los parametros (uno es el nombre la funcion)
    2º- hacemos como una funcion normal
    3º - f(i) : aplicacion de la funcion f sobre i >> i sería el parámetro de la función normal en este caso
    4º - llamamos la funcion sumaTodos y donde estaba f, se pone el nombre de la funcion

>> hay que asegurarse que no devuelva nada extraño como una cadena.
'''


def normal (x):
    return x

def cuadrado (y):
    return y * y

def sumaTodos (limitTo, f): # f va a hacere referencia a la funcion que queremos usar
    resultado = 0
    for i in range (limitTo+1):
        resultado += f(i) # se le suma a resultado el resultado de realizar la funcion normal(i)
    return resultado

print (sumaTodos(100, normal)) #ahora en f(i), sería normal(i)
print (sumaTodos(3, cuadrado))