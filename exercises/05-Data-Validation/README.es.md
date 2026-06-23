# 05 Validación de datos

## Objetivo

En este ejercicio vas a practicar cómo validar datos para mantener objetos en un estado válido.

## Concepto clave

En POO, validar en el constructor y en métodos de actualización evita crear objetos incoherentes.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person`.
2. En `__init__`, recibe `name` y `age`.
3. Valida que:
   - `name` sea texto no vacio.
   - `age` sea entero mayor o igual a 0.
4. Si algún valor es inválido, lanza `ValueError`.
5. Crea un método `set_age(new_age)` que aplique la misma validación de edad y actualice el valor.
6. Crea una instancia valida: `student = Person("John", 21)`.

## Criterio de éxito

El ejercicio se considera correcto cuando:

- Se crean personas válidas correctamente.
- Entradas inválidas lanzan `ValueError`.
- `set_age()` actualiza solo cuando la edad es válida.
