# Integración Continua

## Sistemas de Integración Continua
Existen diferentes sistema para Integración Continua. A continuación se muestran los sistemas más conocidos y cuáles son su
estudio:
* *Travis*: Ofrece diferentes planes de precios y permite usarlas a modo de prueba, pero para poder usarlas es necesario dar una tarjeta de crédito. A cambio, ofrece mayor características que otros sistemas. Dado que es posible que sea necesario pagar por este sistema, lo descartamos al haber otros sistemas con planes gratuitos.\
Enlace de características: https://www.travis-ci.com/pricing/

* *CircleCI*: Este sistema ofrece un plan gratuito, el cual ofrece unas características muy elevadas. Es de los sistemas más utilizados y es muy sencillo de configurar y usar y permite loguearse con GitHub. Por estas razones, se usará este sistema.\
Enlace de características: https://circleci.com/pricing/

* *GitLab*: Este sistema también es bastante conocido. Ofrece también un plan gratuito, pero no ofrece unas características muy altas. Al haber otros sistemas gratuitos y más potentes, se descarta este sistema.\
Enlace de características: https://about.gitlab.com/pricing/

* *GitHub Actions*: Aunque no sea una plataforma especialmente dedicada a la integración continua, es posible usarla como tal. Dado que hay sistemas más específicos para la integración continua, se descarta.

## Configuración del sistema elegido
Para configurar **CircleCI** se han seguidos los siguientes tutoriales oficiales:
* Para acceder al sistema: https://circleci.com/docs/first-steps/
* Ejemplos del archivo de configuración: https://circleci.com/docs/sample-config/
* Configuración del repositorio: https://circleci.com/docs/config-intro/

## Buenas prácticas
Para que se ejecute el sistema, se ha creado un archivo llamado [config.yml](../../.circleci/config.yml). De este archivo destacamos que hacemos uso del contenedor creado para la ejecución de test, **tests_f1department**, y del gestor de tareas que lanza esos tests, **Make**.

## Resultados
Una vez que el archivo **config.yml** está en el repositorio y tras hacer un **push**, podremos ver en la interfaz web de CircleCI la ejecución y resultado de los test.\
![CapturaEjecucionCI](./img/ejecucionCI.png)

En el siguiente enlace podemos ver todos los resultados.\
https://app.circleci.com/pipelines/github/Nastard/F1Department?branch=main
