'''

Objetos.
    -Funciones de primer nivel capaces de llamarse a si mismas y crear copias de si mismas
    -Codigo que encapsulas -tanto el bloque de codigo que hace algo, como tambien las varaibles que en ese codigo luego puedes usar)
    -Ademas, de ese codigo se puden tener muchas copias de el y puede funcionar como objetos
    -cada objeto tiene unas propiedades y atributos únicos, aunque comparta funcionalidad con otros objetos similares
    
        > por eso siempre se crean con un par de paréntesis y a veces con ciertos parametros
    
    -los Objetos se llaman siempre con mayusucla
    >ejemplo: tortugas.
        -importamos turtle
        -tortugita = turtle.Turtle() >> esto es crear un objeto del modulo turtle, de tipo Turtle(objeto)
        - 
  !!- La ventaja es que podemos crear un objeto que sea player1 y otro que sea player2 >> ambos tienen la misma funcionalidad pero no los mismos atributos
  !!- Es decir, dos objetos pueden tener el mismo código, pero su comportamiento/propiesdades son distintas
        (ejemplo, las dos tortugitas tienen el mismo código de turtle, pero luego una se le da atributos diferentes a la otra (otraTortugita es verde, por ejmplo)

    >> el código encapsulado dentro del objeto se llama instancia de un objeto (cada objeto tendrá una instancia distinta, a pesar de que sabemos que tienen la misma funcionalidad)
   
   -Los objetos nos permiten lidiar con la complejidad 
'''

import turtle

tortugita = turtle.Turtle()
otraTortugita = turtle.Turtle()

tortugita.fd(58) # avanzar 58

otraTortugita.color('green')
otraTortugita.left(90)
otraTortugita.fd(50)
