'''
Crear nuestro primer objeto:

-Será un perro
    Variables que definen su estado/Atributos:
        -nombre
        -peso
        -edad
    --Funcionalidad/ Método ladrar()

    >>Se crearán tres instancias: ej
        -miko = Perro('Miko', 8, 3)
Creación:
1º- se define la clase, con class Nombre():
    >> el nombre de la clase siempre con mayuscula
2º- Una clase siempre tiene por necesidad la función constructora __init__
    >>cuando yo diga esta variable es igual a Perro con estos parámetros, esta función se hace cargo de hacer esto
3º - Phyton sabe que una clase va a tener una funcion constructora y genera una clase vacia sin ningun atributo (que es self, ella misma, Perro en este caso)
     >> despues nos va a permitir definir la funcion __init__ y el va a informar la clase vacia y nosotros le metemos a esa clase vacia lo que queramos
     >> self.nombre = nombre > a esta clase, en el atributo nombre, le pones la variable de entrada nombre
    

'''

class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso