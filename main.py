"""Menu interactivo principal para permutaciones y combinaciones."""

from time import sleep

from Combinaciones import (
    combinaciones,
    demostrar_identidad_simetria,
    fila_pascal,
    mostrar_pruebas_combinaciones,
    mostrar_triangulo_pascal,
    verificar_simetria,
)
from Permutaciones import (
    calcular_factorial,
    mostrar_comparacion_factoriales,
    mostrar_proceso_factorial_iterativo,
    mostrar_proceso_factorial_recursivo,
    mostrar_pruebas_permutaciones,
    permutaciones,
)


def _escribir(texto, salto=True, demora=0.002):
    for caracter in str(texto):
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
            _escribir("La entrada no es valida. Debes escribir un numero entero.")


def _leer_si_no(mensaje, por_defecto=False):
    while True:
        texto = _leer_texto(f"{mensaje} [s/n]: ")
        if texto is None:
            return por_defecto
        respuesta = texto.strip().lower()
        if not respuesta:
            return por_defecto
        if respuesta in {"s", "si", "y", "yes"}:
            return True
        if respuesta in {"n", "no"}:
            return False
        _escribir("Respuesta no valida. Escribe s para si o n para no.")


def _mostrar_pruebas_generales():
    _escribir("=== Pruebas y casos especiales ===")
    _escribir("Permutaciones:")
    mostrar_pruebas_permutaciones()
    _escribir("Combinaciones:")
    mostrar_pruebas_combinaciones()
    _pausa()


def _menu_factorial():
    while True:
        _mostrar_menu(
            [
                "Factorial",
                "1. Iterativo",
                "2. Recursivo",
                "3. Comparar ambos procesos",
                "0. Volver",
            ]
        )
        opcion = _leer_texto("Elige una opcion [0-3]: ")
        if opcion is None:
            _escribir("Entrada finalizada. Regresando al menu principal.")
            return
        opcion = opcion.strip()

        if opcion == "0":
            return
        if opcion not in {"1", "2", "3"}:
            _escribir(
                "Esa opcion no existe. Debes elegir 1 para iterativo, 2 para recursivo, 3 para comparar procesos o 0 para volver."
            )
            continue

        if opcion in {"1", "2"}:
            metodo = "iterativo" if opcion == "1" else "recursivo"
            n = _leer_entero("Ingresa n: ")
            if n is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            mostrar_proceso = _leer_si_no("Deseas ver el proceso paso a paso?", True)
            try:
                if mostrar_proceso and metodo == "iterativo":
                    resultado = mostrar_proceso_factorial_iterativo(n)
                elif mostrar_proceso and metodo == "recursivo":
                    resultado = mostrar_proceso_factorial_recursivo(n)
                else:
                    resultado = calcular_factorial(n, metodo)
                    _escribir(f"Listo. El valor de {n}! usando metodo {metodo} es {resultado}.")
                if not mostrar_proceso:
                    _escribir("Este calculo respeta la definicion matematica de factorial.")
            except Exception as error:
                _escribir(f"No fue posible calcular el factorial: {error}")
            _pausa()
            continue

        n = _leer_entero("Ingresa n para comparar ambos procesos: ")
        if n is None:
            _escribir("Entrada finalizada. Regresando al menu anterior.")
            return
        try:
            mostrar_comparacion_factoriales(n)
        except Exception as error:
            _escribir(f"No fue posible comparar factoriales: {error}")
        _pausa()


def _menu_permutaciones():
    while True:
        _mostrar_menu(
            [
                "=== Permutaciones ===",
                "1. Calcular factorial",
                "2. Calcular P(n, r)",
                "3. Comparar dos casos",
                "4. Comparar factorial iterativo y recursivo",
                "5. Ver pruebas y casos especiales",
                "0. Volver",
            ]
        )
        opcion = _leer_texto("Elige una opcion: ")
        if opcion is None:
            _escribir("Entrada finalizada. Regresando al menu principal.")
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
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            r = _leer_entero("Ingresa r: ")
            if r is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            mostrar = _leer_si_no("Deseas ver el procedimiento?", True)
            try:
                resultado = permutaciones(n, r, mostrar_procedimiento=mostrar)
                _escribir(f"Resultado final: P({n}, {r}) = {resultado}.")
                _escribir("Interpretacion: se cuentan las formas de ordenar r objetos distintos tomados de n.")
            except Exception as error:
                _escribir(f"No fue posible calcular la permutacion: {error}")
            _pausa()
            continue
        if opcion == "3":
            _escribir("Vamos a comparar dos casos de permutaciones.")
            n1 = _leer_entero("Ingresa el primer n: ")
            if n1 is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            r1 = _leer_entero("Ingresa el primer r: ")
            if r1 is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            n2 = _leer_entero("Ingresa el segundo n: ")
            if n2 is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            r2 = _leer_entero("Ingresa el segundo r: ")
            if r2 is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                resultado1 = permutaciones(n1, r1)
                resultado2 = permutaciones(n2, r2)
                _escribir(f"Primer caso: P({n1}, {r1}) = {resultado1}")
                _escribir(f"Segundo caso: P({n2}, {r2}) = {resultado2}")
                if resultado1 > resultado2:
                    _escribir("El primer caso produce mas permutaciones.")
                elif resultado1 < resultado2:
                    _escribir("El segundo caso produce mas permutaciones.")
                else:
                    _escribir("Ambos casos producen la misma cantidad de permutaciones.")
            except Exception as error:
                _escribir(f"No fue posible comparar los casos: {error}")
            _pausa()
            continue
        if opcion == "4":
            n = _leer_entero("Ingresa n para comparar factoriales: ")
            if n is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                mostrar_comparacion_factoriales(n)
            except Exception as error:
                _escribir(f"No fue posible comparar factoriales: {error}")
            _pausa()
            continue
        if opcion == "5":
            _escribir("Mostrando pruebas y casos especiales de permutaciones...")
            mostrar_pruebas_permutaciones()
            _pausa()
            continue
        _escribir("Esa opcion no existe. El menu solo acepta 0, 1, 2, 3, 4 o 5.")


