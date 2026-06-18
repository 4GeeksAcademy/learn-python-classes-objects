# 02 Constructor y estado inicial

## Objetivo

En este ejercicio vas a aprender a inicializar el estado de un objeto usando el metodo constructor `__init__`.

## Concepto clave

En POO, una clase define la estructura y comportamiento.

El constructor `__init__` se ejecuta automaticamente cuando creas una instancia y sirve para guardar los datos iniciales del objeto.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase llamada `Person`.
2. Agrega un constructor `__init__` que reciba dos parametros: `name` y `age`.
3. Guarda esos valores en atributos de instancia con el mismo nombre: `self.name` y `self.age`.
4. Crea una instancia llamada `student` con los valores:
   - `name`: `"John"`
   - `age`: `21`

## Criterio de exito

El ejercicio se considera correcto cuando:

- Existe la clase `Person`.
- `Person` tiene un constructor que guarda `name` y `age`.
- Existe `student`.
- `student.name` es `"John"`.
- `student.age` es `21`.
