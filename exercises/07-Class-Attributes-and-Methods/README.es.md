# 07 Atributos y metodos de clase

## Objetivo

En este ejercicio vas a diferenciar estado compartido de clase y comportamiento de instancia.

## Concepto clave

Un atributo de clase se comparte entre todas las instancias.

Los metodos de clase trabajan sobre la clase completa y los metodos estaticos son utilidades relacionadas.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person`.
2. Agrega un atributo de clase `population = 0`.
3. En `__init__(name, age)`, guarda `name` y `age`, y aumenta `Person.population` en 1.
4. Crea un metodo de clase `get_population()` que retorne `population`.
5. Crea un metodo estatico `is_adult(age)` que retorne `True` si `age >= 18`, y `False` en otro caso.
6. Crea una instancia global `student = Person("John", 21)`.

## Criterio de exito

El ejercicio se considera correcto cuando:

- `population` aumenta al crear nuevas instancias.
- `get_population()` refleja el total de instancias creadas.
- `is_adult()` funciona para mayores y menores de edad.
