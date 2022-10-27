# F1Department
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
>Proyecto a desarrollar de la asignatura Cloud Computing del Máster en Ingeniería Informática, curso 2022-2023.

## Descripción del Proyecto y Lógica de Negocio
### Descripción del Proyecto
Se va a desarrollar una aplicación sobre la Formula 1, competición reina del automovilismo, denominada F1Department. En resumen, esta aplicación ofrecerá multitud de estadísticas relacionadas con la Formula 1.

Actualmente no existen demasiadas páginas web o aplicaciones que muestren la gran cantidad de datos que se genera en un evento de Formula 1, pues la Formula 1 tiene registros desde el año 1950, cuando empezó esta competición, y además con el paso de los años cada evento de Formula 1 genera una gran cantidad de datos.
Tampoco existe una gran cantidad de páginas web que muestren las diferentes estadísticas que esta competición genera.

Por ello, se va a desarrollar este proyecto para solventar este problema. A parte de guardar los datos necesarios, se calculará diferentes estadísticas. Las estadísticas que se pueden generar con los datos son muy diversas, como por ejemplo indicar cual es el piloto con más victorias, el piloto con más poles o incluso que nacionalidad ha ganado más carreras.

Este proyecto está destinada para fans de la Formula 1 y para cualquier persona o entidad que necesita de esta información generada, como puede ser el caso de las casas de apuestas, otras aplicaciones...

### Lógica de negocio
En resumen, la lógica de negocio de esta aplicación va a ser la de mostrar resultados calculados a partir de los datos disponibles. Al haber una gran cantidad de datos, se pueden generar multitud de estadísticas que nos interese analizar.

También va a ser necesario juntar en un solo modelo todos los datos disponibles. Se va a usar la página [Ergast](https://ergast.com/mrd/), la cual contiene todos los datos de Formula 1 desde 1950 hasta la carrera más reciente. Los datos que nos proporcionan están divididos, por lo que este proyecto generará un modelo de datos en el cual estén todos los datos unificados.

## Documentación del proyecto
Enlaces con la documentación del proyecto:
* [Documentación del Hito 0](./doc/hito0/README.md)
	* [Configuración inicial del repositorio](./doc/hito0/configuracionInicial.md)
	* [Descripción del problema y lógica de negocio](./doc/hito0/descripcionLogica.md)
