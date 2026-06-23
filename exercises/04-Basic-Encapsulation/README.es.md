# 04 Encapsulamiento básico

## Objetivo

En este ejercicio vas a practicar encapsulamiento usando atributos internos y métodos de acceso controlado.

## Concepto clave

En POO, el encapsulamiento protege el estado del objeto para evitar cambios directos que puedan romper su consistencia.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person`.
2. En `__init__`, recibe `name` y `age`.
3. Guarda esos valores en atributos internos: `self._name` y `self._age`.
4. Crea un método `get_name()` que retorne el nombre.
5. Crea un método `get_age()` que retorne la edad.
6. Crea un método `set_age(new_age)` que:
   - actualice la edad si `new_age` es mayor o igual a 0 y retorne `True`.
   - no cambie nada si `new_age` es menor que 0 y retorne `False`.
7. Crea una instancia `student = Person("John", 21)`.

## Criterio de éxito

El ejercicio se considera correcto cuando:

- `Person` usa `_name` y `_age` como estado interno.
- `get_name()` y `get_age()` retornan los valores correctos.
- `set_age()` valida y actualiza según la regla definida.
