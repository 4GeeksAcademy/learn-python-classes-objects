# 11 Polimorfismo y abstracción aplicada

## Objetivo

En este ejercicio vas a aplicar polimorfismo usando una interfaz común entre clases diferentes.

## Concepto clave

El polimorfismo permite tratar objetos distintos de forma uniforme cuando comparten un mismo contrato de métodos.

## Instrucciones

Trabaja en `app.py` y completa exactamente lo siguiente:

1. Crea una clase base `Animal` con un método `speak()` que lance `NotImplementedError`.
2. Crea una clase `Dog(Animal)` que implemente `speak()` y retorne `"Woof"`.
3. Crea una clase `Cat(Animal)` que implemente `speak()` y retorne `"Meow"`.
4. Crea una función `make_it_speak(animal)` que retorne `animal.speak()`.
5. Crea dos instancias globales:
   - `dog = Dog()`
   - `cat = Cat()`

## Criterio de éxito

El ejercicio se considera correcto cuando:

- `make_it_speak(dog)` retorna `"Woof"`.
- `make_it_speak(cat)` retorna `"Meow"`.
- Se aplica el mismo flujo a tipos distintos sin condicionales por tipo.
