'''
2110 Control de versiones (sistema que controla los cambios de los ficheros que hay en una carpeta)

Hay veces que tienes muchs carpetas de un mismo proyecto con camibios o modificaciones
  >> para esto, se crea un sistema que va creando registros de los cambios que se hacen de los ficheros
     hacen capturas de pantalla para ver los cambios

- Hay dos tipos de control de versiones.
    >Centralizado: hay un repositorio central y si un mimebro del equipo coje un fichero y lo modifica, otro compañero que intente acceder a el solo lo puede hacer en lectura (hasta que termine el otro)
    >Distribuidos: Hay un repositiorio central y cada persona que acceda, descarga toda el repositorio (crea un clon) y trabajan sobre esa copia > si dos personas han tocado el mismo fichero, el sistema solo coge las modificaciones de las partes
                   que no sean iguales. En caso de que ambos hayan tocado lo mismo, genera un conflicto y pide que lo resuelvan los usuarios
                   
    

'''
'''
GITHUB - sistema de control de versiones distribuido

>Este sistema hace una copia de todas las carpetas/ficheros
    >> luego crea enlaces a lo no modificado??
    
>Funciona con 3 área de trabajo (el fichero puede estar en uno de estos 3 estados/áreas de trabajo):
    -Working directory: área de trabajo, es cuando se hace una modificación
    -Staging area(área de preparación): cuando terminamos de modificar, pero antes de hacer la cogelación/foto, hay que decirle a Github que ficheros de los moficados hay pasar al área de preparación
    -Git directory: cuando ya seleccionamos los ficheros, ejecutamos la congelación y pasa al repositorio
    
> Crear cuenta en Github
 -Syldori
 -moniaccion13

- tras crear un git >> comandos:
    -git status para ver el estado de la captura
    -git add . (con punto, para que añada todo lo nuevo all stating area)
    -git add nombrePrograma.py : añade un archivo concreto
    -git commit: para guardarlos (meter mensaje y demás)
    -git commit -m "Mensaje" : esto sirve para guardar poniendo ya el mensaje directamente
    -git local: para que se vean los git que hay y los cambios
    
- para salir cuando hacemos el git commit:
    > <esc> :wq <enter>

-Sincronizar repositorios locales con el remoto:
   >>Usando comandos:
    -decirle al repositorio local que su repositorio remoto (origin) esta en una dirección (ej https://github.com/Syldori/modulo2_0.git )
        > se hace con la instrucción: git remote add origin https://github.com/Syldori/modulo2_0.git
    - esto une los repositorios > el repositirio remoto (llamado origin) va a estar en donde el vínculo
    - una vez puesta la instrucción, hay que hacer un push (subir desde un repositorio local a un remoto)
        > se hace con: git push -u origin master
        - las primeras veces se pone origin, despues se puede ignorar
        >>de esta forma quedan enlazas 

'''

