# pruebas/test_permutaciones.py
import sys
sys.path.append('..')
from problema1_permutaciones import permutaciones

def test_permutaciones():
    assert permutaciones(5,2) == 20
    assert permutaciones(6,0) == 1
    assert permutaciones(10,10) == 3628800
    assert permutaciones(4,1) == 4
    assert permutaciones(7,3) == 210
    print("Todas las pruebas de permutaciones pasaron.")

if __name__ == "__main__":
    test_permutaciones()
