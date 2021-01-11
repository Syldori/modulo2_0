'''

Operadores map, filter y reduce:

-map: realiza una operación sobre cada uno de los items de entrada
     >> map (operacion a realizar/funcion, parametro sobre el que se va a hacer la operacion)
    
    
-filter: aplica un filtro y comprueba, aplicando una condicion sobre un parametro, si es True. Devuelve aquellos resultados que den True, ignora los otros
    > filter (condicion de filtrado como lambda/funcion, parametro sobre el que aplica)
    -devuelve aquello que cumpla la condición, guradándolo 
    >>ej de abajo> me vas a filtrar de todos los numeros que entre, solo me devuelves aquellos que cumplan la siguiente condicion:
        -que el resto de x partido de 2 sea igual a 0, y se lo aplica a lista
    >>esto sería el equivalente de hacer esta funcion
        def f(x):
            if x%2 == 0:
                return x
            else:
                return None
     >> en vez de lambda, se podría poner una funcion (siempre y cuando devuelva True o False, ya que filter comprueba con esos dos):
       ej:  def esPar(x):
             return x % 2 == 0
      - listaPares = filter (esPar, lista)


-reduce: sobre una lista, va  a procesar un por uno sus valores y los transforma en un unico valor:
    -para usar reduce hay que hacer import: from functools import reduce
    >> reduce todo a un valor >> hay que poner
    reduce(operacion
    -ej. un sumaTodos con reduce:
        reduce(lambda de dos parametros que van a sumarse, lista sobre la que se aplica la operacion)
        >reduce(lambda x, y: x+y, lista)
        -- x sería el valor de acumulado(que me va a devolver el reduce) - empieza x= 1, y = 3> suma ambos, y ahora x es 4 e y -1, suma y el 3 es x, y es el 9 etc
    -ej: sumar numeros del 1 al 100 >> misma funcion lambda de suma, ponemos range(101) para que coja todos los numeros entre 0 y 100 -si no ponemos una entrada en range, empieza desde 0
    
        
'''

from functools import reduce

lista = (1,3,-1,15,9)

listadobles = map (lambda x: x*2, lista) # esto sería sobre lista, se realiza el doble de cada uno
print (list(listadobles))

listaPares = filter (lambda x: x%2==0, lista)
print (list(listaPares)) # da una lista vacía en este caso porque ninguno da resto 0

sumatorio = reduce(lambda x, y: x+y, lista)
print (sumatorio)

suma100 = reduce(lambda x,y: x+y, range(101))
print(suma100)

sumatorioDobles = reduce (lambda x, y: x+y*2, lista)
print (sumatorioDobles) # problema de esta es que como hace los dobles a partir de y, y no dobla la x