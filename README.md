# Permutaciones_Combinaciones
Bono de programacion - Matematicas Discretas I

Repositorio preparado para los dos primeros problemas del PDF:

1. Permutaciones generales y k-permutaciones.
2. Combinaciones generales y triangulo de Pascal.

## Idea del proyecto

El objetivo es convertir dos modelos de conteo en herramientas reutilizables y faciles de ejecutar. El usuario puede abrir un menu interactivo, elegir si quiere trabajar con permutaciones o combinaciones, ingresar sus valores y obtener el resultado con validaciones, procedimiento y ejemplos.

## Punto de entrada

- `main.py`: menu interactivo principal.
- `Permutaciones.py`: funciones para factorial, permutaciones y pruebas.
- `Combinaciones.py`: funciones para combinaciones, simetria, Pascal y pruebas.

## Como ejecutar

### Menu interactivo

```bash
py main.py
```

### Ejecucion directa por problema

```bash
py Permutaciones.py
py Combinaciones.py
```

## Estructura del menu

- `1. Permutaciones`
  - calcular factorial
  - calcular `P(n, r)`
  - comparar dos casos
  - comparar factorial iterativo y recursivo
  - ver pruebas y casos especiales
- `2. Combinaciones`
  - calcular `C(n, r)`
  - ver el procedimiento de calculo
  - verificar simetria `C(n, r) = C(n, n-r)`
  - generar una fila de Pascal
  - generar el triangulo de Pascal hasta una fila dada
  - ver pruebas y casos especiales
- `3. Pruebas y casos especiales`
- `0. Salir`

## Problema 1: Permutaciones

### Descripcion matematica

Se cuenta el numero de formas de ordenar `r` objetos distintos tomados de un total de `n` objetos distintos, sin repetir y considerando el orden.

### Formula usada

```text
P(n, r) =      n!
          -------------
          (n - r)!
```

### Algoritmo

El programa no calcula factoriales completos para la permutacion. En su lugar multiplica `r` terminos consecutivos desde `n` hacia abajo, lo que produce el mismo resultado con menos trabajo.

### Casos especiales

- `r = 0` devuelve `1`.
- `r = n` devuelve `n!`.
- `n` o `r` negativos generan error.
- entradas no enteras generan error.
- si `r > n`, el programa informa que la entrada no es valida.

### Eficiencia

- Tiempo: `O(r)`
- Espacio: `O(1)`

### Ejemplos incluidos

- `P(5,2) = 20`
- `P(10,10) = 3628800`
- `P(20,5) = 1860480`

## Problema 2: Combinaciones

### Descripcion matematica

Se cuenta el numero de subconjuntos de tamano `r` que pueden elegirse desde un conjunto de `n` elementos, sin importar el orden.

### Formula usada

```text
C(n, r) =          n!
          ----------------------
          r! x (n - r)!
```

### Algoritmo

El programa usa la simetria `C(n, r) = C(n, n-r)` para reducir el trabajo y luego calcula el valor con un producto entero estable. Adicionalmente, puede mostrar el procedimiento de calculo, generar la fila de Pascal y dibujar el triangulo completo centrado.

### Casos especiales

- `r = 0` devuelve `1`.
- `r = n` devuelve `1`.
- `r > n` genera error.
- `n` o `r` negativos generan error.
- entradas no enteras generan error.

### Eficiencia

- Tiempo: `O(min(r, n-r))`
- Espacio: `O(1)`

### Ejemplos incluidos

- `C(5,2) = 10`
- `C(8,4) = 70`
- `C(4,0) = 1`
- Fila 4 de Pascal: `[1, 4, 6, 4, 1]`
- Triangulo de Pascal centrado para lectura visual.

## Pruebas y validacion

Las pruebas incluidas cubren:

- al menos cinco casos de permutaciones;
- al menos cinco casos de combinaciones;
- validacion de entradas negativas, no enteras y casos donde `r > n`;
- verificacion de la simetria de las combinaciones;
- construccion de la fila y del triangulo de Pascal;
- verificacion del procedimiento mostrado en combinaciones;
- demostracion detallada de la identidad `C(n, r) = C(n, n-r)`.

## Archivos de apoyo

- `problema1_permutaciones.py`
- `problema2_combinaciones.py`
- `Pruebas/test_permutaciones.py`
- `Pruebas/test_combinaciones.py`

## Resultado de la entrega

Este repositorio cumple con lo pedido para los dos primeros ejercicios del documento:

- explicacion breve del problema;
- formula o principio combinatorio;
- algoritmo implementado;
- codigo funcional;
- pruebas con varios valores;
- validacion de casos especiales;
- comentario de eficiencia;
- menu interactivo para uso directo;
- presentacion mas dinamica y explicativa.
