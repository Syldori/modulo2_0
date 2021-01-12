'''

Objetos.
    -Funciones de primer nivel capaces de llamarse a si mismas y crear copias de si mismas
    -Codigo que encapsulas -tanto el bloque de codigo que hace algo, como tambien las varaibles que en ese codigo luego puedes usar)
    -Ademas, de ese codigo se puden tener muchas copias de el y puede funcionar como objetos
    -cada objeto tiene unas propiedades y atributos únicos, aunque comparta funcionalidad con otros objetos similares
    >> el código encapsulado dentro del objeto se llama Instancia de un objeto (cada objeto tendrá una instancia distinta, a pesar de que sabemos que tienen la misma funcionalidad)
        - otratortugita sería una instancia de la clase Turtle
        - tortugita seria otra instancia de la clase Turtle
    >>La Clase es el bloque de código que define las caracteristicas de un objeto de un tipo determinado. Esta compuesto por funciones y variables.
        -las funciones que van con paréntesis se llaman Métodos (de una clase) - por ejemplo, left(); fd()
        -las variables que van a definir su estado se llaman Atributos (.color(), speed(), position(x,y))
        
        > por eso siempre se crean con un par de paréntesis y a veces con ciertos parametros
    
    -los Objetos se llaman siempre con mayusucla
    >ejemplo: tortugas.
        -importamos turtle
        -tortugita = turtle.Turtle() >> esto es crear un objeto del modulo turtle, de tipo Turtle(objeto)
        - 
  !!- La ventaja es que podemos crear un objeto que sea player1 y otro que sea player2 >> ambos tienen la misma funcionalidad pero no los mismos atributos
  !!- Es decir, dos objetos pueden tener el mismo código, pero su comportamiento/propiesdades son distintas
        (ejemplo, las dos tortugitas tienen el mismo código de turtle, pero luego una se le da atributos diferentes a la otra (otraTortugita es verde, por ejmplo)


        
   -Los objetos nos permiten lidiar con la complejidad 
'''

import turtle

tortugita = turtle.Turtle()
otraTortugita = turtle.Turtle()

tortugita.fd(58) # avanzar 58

otraTortugita.color('green')
otraTortugita.left(90)
otraTortugita.fd(50)
