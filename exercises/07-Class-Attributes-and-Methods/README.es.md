# 07 Atributos y métodos de clase

## Objetivo

En este ejercicio vas a diferenciar estado compartido de clase y comportamiento de instancia.

## Concepto clave

Un atributo de clase se comparte entre todas las instancias.

Los métodos de clase trabajan sobre la clase completa y los métodos estáticos son utilidades relacionadas.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person`.
2. Agrega un atributo de clase `population = 0`.
3. En `__init__(name, age)`, guarda `name` y `age`, y aumenta `Person.population` en 1.
4. Define `get_population()` con `@classmethod` para que retorne `population`.
5. Define `is_adult(age)` con `@staticmethod` para que retorne `True` si `age >= 18`, y `False` en otro caso.
6. Crea una instancia global `student = Person("John", 21)`.

## Criterio de éxito

El ejercicio se considera correcto cuando:

- `population` aumenta al crear nuevas instancias.
- `get_population()` refleja el total de instancias creadas.
- `is_adult()` funciona para mayores y menores de edad.
