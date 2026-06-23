# 10 Herencia y reutilización

## Objetivo

En este ejercicio vas a practicar herencia para reutilizar comportamiento entre clases relacionadas.

## Concepto clave

La herencia permite definir una clase base con comportamiento común y extenderla en subclases.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase base `Person` con `name` y `age`.
2. En `Person`, crea un método `describe()` que retorne: `"Name: <name>, Age: <age>"`.
3. Crea una subclase `Student(Person)` con un atributo extra `cohort`.
4. En `Student`, sobrescribe `describe()` para incluir cohorte: `"Name: <name>, Age: <age>, Cohort: <cohort>"`.
5. Usa `super()` para reutilizar la inicialización de `Person`.
6. Crea una instancia global `student = Student("John", 21, "42")`.

## Criterio de éxito

El ejercicio se considera correcto cuando:

- `Student` hereda de `Person`.
- `student.describe()` retorna el texto con cohorte.
- Se reutiliza correctamente la clase base.
