'''
Herencia y subclases:

-Herencia:
    >> tomando el objeto de perro, vamos a crear una clase nueva (Perro Asistencia) que herede los atributos de Perro, pero con nuevos elementos
        >> la nueva clase, en lugar de definirla en vacío, decimos que hereda de la clase preexistente Perro
            -como la nueva clase hereda de la anterior, le decimos a phyton que la cree de tipo de Perro y le informe de los parametros  
            - ponemos Perro.__init__(...) para que en la parte que el conrresponde a Perro, ejecute su funcionalidad
        >>Esta nueva clase heredará todos los atributos y métodos
            -no hereda el def __str__, habría que volverla a definir directamente en la nueva clase
                >>cuando en una clase que hereda de otra, definimos el mismo método
                  esto de redefinirla se llama SOBREESCRIBIR UN MÉTODO (overwrite)
        
        >>Vamos a probar a sobreescribir el método ladrar >> si el perro está trabajnado, no puede ladrar:
            -tenemos que crear un atributo nuevo de 'trabajando' y por defecto lo ponemos a False
            -y sobreesscribimos ladrar() >> ahi ponemos la condicional de si está trabajando, no puede ladrar
            -en caso de que no esté trabajando, queremos la funcionalidad del padre (original)
                >>lo que hacemos es invocar al objeto con la funcionalidad y la instancia -y parametros si tiene- Perro.ladrar(self)
            - Si queremos ponerlo a trabajar, habría que poner en consola nombre.trabajando = True
                >>Una forma más elegante, es hacer un método para que haga esto (el def trabajando)
                 --lo pondríamos a trabajar poniendo nombre.trabajando(True)
               
         METODOS SETTER Y GETTER
            trabajando() - esto es un getter
            trabajando(True) - setter (cuando se le asigna un valor)
            >>Creamos estas funciones de getter setter para poder acceder a un atributo que hayamos escondido poniendole dos guiones por delante
               (ej .__trabajando >> esto hace que no se pueda acceder directamente a el, habria que usar la funcion)
               (simulan ser privados)
    
    No es necesario escribir los atributos del tirón en el cosntructor (ej __init__(self, n, e, p))
         >> podemos asginarlos depsues
    
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
            
    def __str__(self):
        return 'Perro{},e:{},p:{}'.format(self.nombre, self.edad,self.peso)
   
    
class PerroAsistencia(Perro): # con definirlo así, phyton ya sabe que Perroasistencia va a seer una subclase de perro, herendado de ella
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso) # como la nueva clase hereda de la anterior, le decimos a phyton que la cree de tipo de Perro y le informe de los parametros
        self.amo = amo # solo tendríamos que añadir el nuevo atributo
        self.__trabajando = False # estos dos guiones nos permite esconder objetos y simular que sean privadas 
        
    def __str__(self):
        return 'Perro de asistencia de {}'.format(self.amo)
    
    def pasear(self):
        print ('{} ayudo a mi dueño, {} a pasear'.format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.__trabajando:
            print ('No puedo ladrar porque estoy trabajando')
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None): # este es un metodo que nos permite consultar o modificar el estado trabajando del objeto
        if valor == None: # si no informamos del valor, me deuvuelves el valor que tiene
            return self._trabajando
        else: # si nos informa del valor, le asignamos ese valor
            self.__trabajando = valor
            
        