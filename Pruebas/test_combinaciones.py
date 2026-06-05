import sys
sys.path.append('..')
from problema2_combinaciones import combinaciones, verificar_simetria, fila_pascal

def test_combinaciones():
    assert combinaciones(5,2) == 10
    assert combinaciones(10,3) == 120
    assert combinaciones(6,0) == 1
    assert combinaciones(7,7) == 1
    assert combinaciones(8,4) == 70
    # Simetría
    assert combinaciones(8,3) == combinaciones(8,5)
    print("Pruebas de combinaciones exitosas.")

def test_fila_pascal():
    assert fila_pascal(4) == [1, 4, 6, 4, 1]
    print("Fila de Pascal correcta.")

if __name__ == "__main__":
    test_combinaciones()
    test_fila_pascal()
