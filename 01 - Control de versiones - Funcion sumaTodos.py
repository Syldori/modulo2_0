'''

ejemplo para probar el control de verisones con GitHub

funcion que sume todos los numeros entre 0 y limiTo (numero que queramos)
'''

def sumaTodos (limiTo):
    resultado = 0
    for i in range (0, limiTo+1):
        # (0, limiTo+1, 2) >> esto haría que sumase solo los pares    
        resultado += i
    return resultado

print(sumaTodos(100))