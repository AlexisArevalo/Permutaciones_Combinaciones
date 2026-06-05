"""Herramientas para calcular permutaciones y factoriales."""


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


def permutaciones(n, r, mostrar_procedimiento=False):
    """Calcula P(n, r) = n! / (n-r)!.

    Usa el producto de r terminos consecutivos desde n hacia abajo, que es
    equivalente a la formula factorial y evita calcular factoriales completos.
    """
    _validar_enteros_no_negativos(n, r)
    if r > n:
        raise ValueError(f"r ({r}) no puede ser mayor que n ({n}).")

    if r == 0:
        if mostrar_procedimiento:
            print(f"P({n},{r}) = 1")
        return 1

    resultado = 1
    procedimiento = []
    for i in range(r):
        termino = n - i
        resultado *= termino
        if mostrar_procedimiento:
            procedimiento.append(str(termino))

    if mostrar_procedimiento:
        print(f"P({n},{r}) = {' x '.join(procedimiento)} = {resultado}")
    return resultado


def calcular_factorial(n, metodo="iterativo"):
    """Permite calcular n! con el metodo elegido."""
    if metodo == "iterativo":
        return factorial_iterativo(n)
    if metodo == "recursivo":
        return factorial_recursivo(n)
    raise ValueError("Metodo debe ser 'iterativo' o 'recursivo'.")


if __name__ == "__main__":
    print("=== Calculadora de Permutaciones ===")
    casos = [(10, 3), (20, 5), (5, 0), (5, 5), (0, 0)]
    for n, r in casos:
        try:
            p = permutaciones(n, r, mostrar_procedimiento=True)
            print(f"Resultado: {p}\n")
        except Exception as error:
            print(f"Error con P({n},{r}): {error}\n")

    print("Comparacion:")
    print(f"P(10,3) = {permutaciones(10, 3)}")
    print(f"P(20,5) = {permutaciones(20, 5)}")
    print(f"La razon P(20,5)/P(10,3) es {permutaciones(20, 5) / permutaciones(10, 3):.2e}")
