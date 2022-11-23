# F1Department
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
>Proyecto a desarrollar de la asignatura Cloud Computing del Máster en Ingeniería Informática, curso 2022-2023.

## Biblioteca de aserciones

### Elección de la biblioteca de aserciones
Existen diferentes bibliotecas de aserciones en Python. Vamos a mostrar algunas de las más conocidas y elegiremos la más adecuada para el proyecto.

#### Unittest
Unittest es una librería estándar de pruebas unitarias de las más usadas popular. Permite testear métodos y clases de forma muy sencilla y ofreciendo más funcionalidades que otras librerías, como por ejemplo una función para inicializar los datos a usar. Viene por defecto con Python\
Página oficial: https://docs.python.org/3/library/unittest.html

#### Assert del lenguaje Python
Python permite testear con una palabra clave, *assert*. Es una manera muy rápida y sencilla para hacer test, pero no está pensado para ello y por eso ofrece unas características muy inferiores que una librería. Está más pensado para debuggear, aunque a veces se usa para testeo.

#### Asertpy
Asertpy es una biblioteca de aserciones con una buena API fluida. Para poder usarla es necesario instalarla, pues no viene por defecto con Python. Su forma de uso es algo compleja, pero también ofrece más funcionalidades como testear varios casos con una sola sentencia.\
Página oficial: https://pypi.org/project/assertpy/

### Conclusión
De estas tres bibliotecas de aserciones, vamos a usar Unittest porque es de las más usadas y sencillas de programar, sin necesidad de tener que instalarla. También porque se adapta bien al proyecto.

### Uso de marco de pruebas
El uso de Unittest se hace dentro de las clases de test.

## Marco de pruebas

### Elección del marco de pruebas
Existen diferentes marco de pruebas en Python. Vamos a mostrar algunas de las más conocidas y elegiremos la más adecuada para el proyecto.

#### Pytest
Pytest es un marco de prueba de código abierto de los más utilizados que existen. Admite también pruebas unitarias, pruebas funcionales y pruebas de API. Permite hacer pruebas compactas y simples y dispone de una gran comunidad detrás. Es ideal para crear pruebas pequeñas y concisas, que admitan escenarios complejos.\
Página oficial: https://docs.pytest.org/en/7.2.x/

#### Behave
Behave es un marcos de prueba más populares para BDD (desarrollo basado en el comportamiento). Permite escribir casos de prueba en un lenguaje legible. dispone una gran cantidad de documentación. Solo sirve para pruebas de caja negra.\
Página oficial: https://behave.readthedocs.io/en/latest/

#### Testify
Testify está diseñado para reemplazar los marcos de Unittest y Nose, y tiene funciones avanzadas para el Unittest estándar. Se utiliza para pruebas unitarias, pruebas de integración y pruebas de sistemas. Ofrece multitud de complementos y tiene una sintaxis simple. No dispone de una documentación extensa, por lo que es difícil de aprender.
Página oficial: https://pypi.org/project/testify/

### Conclusión
De estos tres marcos de pruebas, vamos a usar Pytest, ya que es la más completa y sencilla y las características que ofrece son las más indicadas para este proyecto. Para usarla la instalaremos.

### Uso de marco de pruebas
Para ejecutar el marco de pruebas, tan solo debemos ir a la carpeta de los test y ejecutar el siguiente comando:
```
$ pytest
```

## Gestor de tareas

### Elección del gestor de tareas
Existen diferentes gestores de tareas en Python. Vamos a mostrar algunas de las más conocidas y elegiremos la más adecuada para el proyecto.

#### Makefile
Makefile es un gestor muy utilizado que permite gestionar Python entre muchas otras cosas que permite realizar. Es muy sencillo de usar, pero puede complicarse si queremos hacer tareas más complejas. Las tareas se definen en un fichero y permiten interactuar con el sistema operativo.

#### Invoke
Invoke es una biblioteca de Python para administrar tareas orientados a shell y organizar el código de Python ejecutable en tareas invocables por CLI. Se inspira en varias fuentes, ofreciendo un conjunto de funciones potente y limpio.\
Página oficial: https://www.pyinvoke.org/

