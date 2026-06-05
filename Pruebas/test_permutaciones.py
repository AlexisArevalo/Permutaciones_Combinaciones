from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from problema1_permutaciones import factorial_iterativo, factorial_recursivo, permutaciones


def test_permutaciones():
    assert permutaciones(5, 2) == 20
    assert permutaciones(6, 0) == 1
    assert permutaciones(10, 10) == 3628800
    assert permutaciones(4, 1) == 4
    assert permutaciones(7, 3) == 210
    assert factorial_iterativo(5) == 120
    assert factorial_recursivo(6) == 720
    print("Todas las pruebas de permutaciones pasaron.")


def test_validaciones_permutaciones():
    for args in [(-1, 0), (3, 4), (2.5, 1)]:
        try:
            permutaciones(*args)
        except (TypeError, ValueError):
            pass
        else:
            raise AssertionError(f"Se esperaba error para {args}")


if __name__ == "__main__":
    test_permutaciones()
    test_validaciones_permutaciones()
