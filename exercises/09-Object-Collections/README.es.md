# 09 Colecciones de objetos

## Objetivo

En este ejercicio vas a practicar manejo de colecciones de objetos dentro de otra clase.

## Concepto clave

Cuando un problema involucra varios objetos del mismo tipo, una clase contenedora ayuda a centralizar operaciones.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person` con `name` y `age`.
2. Crea una clase `Classroom` con una lista interna de estudiantes.
3. En `Classroom`, implementa:
   - `add_student(person)`
   - `remove_student_by_name(name)` que retorne `True` si elimina, `False` si no encuentra.
   - `find_student(name)` que retorne el objeto o `None`.
   - `total_students()` que retorne la cantidad de estudiantes.
4. Crea una instancia `bootcamp = Classroom()`.

## Criterio de exito

El ejercicio se considera correcto cuando:

- Se pueden agregar y eliminar estudiantes correctamente.
- Se pueden buscar estudiantes por nombre.
- `total_students()` refleja la cantidad real en la coleccion.
