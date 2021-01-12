'''
Ejercicio:
hacer con funcion recursiva el factorial de n (multiplicar todos los nº entre n y 1)

ej: factorial de 5 > 5*4*3*2*1 = 120

'''

def factorial(n):
    if n != 0: 
        return n * factorial(n-1) # retorna el valor más el sumatorio siguiente
    else:
        return 1
    
print(factorial(5))