def _menu_combinaciones():
    while True:
        _mostrar_menu(
            [
                "=== Combinaciones ===",
                "1. Calcular C(n, r)",
                "2. Verificar simetria",
                "3. Generar fila de Pascal",
                "4. Generar triangulo de Pascal",
                "5. Ver pruebas y casos especiales",
                "0. Volver",
            ]
        )
        opcion = _leer_texto("Elige una opcion: ")
        if opcion is None:
            _escribir("Entrada finalizada. Regresando al menu principal.")
            return
        opcion = opcion.strip()

        if opcion == "0":
            return
        if opcion == "1":
            n = _leer_entero("Ingresa n: ")
            if n is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            r = _leer_entero("Ingresa r: ")
            if r is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            mostrar = _leer_si_no("Deseas ver el procedimiento?", True)
            try:
                resultado = combinaciones(n, r, mostrar_procedimiento=mostrar)
                _escribir(f"Resultado final: C({n}, {r}) = {resultado}.")
                _escribir("Interpretacion: se cuentan subconjuntos de tamano r sin importar el orden.")
                demostrar = _leer_si_no("Deseas la demostracion detallada de la identidad C(n, r) = C(n, n-r)?", False)
                if demostrar:
                    demostrar_identidad_simetria(n, r)
            except Exception as error:
                _escribir(f"No fue posible calcular la combinacion: {error}")
            _pausa()
            continue
        if opcion == "2":
            n = _leer_entero("Ingresa n: ")
            if n is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            r = _leer_entero("Ingresa r: ")
            if r is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                if verificar_simetria(n, r):
                    _escribir(
                        f"La simetria se cumple: C({n}, {r}) es igual a C({n}, {n-r}), como predice la teoria."
                    )
                else:
                    _escribir(
                        f"Algo no coincide: C({n}, {r}) no resulta igual a C({n}, {n-r}). Revisa la entrada."
                    )
            except Exception as error:
                _escribir(f"No fue posible verificar la simetria: {error}")
            _pausa()
            continue
        if opcion == "3":
            n = _leer_entero("Ingresa la fila n: ")
            if n is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                fila = fila_pascal(n)
                _escribir(f"Fila {n} de Pascal: {fila}")
                _escribir("Cada fila resume los coeficientes binomiales de una potencia binomial.")
            except Exception as error:
                _escribir(f"No fue posible generar la fila de Pascal: {error}")
            _pausa()
            continue
        if opcion == "4":
            n = _leer_entero("Generar hasta la fila: ")
            if n is None:
                _escribir("Entrada finalizada. Regresando al menu anterior.")
                return
            try:
                mostrar_triangulo_pascal(n)
                _escribir("El triangulo se imprime centrado para resaltar su forma clasica.")
            except Exception as error:
                _escribir(f"No fue posible generar el triangulo de Pascal: {error}")
            _pausa()
            continue
        if opcion == "5":
            _escribir("Mostrando pruebas y casos especiales de combinaciones...")
            mostrar_pruebas_combinaciones()
            _pausa()
            continue
        _escribir("Esa opcion no existe. El menu solo acepta 0, 1, 2, 3, 4 o 5.")


def main():
    while True:
        _mostrar_menu(
            [
                "=== Bono de Matematicas Discretas ===",
                "1. Permutaciones",
                "2. Combinaciones",
                "3. Pruebas y casos especiales",
                "0. Salir",
            ]
        )
        opcion = _leer_texto("Elige una opcion: ")
        if opcion is None:
            _escribir("Entrada finalizada. Saliendo del programa.")
            return
        opcion = opcion.strip()

        if opcion == "0":
            _escribir("Fin del programa. Gracias por usar la calculadora.")
            return
        if opcion == "1":
            _menu_permutaciones()
            continue
        if opcion == "2":
            _menu_combinaciones()
            continue
        if opcion == "3":
            _mostrar_pruebas_generales()
            continue
        _escribir("Esa opcion no existe. Elige 0, 1, 2 o 3.")


if __name__ == "__main__":
    main()
