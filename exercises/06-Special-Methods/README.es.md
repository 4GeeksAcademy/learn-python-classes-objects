# 06 Metodos especiales

## Objetivo

En este ejercicio vas a practicar metodos especiales para representar y comparar objetos.

## Concepto clave

Los metodos especiales permiten que tus clases se integren mejor con Python.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person` con `name` y `age`.
2. Implementa `__str__` para retornar: `"Person: <name> (<age> years old)"`.
3. Implementa `__repr__` para retornar: `"Person(name='<name>', age=<age>)"`.
4. Implementa `__eq__` para que dos personas sean iguales si tienen mismo `name` y misma `age`.
5. Crea estas instancias:
   - `student = Person("John", 21)`
   - `student_clone = Person("John", 21)`

## Criterio de exito

El ejercicio se considera correcto cuando:

- `str(student)` retorna el formato esperado.
- `repr(student)` retorna el formato esperado.
- `student == student_clone` es `True`.
