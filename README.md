# Permutaciones_Combinaciones
Bono de programación – Matemáticas Discretas I – Calculadora de permutaciones y combinaciones

**Autor:** [Sebastian Alexis Arévalo Grande]  
**Problemas escogidos:** 1 (Permutaciones) y 2 (Combinaciones)

## Instrucciones de ejecución

1. Asegúrate de tener Python 3.8+ instalado.
2. Clona el repositorio o descarga los archivos.
3. Ejecuta cada programa por separado:
   ```bash
   python Permutaciones.py
   python Combinaciones.py

4. Para ejecutar las pruebas:
   ```bash
   python -m pytest pruebas/ 
   # o ejecuta cada archivo de prueba directamente
   python pruebas/test_permutaciones.py
   python pruebas/test_combinaciones.py

Explicación breve de los problemas
Problema 1 – Calculadora de permutaciones
Permite calcular el número de formas de ordenar r objetos tomados de un total de n objetos distintos.
Fórmula: P(n,r) = n! / (n-r)!
Funciones: permutaciones(n, r, mostrar_procedimiento), calcular_factorial(n, metodo).

Problema 2 – Calculadora de combinaciones
Calcula el número de subconjuntos de tamaño r de un conjunto de n elementos.
Fórmula: C(n,r) = n! / (r! (n-r)!)
Propiedades: Simetría, generación del triángulo de Pascal.
Funciones: combinaciones(n, r), fila_pascal(n), triangulo_pascal(hasta_n).

Ejemplos de entrada y salida

Permutaciones
   ```bash
    P(10,3) = 10 × 9 × 8 = 720
   P(20,5) = 20 × 19 × 18 × 17 × 16 = 1860480


   
