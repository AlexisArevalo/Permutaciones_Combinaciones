from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from problema2_combinaciones import combinaciones, fila_pascal, triangulo_pascal, verificar_simetria


def test_combinaciones():
    assert combinaciones(5, 2) == 10
    assert combinaciones(10, 3) == 120
    assert combinaciones(6, 0) == 1
    assert combinaciones(7, 7) == 1
    assert combinaciones(8, 4) == 70
    assert combinaciones(8, 3) == combinaciones(8, 5)
    assert triangulo_pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print("Pruebas de combinaciones exitosas.")


def test_fila_pascal():
    assert fila_pascal(4) == [1, 4, 6, 4, 1]
    print("Fila de Pascal correcta.")


def test_validaciones_combinaciones():
    for args in [(-1, 0), (3, 4), (2.5, 1)]:
        try:
            combinaciones(*args)
        except (TypeError, ValueError):
            pass
        else:
            raise AssertionError(f"Se esperaba error para {args}")


if __name__ == "__main__":
    test_combinaciones()
    test_fila_pascal()
    test_validaciones_combinaciones()
