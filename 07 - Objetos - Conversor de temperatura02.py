'''
Para hacer que se comporte más como un termómetro:
-creamos getter y setter >> para que la unidad y la temperatura fueran privados y no se puedan inicializar en la construcción:
    - lo que hace es que si la entrada es adecuada la cambia, sino no hace nada
    -COn la funcion mide:
        >Va a coger la unida de medida, comprueba 3 cosas:
            -esta unidad está vacía
            -es igual a la unidad de medida que hemos señalado antes
                >>si se dan algunos de estos dos casos, me devuelva la temepratura y la undia de medida informadas (con la función __str__)
            -si no lo es: hace una conversión de la temperatura a la otra unidad informada en mide -ej t.mide('C'/'F')
        
>>Lo que intentamos hacer es un Termometro que tenga:
    -Atributos: Unidad Medida
                Temperatura que esta midiendo
    -Funciones: mide (unidad) > este mide tendrá de parametro la unidad como opcional
    >>Este temometro lo inicializamos ej:
        >>> t=Termometro()
        >>> t.temp(32)
        >>> t.unidadMedida('F')
        >>> t.mide()
            >> si le ponemos t.mide() sin nada, nos devuevle "32º F'
            >> si le ponemos t.mide('C') -es decir, una unidad que pueda transformar- >> nos devuelve la transformación a grados

--- 
'''

class Termometro():
    def __init__(self):
        self.__unidadM = 'C' #las hacemos privadas
        self.__temperatura = 0
    
    def __str__(self):
        return '{}º{}'.format(self.__temperatura, self.__unidadM)
    
    def unidadMedida(self, uniM=None): #Creamos un getter y un setter de este atributo
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM
                
    def temp(self, temperatura =None):
        if temperatura ==None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura

    def __conversor(self, temperatura, unidad): # la ponemos privada porque nos queremos que se vea
        if unidad.upper() == 'C':
            return '{}º F'.format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return '{}º C'.format((temperatura -32)*5/9)
        else:
            return 'unidad incorrecta'
    
    def mide(self, uniM=None): # esto funciona como un getter o un setter
        if uniM == None or uniM == self.__unidadM:
         # si le digo qu me mida y no le informo nada, me va a devolver la medida que tiene
         # si le digo que mida y le informo de algo, pero ese algo es igual a la medida que tiene, me va a devolver la temperatura en la medida que informamos
            return self.__str__()
        else: # si no coincide, habrá que hacer la conversión
            if uniM == 'F' or uniM == 'C': # primero validamos que si no estamos informando exactamente esta o en vacio, la que esté informando sea correcta
                # Esta validación se hace por si ponemos kelvin o algo así, y que nos devuelva el valor en el que está
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()