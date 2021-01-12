'''
La Recursividad
-es la iteración funcional
-es una función que para repetirse, lo que hace es invocarse a si misma
-el primer punto importante de la recursividad es que tiene que llamarse a si misma
-el segundo punto importante es 'cuando paro' > tiene que haber una condición de salida
    >>si no hay una condicion de salida, peta el programa
-No necesita de un acumulador, porque todas las llamadas quedan en espera y la variable que se modifica en cada instancia es local a acada llamada > son distitnta a pesar de tener mismo nombre

-en programación, la recursividad es elegante, pero poco eficiente:
    >>por el problema de crear un bucle infinito y
    >>consume muchos recursos porque tiene reservadas todas la ejecuciones de sumatorio que se han llamado recursivamente 

    
ej. Contador hacia atrás:
    >>def retroContador(entrada):
        print(entrada+',')
        retrocontador (entrada-1)
    > Es recursiva porque se llama a sí misma
    
--PROBLEMA de la recursividad: en el caso del ejemplo crea un bucle infinito
>>Hay que solucionar esto si se usa la recursividad (en el ejemplo hacer que pare si llega a 0)
    -Usamos un if para que se salga cuando llegue a 0 ( ya sea con if e == 0; o if e != 0, o if e > 0 -el de mayor de 0 para evitar problemas al poner nº negativos)

-No se suelen usar mucho >> permite iterar sin necesidad de los operadores vistos
'''

def retroContador(entrada): 
    print('{},'.format(entrada), end = "")
    if entrada == 0:
        return
    retroContador(entrada-1)
    
retroContador(9)

# ejemplo de un sumatorio recursivo
#no podemos aplicar la misma solución porque el return devolvería None y no se puede operar numeros con None 
def sumatorio(n):
    if n > 0: 
        return n + sumatorio(n-1) # retorna el valor más el sumatorio siguiente
    else:
        return 0 # le decimos que retorne 0 para cuando llegue a n = 0. Si no ponemos nada, retorna None y peta 

print (sumatorio(4))