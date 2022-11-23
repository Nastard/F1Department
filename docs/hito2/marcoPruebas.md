# Marco de pruebas

## Elección del marco de pruebas
Existen diferentes marco de pruebas en Python. Vamos a mostrar algunas de las más conocidas y elegiremos la más adecuada para el proyecto.

### Pytest
Pytest es un marco de prueba de código abierto de los más utilizados que existen. Admite también pruebas unitarias, pruebas funcionales y pruebas de API. Permite hacer pruebas compactas y simples y dispone de una gran comunidad detrás. Es ideal para crear pruebas pequeñas y concisas, que admitan escenarios complejos.\
Página oficial: https://docs.pytest.org/en/7.2.x/

### Behave
Behave es un marcos de prueba más populares para BDD (desarrollo basado en el comportamiento). Permite escribir casos de prueba en un lenguaje legible. dispone una gran cantidad de documentación. Solo sirve para pruebas de caja negra.\
Página oficial: https://behave.readthedocs.io/en/latest/

### Testify
Testify está diseñado para reemplazar los marcos de Unittest y Nose, y tiene funciones avanzadas para el Unittest estándar. Se utiliza para pruebas unitarias, pruebas de integración y pruebas de sistemas. Ofrece multitud de complementos y tiene una sintaxis simple. No dispone de una documentación extensa, por lo que es difícil de aprender.
Página oficial: https://pypi.org/project/testify/

## Conclusión
De estos tres marcos de pruebas, vamos a usar Pytest, ya que es la más completa y sencilla y las características que ofrece son las más indicadas para este proyecto. Para usarla la instalaremos.

## Uso de marco de pruebas
Para ejecutar el marco de pruebas, tan solo debemos ir a la carpeta de los test y ejecutar el siguiente comando:
```
$ pytest
```
