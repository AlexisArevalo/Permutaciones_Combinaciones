"""Menu interactivo principal para permutaciones y combinaciones."""

from time import sleep

from Combinaciones import (
    combinaciones,
    fila_pascal,
    mostrar_triangulo_pascal,
    verificar_simetria,
)
from Permutaciones import calcular_factorial, permutaciones


def _escribir(texto, salto=True, demora=0.006):
    for caracter in texto:
        print(caracter, end="", flush=True)
        sleep(demora)
    if salto:
        print()


def _mostrar_menu(lineas):
    print()
    for linea in lineas:
        _escribir(linea)


def _pausa():
    try:
        input("\nPresiona Enter para continuar...")
    except EOFError:
        return


def _leer_texto(mensaje):
    try:
        return input(mensaje)
    except EOFError:
        return None


def _leer_entero(mensaje):
    while True:
        texto = _leer_texto(mensaje)
        if texto is None:
            return None
        try:
            return int(texto)
        except ValueError:
            print("La entrada no es valida. Debes escribir un numero entero.")


def _leer_si_no(mensaje, por_defecto=False):
    opciones = " [s/n]: "
    while True:
        texto = _leer_texto(mensaje + opciones)
        if texto is None:
            return por_defecto
        respuesta = texto.strip().lower()
        if not respuesta:
            return por_defecto
        if respuesta in {"s", "si", "y", "yes"}:
            return True
        if respuesta in {"n", "no"}:
            return False
        print("Respuesta no valida. Escribe s para si o n para no.")


def _menu_factorial():
    while True:
        _mostrar_menu(
            [
                "Factorial",
                "1. Iterativo",
                "2. Recursivo",
                "0. Volver",
            ]
        )
        opcion = _leer_texto("Elige una opcion [0-2]: ")
        if opcion is None:
            print("\nEntrada finalizada. Regresando al menu principal.")
            return
        opcion = opcion.strip()

        if opcion == "0":
            return
        if opcion not in {"1", "2"}:
            print(
                "Esa opcion no existe. Debes elegir 1 para iterativo, 2 para recursivo o 0 para volver."
            )
            continue

        metodo = "iterativo" if opcion == "1" else "recursivo"
        n = _leer_entero("Ingresa n: ")
        if n is None:
            print("Entrada finalizada. Regresando al menu anterior.")
            return
        try:
            resultado = calcular_factorial(n, metodo)
            print(f"Listo. El valor de {n}! usando metodo {metodo} es {resultado}.")
            print("Este calculo respeta la definicion matematica de factorial.")
        except Exception as error:
            print(f"No fue posible calcular el factorial: {error}")
        _pausa()


def _menu_permutaciones():
    while True:
        _mostrar_menu(
            [
                "=== Permutaciones ===",
                "1. Calcular factorial",
                "2. Calcular P(n, r)",
                "3. Comparar ejemplos",
                "0. Volver",
            ]
        )
        opcion = _leer_texto("Elige una opcion: ")
        if opcion is None:
            print("\nEntrada finalizada. Regresando al menu principal.")
            return
        opcion = opcion.strip()

        if opcion == "0":
            return
        if opcion == "1":
            _menu_factorial()
            continue
        if opcion == "2":
            n = _leer_entero("Ingresa n: ")
            if n is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            r = _leer_entero("Ingresa r: ")
            if r is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            mostrar = _leer_si_no("Deseas ver el procedimiento?", True)
            try:
                resultado = permutaciones(n, r, mostrar_procedimiento=mostrar)
                print(f"Resultado final: P({n}, {r}) = {resultado}.")
                print("Interpretacion: se cuentan las formas de ordenar r objetos distintos tomados de n.")
            except Exception as error:
                print(f"No fue posible calcular la permutacion: {error}")
            _pausa()
            continue
        if opcion == "3":
            print("Vamos a comparar dos casos de referencia del documento:")
            print(f"P(10, 3) = {permutaciones(10, 3)}")
            print(f"P(20, 5) = {permutaciones(20, 5)}")
            print("Ambos ejemplos muestran que el programa trabaja con valores generales, no con un caso fijo.")
            _pausa()
            continue
        print("Esa opcion no existe. El menu solo acepta 0, 1, 2 o 3.")


def _menu_combinaciones():
    while True:
        _mostrar_menu(
            [
                "=== Combinaciones ===",
                "1. Calcular C(n, r)",
                "2. Verificar simetria",
                "3. Generar fila de Pascal",
                "4. Generar triangulo de Pascal",
                "0. Volver",
            ]
        )
        opcion = _leer_texto("Elige una opcion: ")
        if opcion is None:
            print("\nEntrada finalizada. Regresando al menu principal.")
            return
        opcion = opcion.strip()

        if opcion == "0":
            return
        if opcion == "1":
            n = _leer_entero("Ingresa n: ")
            if n is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            r = _leer_entero("Ingresa r: ")
            if r is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            mostrar = _leer_si_no("Deseas ver el procedimiento?", True)
            try:
                resultado = combinaciones(n, r, mostrar_procedimiento=mostrar)
                print(f"Resultado final: C({n}, {r}) = {resultado}.")
                print("Interpretacion: se cuentan subconjuntos de tamano r sin importar el orden.")
            except Exception as error:
                print(f"No fue posible calcular la combinacion: {error}")
            _pausa()
            continue
        if opcion == "2":
            n = _leer_entero("Ingresa n: ")
            if n is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            r = _leer_entero("Ingresa r: ")
            if r is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                if verificar_simetria(n, r):
                    print(
                        f"La simetria se cumple: C({n}, {r}) es igual a C({n}, {n-r}), como predice la teoria."
                    )
                else:
                    print(
                        f"Algo no coincide: C({n}, {r}) no resulta igual a C({n}, {n-r}). Revisa la entrada."
                    )
            except Exception as error:
                print(f"No fue posible verificar la simetria: {error}")
            _pausa()
            continue
        if opcion == "3":
            n = _leer_entero("Ingresa la fila n: ")
            if n is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                fila = fila_pascal(n)
                print(f"Fila {n} de Pascal: {fila}")
                print("Cada fila resume los coeficientes binomiales de una potencia binomial.")
            except Exception as error:
                print(f"No fue posible generar la fila de Pascal: {error}")
            _pausa()
            continue
        if opcion == "4":
            n = _leer_entero("Generar hasta la fila: ")
            if n is None:
                print("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                mostrar_triangulo_pascal(n)
                print("El triangulo se imprime centrado para resaltar su forma clasica.")
            except Exception as error:
                print(f"No fue posible generar el triangulo de Pascal: {error}")
            _pausa()
            continue
        print("Esa opcion no existe. El menu solo acepta 0, 1, 2, 3 o 4.")


def main():
    while True:
        _mostrar_menu(
            [
                "=== Bono de Matematicas Discretas ===",
                "1. Permutaciones",
                "2. Combinaciones",
                "0. Salir",
            ]
        )
        opcion = _leer_texto("Elige una opcion: ")
        if opcion is None:
            print("\nEntrada finalizada. Saliendo del programa.")
            return
        opcion = opcion.strip()

        if opcion == "0":
            print("Fin del programa. Gracias por usar la calculadora.")
            return
        if opcion == "1":
            _menu_permutaciones()
            continue
        if opcion == "2":
            _menu_combinaciones()
            continue
        print("Esa opcion no existe. Elige 0, 1 o 2.")


if __name__ == "__main__":
    main()
