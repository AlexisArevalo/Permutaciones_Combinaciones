import math

def combinaciones(n, r, usar_factoriales=True):
    """
    Calcula C(n, r) = n! / (r! (n-r)!).
    usar_factoriales=True usa factoriales; False usa recursión de Pascal.
    """
    if not (isinstance(n, int) and isinstance(r, int)):
        raise TypeError("n y r deben ser enteros.")
    if n < 0 or r < 0:
        raise ValueError("n y r deben ser no negativos.")
    if r > n:
        raise ValueError(f"r ({r}) no puede ser mayor que n ({n}).")
    
    # Simetría para optimizar
    r = min(r, n - r)
    
    if usar_factoriales:
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    else:
        # Método recursivo (menos eficiente, solo educativo)
        if r == 0 or r == n:
            return 1
        return combinaciones(n-1, r-1, False) + combinaciones(n-1, r, False)

def verificar_simetria(n, r):
    """Verifica que C(n,r) == C(n, n-r)."""
    c1 = combinaciones(n, r)
    c2 = combinaciones(n, n - r)
    print(f"C({n},{r}) = {c1}, C({n},{n-r}) = {c2} → {'OK' if c1==c2 else 'ERROR'}")
    return c1 == c2

def fila_pascal(n):
    """Devuelve la fila n del triángulo de Pascal (lista de enteros)."""
    fila = []
    for r in range(n+1):
        fila.append(combinaciones(n, r))
    return fila

def triangulo_pascal(hasta_n):
    """Genera todo el triángulo de Pascal desde fila 0 hasta hasta_n."""
    triangulo = []
    for n in range(hasta_n + 1):
        triangulo.append(fila_pascal(n))
    return triangulo

# Ejemplos de uso y pruebas
if __name__ == "__main__":
    print("=== Calculadora de Combinaciones ===")
    casos = [(5,2), (10,3), (6,0), (7,7), (8,4)]
    for n, r in casos:
        try:
            c = combinaciones(n, r)
            print(f"C({n},{r}) = {c}")
            verificar_simetria(n, r)
        except Exception as e:
            print(f"Error: {e}")
        print()
    
    print("Fila 6 del triángulo de Pascal:", fila_pascal(6))
    print("\nTriángulo de Pascal hasta fila 5:")
    for i, fila in enumerate(triangulo_pascal(5)):
        print(f"Fila {i}: {fila}")
