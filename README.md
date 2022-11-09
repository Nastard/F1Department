# F1Department
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
>Proyecto a desarrollar de la asignatura Cloud Computing del Máster en Ingeniería Informática, curso 2022-2023.

## Descripción del Proyecto y Lógica de Negocio
### Descripción del Proyecto
Se va a desarrollar una aplicación sobre la Formula 1, competición reina del automovilismo, denominada F1Department. En resumen, esta aplicación ofrecerá multitud de estadísticas relacionadas con la Formula 1.

### Lógica de negocio
En resumen, la lógica de negocio de esta aplicación va a ser la de mostrar resultados calculados a partir de los datos disponibles. Al haber una gran cantidad de datos, se pueden generar multitud de estadísticas que nos interese analizar.


## Concretando y planificando el proyecto
### Hitos establecidos para el proyecto
Se han establecido los siguientes Hitos para la realización de este proyecto.

**[Hito0: Descripción del problema a resolver.](https://github.com/Nastard/F1Department/milestone/1)**\
En este hito se define el proyecto  y el problema que resolver. También se define la lógica de negocio que el proyecto va a tener.

**[Hito1: Diseño de las clases necesarias para leer y almacenar todos los datos.](https://github.com/Nastard/F1Department/milestone/2)**\
En este hito se quiere definir e implementar el código necesario con una estructura básica que usara el proyecto para almacenar los datos leídos.

**[Hito2: Diseño de los métodos necesarios que calculará y devolverá las diferentes estadísticas relacionadas con la Formula 1.](https://github.com/Nastard/F1Department/milestone/3)**\
En este hito se va a continuar con el desarrollo del código implementando los diversos métodos que tendrá el proyecto, en este caso el cálculo de estadísticas.

**[Hito3: Diseño de una API que devuelva las diferentes estadísticas.](https://github.com/Nastard/F1Department/milestone/4)**\
En este hito se desea desarrollar una API que devuelva los resultados de las distintas estadísticas.

### Historias de usuario para el proyecto
Se han establecido las siguientes historias de usuario para la realización de este proyecto. Además se definen issues relacionadas con estas historias de usuario.

**[[HU1]Como administrador de la aplicación, dado que tengo disponible los datos históricos de la Formula 1, necesito unificar todos estos datos en una única estructura.](https://github.com/Nastard/F1Department/issues/4)**\
En esta historia de usuario se quiere que el administrador del proyecto sea capaz de unificar los distintos datos disponibles en una estructura.\
Para realizar la HU1, se creará una clase que sea capaz de unir los ficheros CSV y devolverlo.\
- *[Como programador, se creará una clase que lea los ficheros CSV y lo unifiquen en uno solo CSV y también que lo devuelva como una estructura de datos.](https://github.com/Nastard/F1Department/issues/6)*

**[[HU2]Como usuario de la aplicación, quiero saber diversas estadísticas relacionadas con la Formula 1.](https://github.com/Nastard/F1Department/issues/5)**\
En esta historia de usuario un usuario indica qué estadísticas desea saber.\
Para ello se crean diferentes issues para las diversas estadísticas que el administrador deberá implementar:\
- *[Como programador, se necesita implementar un método que devuelva al piloto con más victorias.](https://github.com/Nastard/F1Department/issues/7)*
- *[Como programador, se necesita implementar un método que devuelva al piloto con más pole position.](https://github.com/Nastard/F1Department/issues/8)*
- *[Como programador, se necesita implementar un método que devuelva la nacionalidad que ha ganado más carreras.](https://github.com/Nastard/F1Department/issues/9)*
- *[Como programador, se necesita implementar un método que devuelva el constructor con más vueltas lideradas.](https://github.com/Nastard/F1Department/issues/10)*
- *[Como programador, se necesita implementar un método que devuelva el constructor con más puntos obtenidos.](https://github.com/Nastard/F1Department/issues/11)*

### Descripción de las clases para el proyecto
Se han definido las siguientes clases para la realización de este proyecto. Se ha decidido hacer dos clases, una para leer los datos y otra para devolver las estadísticas, para una mejor reutilización del código.

**[F1DepartmentDataJoin](../../f1department/f1department_data_join.py)**\
Esta clase sirve para leer todos los ficheros CSV de datos y unificarlos en un objeto de tipo DataFrame.

**[F1Department](../../f1department/f1department.py)**\
Esta clase sirve para implementar los distintos métodos que devolverán las estadísticas.   


## Documentación del proyecto
Enlaces con la documentación del proyecto:
* [Documentación del Hito 0 de la asignatura](./docs/hito0/README.md)
* [Documentación del Hito 1 de la asignatura](./docs/hito1/README.md)
	* [Historias de Usuario](./docs/hito1/historiasUsuario.md)
	* [Hitos para el proyecto](./docs/hito1/hitosProyecto.md)
	* [Clases creadas](./docs/hito1/descripcionClases.md)
