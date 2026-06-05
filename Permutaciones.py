import math

def factorial_iterativo(n):
    """Calcula n! de forma iterativa."""
    if n < 0:
        raise ValueError("El factorial no está definido para negativos.")
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    """Calcula n! de forma recursiva (solo para demostración)."""
    if n < 0:
        raise ValueError("Factorial de negativo no definido.")
    if n == 0:
        return 1
    return n * factorial_recursivo(n-1)

def permutaciones(n, r, mostrar_procedimiento=False):
    """
    Calcula P(n, r) = n! / (n-r)!.
    Valida entradas y opcionalmente muestra el procedimiento.
    """
    # Validaciones
    if not (isinstance(n, int) and isinstance(r, int)):
        raise TypeError("n y r deben ser enteros.")
    if n < 0 or r < 0:
        raise ValueError("n y r deben ser no negativos.")
    if r > n:
        raise ValueError(f"r ({r}) no puede ser mayor que n ({n}).")
    
    # Optimización: producto de r términos desde n hacia abajo
    resultado = 1
    procedimiento = []
    for i in range(r):
        termino = n - i
        resultado *= termino
        if mostrar_procedimiento:
            procedimiento.append(str(termino))
    
    if mostrar_procedimiento:
        print(f"P({n},{r}) = {' × '.join(procedimiento)} = {resultado}")
    return resultado

def calcular_factorial(n, metodo='iterativo'):
    """Permite calcular n! con el método elegido."""
    if metodo == 'iterativo':
        return factorial_iterativo(n)
    elif metodo == 'recursivo':
        return factorial_recursivo(n)
    else:
        raise ValueError("Método debe ser 'iterativo' o 'recursivo'.")

# Ejemplo de comparación
if __name__ == "__main__":
    # Pruebas básicas
    print("=== Calculadora de Permutaciones ===")
    casos = [(10,3), (20,5), (5,0), (5,5), (0,0)]
    for n, r in casos:
        try:
            p = permutaciones(n, r, mostrar_procedimiento=True)
            print(f"Resultado: {p}\n")
        except Exception as e:
            print(f"Error con P({n},{r}): {e}\n")
    
    # Comparación adicional
    print("Comparación:")
    print(f"P(10,3) = {permutaciones(10,3)}")
    print(f"P(20,5) = {permutaciones(20,5)}")
    print(f"La razón P(20,5)/P(10,3) es {permutaciones(20,5)/permutaciones(10,3):.2e}")
