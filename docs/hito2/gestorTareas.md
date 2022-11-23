# Gestor de tareas

## Elección del gestor de tareas
Existen diferentes gestores de tareas en Python. Vamos a mostrar algunas de las más conocidas y elegiremos la más adecuada para el proyecto.

### Makefile
Makefile es un gestor muy utilizado que permite gestionar Python entre muchas otras cosas que permite realizar. Es muy sencillo de usar, pero puede complicarse si queremos hacer tareas más complejas. Las tareas se definen en un fichero y permiten interactuar con el sistema operativo.

### Invoke
Invoke es una biblioteca de Python para administrar tareas orientados a shell y organizar el código de Python ejecutable en tareas invocables por CLI. Se inspira en varias fuentes, ofreciendo un conjunto de funciones potente y limpio.\
Página oficial: https://www.pyinvoke.org/

### Pypyr
Pypyr es un gestor de tareas para procesos automáticos. Se ejecuta de forma condicional y puede manejar errores. Las tareas se describen en un fichero yaml de forma secuencial, por lo que es muy parecido a Makefile. Se debe instalar, no viene con como una librería de Python. Este gestor es nuevo y hay poca información en internet, por lo que si hay dudas o errores puede ser difícil conseguir una solución.\
Página oficial: https://pypyr.io/

### Conclusión
De estos tres gestores de tareas, vamos a usar Makefile, pues es el más sencillo y rápido de utilizar y es capaz de abarcar las necesidades del proyecto sin tener que realizar instalaciones adicionales o configuraciones más complejas.

## Configuración y uso del gestor de tareas
Para ejecutar el gestor de tareas, tan solo es necesario ejecutar las opciones descritas en el archivo Makefile. Estas opciones son las siguientes:\
Esta opción instala las librerías necesarias que necesita el proyecto. Para ello lee el archivo *requirements.txt*, donde se encuentran todos los paquetes necesarios del proyecto.
```
$ make install
```
Esta opción permite ejecutar los test, haciendo uso del marco de pruebas, en este caso *Pytest*.
```
$ make test
```
