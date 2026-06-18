# 03 Metodos de instancia

## Objetivo

En este ejercicio vas a practicar como agregar comportamiento a un objeto usando metodos de instancia.

## Concepto clave

En POO, los atributos representan el estado del objeto y los metodos representan lo que el objeto puede hacer.

Un metodo de instancia siempre recibe `self`, que referencia al objeto actual.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase llamada `Person`.
2. Agrega un constructor `__init__` que reciba `name` y `age`.
3. Guarda esos valores en `self.name` y `self.age`.
4. Agrega un metodo de instancia llamado `greet` que retorne este texto:
   - `"Hi, my name is <name>"`
5. Agrega un metodo de instancia llamado `have_birthday` que aumente la edad en 1.
6. Crea una instancia llamada `student` con:
   - `name`: `"John"`
   - `age`: `21`

## Criterio de exito

El ejercicio se considera correcto cuando:

- Existe la clase `Person`.
- `student` es instancia de `Person`.
- `student.greet()` retorna `"Hi, my name is John"`.
- Al ejecutar `student.have_birthday()`, la edad aumenta en 1.
