# 08 Composicion (has-a)

## Objetivo

En este ejercicio vas a practicar composicion, modelando un objeto que contiene otro objeto.

## Concepto clave

La composicion permite construir modelos mas ricos combinando objetos pequenos con responsabilidades claras.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase `Address` con `city` y `country`.
2. Crea una clase `Person` con `name` y `address`.
3. En `Person`, crea un metodo `full_address()` que retorne: `"<city>, <country>"`.
4. Crea una instancia `student` con:
   - `name`: `"John"`
   - `address`: `Address("Miami", "USA")`

## Criterio de exito

El ejercicio se considera correcto cuando:

- `student.address` es una instancia de `Address`.
- `student.full_address()` retorna `"Miami, USA"`.