#### Pypyr
Pypyr es un gestor de tareas para procesos automáticos. Se ejecuta de forma condicional y puede manejar errores. Las tareas se describen en un fichero yaml de forma secuencial, por lo que es muy parecido a Makefile. Se debe instalar, no viene con como una librería de Python. Este gestor es nuevo y hay poca información en internet, por lo que si hay dudas o errores puede ser difícil conseguir una solución.\
Página oficial: https://pypyr.io/

#### Conclusión
De estos tres gestores de tareas, vamos a usar Makefile, pues es el más sencillo y rápido de utilizar y es capaz de abarcar las necesidades del proyecto sin tener que realizar instalaciones adicionales o configuraciones más complejas.

### Configuración y uso del gestor de tareas
Para ejecutar el gestor de tareas, tan solo es necesario ejecutar las opciones descritas en el archivo Makefile. Estas opciones son las siguientes:\
Esta opción instala las librerías necesarias que necesita el proyecto. Para ello lee el archivo *requirements.txt*, donde se encuentran todos los paquetes necesarios del proyecto.
```
$ make install
```
Esta opción permite ejecutar los test, haciendo uso del marco de pruebas, en este caso *Pytest*.
```
$ make test
```

## Concretando y planificando el proyecto
### Hitos establecidos para el proyecto
Se han establecido los siguientes Hitos para la realización de este proyecto.\
**[Hito0: Descripción del problema a resolver.](https://github.com/Nastard/F1Department/milestone/1)**\
**[Hito1: Diseño de las clases necesarias para leer y almacenar todos los datos.](https://github.com/Nastard/F1Department/milestone/2)**\
**[Hito2: Diseño de los métodos necesarios que calculará y devolverá las diferentes estadísticas relacionadas con la Formula 1.](https://github.com/Nastard/F1Department/milestone/3)**\
**[Hito3: Diseño de una API que devuelva las diferentes estadísticas.](https://github.com/Nastard/F1Department/milestone/4)**

### Historias de usuario para el proyecto
Se han establecido las siguientes historias de usuario para la realización de este proyecto.\
**[[HU1]Como administrador de la aplicación, dado que tengo disponible los datos históricos de la Formula 1, necesito unificar todos estos datos en una única estructura.](https://github.com/Nastard/F1Department/issues/4)**\
**[[HU2]Como usuario de la aplicación, quiero saber diversas estadísticas relacionadas con la Formula 1.](https://github.com/Nastard/F1Department/issues/5)**

### Descripción de las clases para el proyecto
Se han definido las siguientes clases para la realización de este proyecto.\
**[F1DepartmentDataJoin](./f1department/f1department_data_join.py)**\
**[F1Department](./f1department/f1department.py)**

## Descripción del Proyecto y Lógica de Negocio
### Descripción del Proyecto
Se va a desarrollar una aplicación sobre la Formula 1, competición reina del automovilismo, denominada F1Department. En resumen, esta aplicación ofrecerá multitud de estadísticas relacionadas con la Formula 1.

### Lógica de negocio
En resumen, la lógica de negocio de esta aplicación va a ser la de mostrar resultados calculados a partir de los datos disponibles. Al haber una gran cantidad de datos, se pueden generar multitud de estadísticas que nos interese analizar.

## Documentación del proyecto
Enlaces con la documentación del proyecto:
* [Documentación del Hito 0 de la asignatur, Descripción y lógica](./docs/hito0/README.md)
* [Documentación del Hito 1 de la asignatura, Planificación](./docs/hito1/README.md)
* [Documentación del Hito 2 de la asignatura, Test](./docs/hito2/README.md)
	* [Gestor de Tareas](./docs/hito2/gestorTareas.md)
	* [Biblioteca de Aserciones](./docs/hito2/bibliotecaAserciones.md)
	* [Marco de Pruebas](./docs/hito2/marcoPruebas.md)
