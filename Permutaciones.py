"""Herramientas para calcular permutaciones y factoriales."""

from time import sleep


def _escribir(texto, salto=True, demora=0.002):
    for caracter in str(texto):
        print(caracter, end="", flush=True)
        sleep(demora)
    if salto:
        print()


def _validar_enteros_no_negativos(*valores):
    for valor in valores:
        if not isinstance(valor, int):
            raise TypeError("n y r deben ser enteros.")
        if valor < 0:
            raise ValueError("n y r deben ser no negativos.")


def factorial_iterativo(n):
    """Calcula n! de forma iterativa."""
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero.")
    if n < 0:
        raise ValueError("El factorial no esta definido para negativos.")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    """Calcula n! de forma recursiva, para comparacion didactica."""
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero.")
    if n < 0:
        raise ValueError("El factorial no esta definido para negativos.")
    if n in (0, 1):
        return 1
    return n * factorial_recursivo(n - 1)


def mostrar_comparacion_factoriales(n):
    """Muestra una comparacion entre factorial iterativo y recursivo."""
    resultado_iterativo = factorial_iterativo(n)
    resultado_recursivo = factorial_recursivo(n)
    _escribir(f"Comparacion de factoriales para {n}!")
    _escribir(f"Metodo iterativo  -> {resultado_iterativo}")
    _escribir(f"Metodo recursivo  -> {resultado_recursivo}")
    if resultado_iterativo == resultado_recursivo:
        _escribir("Ambos metodos coinciden exactamente.")
    else:
        _escribir("Los metodos no coinciden, revisa la implementacion.")


def permutaciones(n, r, mostrar_procedimiento=False):
    """Calcula P(n, r) = n! / (n-r)!."""
    _validar_enteros_no_negativos(n, r)
    if r > n:
        raise ValueError(f"r ({r}) no puede ser mayor que n ({n}).")

    if r == 0:
        if mostrar_procedimiento:
            _escribir(f"P({n}, {r}) = 1 porque no se elige ningun elemento.")
        return 1

    resultado = 1
    if mostrar_procedimiento:
        _escribir(f"Usamos la formula: P({n}, {r}) = n! / (n-r)!")
        _escribir(f"Reemplazando: P({n}, {r}) = {n}! / ({n}-{r})! = {n}! / {n-r}!")
        _escribir(f"Ahora multiplicamos {r} terminos consecutivos desde {n}:")

    for paso, termino in enumerate(range(n, n - r, -1), start=1):
        resultado *= termino
        if mostrar_procedimiento:
            _escribir(f"Paso {paso}: multiplicamos por {termino} -> acumulado = {resultado}")

    if mostrar_procedimiento:
        _escribir(f"Resultado final: P({n}, {r}) = {resultado}")
    return resultado


def calcular_factorial(n, metodo="iterativo"):
    """Permite calcular n! con el metodo elegido."""
    if metodo == "iterativo":
        return factorial_iterativo(n)
    if metodo == "recursivo":
        return factorial_recursivo(n)
    raise ValueError("Metodo debe ser 'iterativo' o 'recursivo'.")


def mostrar_pruebas_permutaciones():
    """Muestra varias pruebas y casos especiales."""
    _escribir("Pruebas de permutaciones")
    pruebas = [(5, 2), (6, 0), (10, 10), (4, 1), (7, 3)]
    for n, r in pruebas:
        _escribir(f"P({n}, {r}) = {permutaciones(n, r)}")

    _escribir("Casos especiales y validaciones")
    especiales = [(-1, 2), (3, 5), (2.5, 1)]
    for n, r in especiales:
        try:
            permutaciones(n, r)
        except Exception as error:
            _escribir(f"P({n}, {r}) genera validacion: {error}")

    _escribir("Comparacion de factoriales")
    mostrar_comparacion_factoriales(6)


if __name__ == "__main__":
    _escribir("=== Calculadora de Permutaciones ===")
    casos = [(10, 3), (20, 5), (5, 0), (5, 5), (0, 0)]
    for n, r in casos:
        try:
            resultado = permutaciones(n, r, mostrar_procedimiento=True)
            _escribir(f"Resultado: {resultado}")
        except Exception as error:
            _escribir(f"Error con P({n}, {r}): {error}")
        _escribir("")

    _escribir("Comparacion de casos:")
    _escribir(f"P(10, 3) = {permutaciones(10, 3)}")
    _escribir(f"P(20, 5) = {permutaciones(20, 5)}")
    _escribir(f"La razon P(20, 5) / P(10, 3) es {permutaciones(20, 5) / permutaciones(10, 3):.2e}")
