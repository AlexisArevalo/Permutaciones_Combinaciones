"""Herramientas para calcular combinaciones y el triangulo de Pascal."""


def _validar_enteros_no_negativos(*valores):
    for valor in valores:
        if not isinstance(valor, int):
            raise TypeError("n y r deben ser enteros.")
        if valor < 0:
            raise ValueError("n y r deben ser no negativos.")


def _formatear_procedimiento_combinacion(n, r):
    numerador = " x ".join(str(numero) for numero in range(n, n - r, -1)) or "1"
    denominador = " x ".join(str(numero) for numero in range(r, 0, -1)) or "1"
    return numerador, denominador


def combinaciones(n, r, usar_factoriales=True, mostrar_procedimiento=False):
    """Calcula C(n, r) = n! / (r! (n-r)!).

    Si usar_factoriales es False, usa la recurrencia de Pascal para mostrar
    una alternativa educativa mas lenta.
    """
    _validar_enteros_no_negativos(n, r)
    if r > n:
        raise ValueError(f"r ({r}) no puede ser mayor que n ({n}).")

    original_r = r
    r = min(r, n - r)

    if usar_factoriales:
        resultado = 1
        for i in range(1, r + 1):
            resultado = resultado * (n - r + i) // i

        if mostrar_procedimiento:
            if original_r != r:
                print(
                    f"Usamos simetria: C({n}, {original_r}) = C({n}, {r}) para reducir el trabajo."
                )
            numerador, denominador = _formatear_procedimiento_combinacion(n, r)
            print(
                f"Paso a paso: ({numerador}) / ({denominador}) = {resultado}."
            )
        return resultado

    if r == 0:
        if mostrar_procedimiento:
            print(
                f"C({n}, {original_r}) = 1 porque elegir 0 elementos siempre da un unico subconjunto."
            )
        return 1

    if mostrar_procedimiento:
        print(
            f"C({n}, {original_r}) se calcula con la recurrencia de Pascal: "
            f"C({n-1}, {r-1}) + C({n-1}, {r})."
        )
    return combinaciones(n - 1, r - 1, False, False) + combinaciones(n - 1, r, False, False)


def verificar_simetria(n, r):
    """Verifica que C(n, r) == C(n, n-r)."""
    c1 = combinaciones(n, r)
    c2 = combinaciones(n, n - r)
    print(
        f"C({n},{r}) = {c1} y C({n},{n-r}) = {c2}. "
        f"{'La simetria se cumple.' if c1 == c2 else 'La simetria no se cumple.'}"
    )
    return c1 == c2


def fila_pascal(n):
    """Devuelve la fila n del triangulo de Pascal."""
    _validar_enteros_no_negativos(n)
    fila = []
    for r in range(n + 1):
        fila.append(combinaciones(n, r))
    return fila


def triangulo_pascal(hasta_n):
    """Genera el triangulo de Pascal desde la fila 0 hasta hasta_n."""
    _validar_enteros_no_negativos(hasta_n)
    triangulo = []
    for n in range(hasta_n + 1):
        triangulo.append(fila_pascal(n))
    return triangulo


def mostrar_triangulo_pascal(hasta_n):
    """Imprime el triangulo de Pascal centrado."""
    triangulo = triangulo_pascal(hasta_n)
    if not triangulo:
        return

    ultimo_renglon = "   ".join(str(numero) for numero in triangulo[-1])
    ancho_total = len(ultimo_renglon)

    for fila in triangulo:
        renglon = "   ".join(str(numero) for numero in fila)
        print(renglon.center(ancho_total))


if __name__ == "__main__":
    print("=== Calculadora de Combinaciones ===")
    casos = [(5, 2), (10, 3), (6, 0), (7, 7), (8, 4)]
    for n, r in casos:
        try:
            c = combinaciones(n, r, mostrar_procedimiento=True)
            print(f"Resultado final: C({n},{r}) = {c}")
            verificar_simetria(n, r)
        except Exception as error:
            print(f"Error: {error}")
        print()

    print("Fila 6 del triangulo de Pascal:", fila_pascal(6))
    print("\nTriangulo de Pascal hasta fila 5:")
    mostrar_triangulo_pascal(5)
