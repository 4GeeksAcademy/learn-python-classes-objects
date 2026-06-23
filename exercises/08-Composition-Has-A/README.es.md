# 08 Composición (has-a)

## Objetivo

En este ejercicio vas a practicar composición, modelando un objeto que contiene otro objeto.

## Concepto clave

La composición permite construir modelos más ricos combinando objetos pequeños con responsabilidades claras.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Address` con `city` y `country`.
2. Crea una clase `Person` con `name` y `address`.
3. En `Person`, crea un método `full_address()` que retorne: `"<city>, <country>"`.
4. Crea una instancia `student` con:
   - `name`: `"John"`
   - `address`: `Address("Miami", "USA")`

## Criterio de éxito

El ejercicio se considera correcto cuando:

- `student.address` es una instancia de `Address`.
- `student.full_address()` retorna `"Miami, USA"`.
