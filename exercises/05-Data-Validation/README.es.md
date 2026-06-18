# 05 Validacion de datos

## Objetivo

En este ejercicio vas a practicar como validar datos para mantener objetos en un estado valido.

## Concepto clave

En POO, validar en el constructor y en metodos de actualizacion evita crear objetos incoherentes.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person`.
2. En `__init__`, recibe `name` y `age`.
3. Valida que:
   - `name` sea texto no vacio.
   - `age` sea entero mayor o igual a 0.
4. Si algun valor es invalido, lanza `ValueError`.
5. Crea un metodo `set_age(new_age)` que aplique la misma validacion de edad y actualice el valor.
6. Crea una instancia valida: `student = Person("John", 21)`.

## Criterio de exito

El ejercicio se considera correcto cuando:

- Se crean personas validas correctamente.
- Entradas invalidas lanzan `ValueError`.
- `set_age()` actualiza solo cuando la edad es valida.
