# Biblioteca de aserciones

## Elección de la biblioteca de aserciones
Existen diferentes bibliotecas de aserciones en Python. Vamos a mostrar algunas de las más conocidas y elegiremos la más adecuada para el proyecto.

### Unittest
Unittest es una librería estándar de pruebas unitarias de las más usadas popular. Permite testear métodos y clases de forma muy sencilla y ofreciendo más funcionalidades que otras librerías, como por ejemplo una función para inicializar los datos a usar. Viene por defecto con Python\
Página oficial: https://docs.python.org/3/library/unittest.html

### Assert del lenguaje Python
Python permite testear con una palabra clave, *assert*. Es una manera muy rápida y sencilla para hacer test, pero no está pensado para ello y por eso ofrece unas características muy inferiores que una librería. Está más pensado para debuggear, aunque a veces se usa para testeo.

### Asertpy
Asertpy es una biblioteca de aserciones con una buena API fluida. Para poder usarla es necesario instalarla, pues no viene por defecto con Python. Su forma de uso es algo compleja, pero también ofrece más funcionalidades como testear varios casos con una sola sentencia.\
Página oficial: https://pypi.org/project/assertpy/

## Conclusión
De estas tres bibliotecas de aserciones, vamos a usar Unittest porque es de las más usadas y sencillas de programar, sin necesidad de tener que instalarla. También porque se adapta bien al proyecto.

## Uso de marco de pruebas
El uso de Unittest se hace dentro de las clases de test.
