'''
Conversor de temperatura:

Crear un progrma que convierta temperatura Fh a Celsius y viceversa:
-Formula
    C = (F - 32)*5/9
    F = (C*9/5)+32

-Se puede elegir el tipo de conversion en mayusculas o minusculas
-Reducir el numero de sentencias al minimo y no repetir prints

>> Crea un objeto que sea un conversor de temperatura
    - Clase: Termómetro
        Atributos: unidad de medida (C,F)
                   Temperatura
        Métodos: conversor(self, temperatura, unidad de medida)
        
-no hace falta meterle las variables directamente en el __init__                         
- dentro del conversor meteríamos toda la funcionalidad con las formulas
- hay que poner .upper para que ponga en mayusculas y no de problemas

>>>El problema de esta version es que realmente este objeto no se comporta como uno (bastaría con hacer la funcion conversor y list)
    > para que se comporte más como uno, ver Conversor de temperatura02

!!! - el proceso de crear un objeto es:
         >Que quiero que haga
         >Que variables necesito para que me definan su estado
         >La funcionalidad que quiero
'''

class Termometro():
    def __init__(self):
        self.unidadM = 'C' #podemos poner None o una por defecto
        self.temperatura = 0
    
    def conversor(self, temperatura, unidad):
        if unidad.upper() == 'C':
            return '{}º F'.format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return '{}º C'.format((temperatura -32)*5/9)
        else:
            return 'unidad incorrecta'
        
    def __str__(self):
        return '{}º{}'.format(self.temperatura, self.unidadM)