"""Herramientas para calcular combinaciones y el triangulo de Pascal."""

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


def _formatear_procedimiento_combinacion(n, r):
    numerador = " x ".join(str(numero) for numero in range(n, n - r, -1)) or "1"
    denominador = " x ".join(str(numero) for numero in range(r, 0, -1)) or "1"
    return numerador, denominador


def combinaciones(n, r, usar_factoriales=True, mostrar_procedimiento=False):
    """Calcula C(n, r) = n! / (r! (n-r)!)."""
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
                _escribir(
                    f"Usamos la identidad de simetria: C({n}, {original_r}) = C({n}, {r}) para reducir el trabajo."
                )
            _escribir(f"Formula: C({n}, {original_r}) = n! / (r!(n-r)!)")
            _escribir(f"Reemplazando: C({n}, {original_r}) = {n}! / ({original_r}! x {n - original_r}!)")
            numerador, denominador = _formatear_procedimiento_combinacion(n, r)
            _escribir(f"Numerador expandido: {numerador}")
            _escribir(f"Denominador expandido: {denominador}")
            _escribir(f"Paso final: ({numerador}) / ({denominador}) = {resultado}")
        return resultado

    if r == 0:
        if mostrar_procedimiento:
            _escribir(
                f"C({n}, {original_r}) = 1 porque elegir 0 elementos siempre da un unico subconjunto."
            )
        return 1

    if mostrar_procedimiento:
        _escribir(
            f"C({n}, {original_r}) se calcula con la recurrencia de Pascal: C({n-1}, {r-1}) + C({n-1}, {r})."
        )
    return combinaciones(n - 1, r - 1, False, False) + combinaciones(n - 1, r, False, False)


def demostrar_identidad_simetria(n, r):
    """Explica por que C(n, r) = C(n, n-r)."""
    valor = combinaciones(n, r)
    valor_simetrico = combinaciones(n, n - r)
    _escribir(f"Queremos demostrar que C({n}, {r}) = C({n}, {n-r}).")
    _escribir(f"Ambos valores se calculan con la misma cantidad de subconjuntos: {valor} y {valor_simetrico}.")
    _escribir("La igualdad se cumple porque elegir r elementos deja exactamente n-r elementos sin elegir.")
    _escribir("Por eso, escoger r elementos o escoger los n-r restantes describe la misma particion del conjunto.")
    _escribir(f"Conclusión: C({n}, {r}) = C({n}, {n-r}) = {valor}.")


def verificar_simetria(n, r):
    """Verifica que C(n, r) == C(n, n-r)."""
    c1 = combinaciones(n, r)
    c2 = combinaciones(n, n - r)
    if c1 == c2:
        _escribir(f"C({n}, {r}) = {c1} y C({n}, {n-r}) = {c2}. La simetria se cumple.")
    else:
        _escribir(f"C({n}, {r}) = {c1} y C({n}, {n-r}) = {c2}. La simetria no se cumple.")
    return c1 == c2


def fila_pascal(n):
    """Devuelve la fila n del triangulo de Pascal."""
    _validar_enteros_no_negativos(n)
    return [combinaciones(n, r) for r in range(n + 1)]


def triangulo_pascal(hasta_n):
    """Genera el triangulo de Pascal desde la fila 0 hasta hasta_n."""
    _validar_enteros_no_negativos(hasta_n)
    return [fila_pascal(n) for n in range(hasta_n + 1)]


def mostrar_triangulo_pascal(hasta_n):
    """Imprime el triangulo de Pascal centrado."""
    triangulo = triangulo_pascal(hasta_n)
    if not triangulo:
        return

    ancho_total = len("   ".join(str(numero) for numero in triangulo[-1]))
    for fila in triangulo:
        renglon = "   ".join(str(numero) for numero in fila)
        _escribir(renglon.center(ancho_total))


def mostrar_pruebas_combinaciones():
    """Muestra varias pruebas y casos especiales."""
    _escribir("Pruebas de combinaciones")
    pruebas = [(5, 2), (10, 3), (6, 0), (7, 7), (8, 4)]
    for n, r in pruebas:
        _escribir(f"C({n}, {r}) = {combinaciones(n, r)}")

    _escribir("Casos especiales y validaciones")
    especiales = [(-1, 2), (3, 5), (2.5, 1)]
    for n, r in especiales:
        try:
            combinaciones(n, r)
        except Exception as error:
            _escribir(f"C({n}, {r}) genera validacion: {error}")

    _escribir("Verificacion de simetria")
    verificar_simetria(8, 3)
    _escribir("Demostracion detallada de la simetria")
    demostrar_identidad_simetria(8, 3)


if __name__ == "__main__":
    _escribir("=== Calculadora de Combinaciones ===")
    casos = [(5, 2), (10, 3), (6, 0), (7, 7), (8, 4)]
    for n, r in casos:
        try:
            resultado = combinaciones(n, r, mostrar_procedimiento=True)
            _escribir(f"Resultado final: C({n}, {r}) = {resultado}")
            verificar_simetria(n, r)
        except Exception as error:
            _escribir(f"Error: {error}")
        _escribir("")

    _escribir("Fila 6 del triangulo de Pascal:")
    _escribir(str(fila_pascal(6)))
    _escribir("Triangulo de Pascal hasta fila 5:")
    mostrar_triangulo_pascal(5)
