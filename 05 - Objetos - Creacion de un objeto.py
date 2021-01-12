
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
4º - Le creamos los otros dos atributos
5º- Ahora hay que crear la función ladrar():
     Por como funcionan los objetos/clases en phyton
         >> Primer parámetro de la función/metodos de un objeto/clase SIEMPRE tienen que ser la propia clase
         >> ese primer parámetro no hace falta ponerlo ni informarlo (no la pongamos cuando pongamos ladrar(), pero siempre hay que ponerlo)
         >> Si ponemos parámetros después, funcionan como en una función normal
6º - ahora podemos ir añadiendo condiciones > ej: si pesa mucho, que ladre más fuerte
7º - si se pone print(nombrePerro) nos devuelve la dirección de memoria y que es de tipo perro
    >> podemos cambiarlo para que nos devuelva lo que queramos, como por ejemplo, los valores de las variables:
        >def __str__(self):
            return (lo que queramos poner)

>>para llamar al objeto, variable = Objeto(atributos)
'''

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    def ladrar(self):
        if self.peso >= 8:
            print ('WOW, WOW')
        else:
            print ('Guau, guau')
            
    def __str__(self): # esto es para que cuando ponemos prnt(nombre perro), nos diga esa frase
        return 'Soy el perro {}'.self.nombre
   
   '''
    esto haría que al poner print(nombrePerro), imprime el nombre y los 
    
    def __str__(self):
        return 'Perro{},e:{},p:{}'.format(self.nombre, self.edad,self.peso)
    '''
    
miko = Perro('Miko', 9,10)
miko.ladrar()
salchicho = Perro('Salchicho', 9, 5)
salchicho.ladrar()