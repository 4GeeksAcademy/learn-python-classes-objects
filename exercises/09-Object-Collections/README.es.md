# 09 Colecciones de objetos

## Objetivo

En este ejercicio vas a practicar manejo de colecciones de objetos dentro de otra clase.

## Concepto clave

Cuando un problema involucra varios objetos del mismo tipo, una clase contenedora ayuda a centralizar operaciones.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Person` con `name` y `age`.
2. Crea una clase `Classroom` y, dentro de `__init__`, inicializa una lista vacía para guardar estudiantes (por ejemplo: `self.students = []`).
3. En `Classroom`, implementa:
   - `add_student(person)` para agregar una instancia de `Person` al final de la lista.
   - `remove_student_by_name(name)` que elimine la primera coincidencia por nombre y retorne `True`; si no encuentra, retorne `False`.
   - `find_student_by_name(name)` que retorne la primera coincidencia por nombre o `None`.
   - `total_students()` que retorne la cantidad de estudiantes.
4. Crea una instancia `bootcamp = Classroom()`.

Nota: en este ejercicio no necesitas validaciones extra de tipos; enfócate en la lógica de colección.

## Criterio de éxito

El ejercicio se considera correcto cuando:

- Se pueden agregar y eliminar estudiantes correctamente.
- Se pueden buscar estudiantes por nombre.
- `total_students()` refleja la cantidad real en la colección.
- `Classroom` mantiene su colección en una lista interna inicializada en `__init__`.
