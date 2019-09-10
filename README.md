# Tarea2MatamorosNarvaez

Tarea No.2: GitHub, Pytest y Flake8

Realizado por:
Roberto Matamoros Gamboa    2016252162
Katherin Narváez Núñez      2016123067

PRIMERA PARTE: CONCEPTOS TEÓRIOCOS

¿Qué es Git? 
  Git es un sistema de control de versiones de código de forma distribuida que permite trabajar en equipo cuando se desarrolla un software. Es una herramienta muy potente, diseñada por Linus Torvalds. De acuerdo con Rubio (2019) cuenta con las siguientes características:
      -Es un software libre.
      -No depende de un repositorio central.
      -Se puede mantener un historial de versiones completo.
      -Es muy rápido.
      -Cuenta con un sistema de trabajo con ramas.
      -Las ramas cuentan con una línea de progreso diferente a la rama principal.

¿Qué es Github?
    De acuerdo con Kinsta, proveedor de WordPress hosting, GitHub es una compañia que ofrece un servicio de hosting de repositorios almacenados en la nube. Permite a los individuos y equipos utilizar más fácilmente Git como la versión de control y colaboración.
   Es decir, GitHub es un sitio web y un servicio en la nube que permite a los programadores tanto almacenar como administrar un código. Además, la plataforma permite llevar un registro y control de cualquier cambio realizado al código. 

¿Qué es un branch?
    Un branch o una rama es una bifurcación que parte de la rama principal (master) o bien de otra rama. (Pérez, A; 2011). Entre sus utilidades se encuentran:
      -Desarrollar una nueva función sin afectar a la rama principal.
      -Realizar un hotfix en una versión que ya había salido de producción.
      -Gestionar distintas versiones de un mismo producto.
    Otra manera de verlo, es como una versión paralela del repositorio. Una vez que se realizan todos los cambios a la rama se puede fusionar con la rama principal
  
¿Qué es un commit? 
   Un commit es un cambio que se le hace a un archivo o a un grupo de archivos, se asimila a  la acción de guardar o subir datos, con la diferencia que en Git cada vez que se guarda se crea un ID único en el repositorio. Esto permite llevar un registro de los cambios que se han realizado, donde se indica quién lo realizó y cuando.  (GitHub Help; 2019)

¿Qué se entiende cuando se dice que un archivo está “staged”? 
    Existen tres estados principales en el sistema Git: confirmado (commited), modificado (modified) y preparado (staged). (Palacios, J; 2017)
      -En el primero, luego de hacer un commit se sabe que los datos se almacenaron en la línea de tiempo de Git. 
      -En el segundo, se indica que una modificación ha sido detectada pero que no ha sido guardada porque no se ha confirmado que se quieren guardar los datos. 
      -En el tercero, se indica que uno o varios archivos modificados se han puesto en cola para que se incluyan en la siguiente instrucción de commit y que puedan ser guardados de manera definitiva en la línea temporal.

¿Qué hace el comando git checkout? 
   Se utiliza para crear ramas o cambiar entre ellas. El comando se utiliza de las siguientes manera (Gustavo B; 2019):
                                 Comando                             Función
                  git checkout -b <branch-name>          Crea una nueva rama y se cambia a ella.
                  git checkout <branch-name>             Se cambia de una rama a la otra.

¿Qué hace el comando git stash?
   Es utilizado cuando se quiere cambiar de rama pero sin confirmar los cambios realizados hasta el momento. Lo que hace es un guardado rápido provisional y envía un nuevo grupo de cambios a la pila de guardado rápido. (Pro Git, 2da Edición, Capítulo 1.3)
  
¿Qué hace el comando git add? 
   Se utiliza para agregar documentos al repositorio. Se debe escribir el comando y luego el nombre del archivo, por ejemplo (Gustavo B; 2019):
                                                 git add Temp.txt
  Si se utiliza luego del comando la indicación -A entonces se agregan todos los archivos y carpetas que hay en el proyecto.
                                                 git add - A
 
¿Qué es Pytest? 
    Pytest es una herramienta para realizar pruebas de software de cualquier tipo y nivel utilizando Python. Suele ser usado por equipos de desarrollo, equipos QA, individuos practicando TDD (Okken, B.; 2019)… Ofrece muchas ventajas entre ellas se encuentran: 
      -Es simple y tiene una sintaxis sencilla.
      -Puede correr pruebas en paralelo.
      -Puede correr una prueba en específico o un grupo de pruebas.
      -Detecta pruebas automáticamente.
      -Es una fuente abierta.
 
Bajo el contexto de pytest. ¿Qué es un “assert”? 
    El comando assert, en el lenguaje de Python, permite la definición de condiciones que se deben cumplir siempre. Puede ser usado como un pre y post condición en métodos, funciones, bloques de código y para especificar invariantes. En la herramienta Pytest se permite hacer uso de este comando para verificar las expectativas y valores en las pruebas. (Martínez, H; 2005)

¿Qué es Flake 8? 
    Flake 8 es una librería de Python que encierra PyFlakes, pycodestyle y Ned Batchelder´s McCabe script. Es una herramienta para revisar código basándose en el estilo de código PEP8, para detectar errores de programación y revisar la complejidad ciclomática (software que mide el número de caminos independientes dentro del código fuente). (Freitas, V.; 2016)


FUENTES CONSULTADAS

Freitas, V. (2016) How to Use Flake8. Obtenido de https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html
GitHub Help. (2019) GitHub glossary. Obtenido de https://help.github.com/en/articles/github-glossary
Gustavo B. (2019). Comandos básicos de GIT. Obtenido de https://www.hostinger.es/tutoriales/comandos-de-git
Kinsta (2018). ¿Qués es GitHub? Una Guía para Principiantes sobre GitHub. Obtenido de https://kinsta.com/es/base-de-conocimiento/que-es-github/
Martínez, H. (2005). Assert, era RE: Sobrecargar función. Obtenido de https://mail.python.org/pipermail/python-es/2005-February/007398.html
Okken, B. (2019). Python testing with pytest. Obtenido de https://www.oreilly.com/library/view/python-testing-with/9781680502848/f_0006.xhtml
Palacios, J. (2017). Los tres estados de Git. Obtenido de https://sargantanacode.es/post/the-three-states-of-git
Pérez, A. (2011) Trabajando con GIT, introducción al uso de los branches y git-completion.bash. Obtenido de https://www.adictosaltrabajo.com/2011/06/27/git-branch-bash/
Pro Git, 2da Edición, Capítulo 1.3: Las herramientas de Git - Guardado rápido provisional. Obtenido de https://git-scm.com/book/es/v1/Las-herramientas-de-Git-Guardado-r%C3%A1pido-provisional
Rubio, J (2019). Qué es GIT y para qué sirve. Obtenido de https://openwebinars.net/blog/que-es-git-y-para-que-sirve/
