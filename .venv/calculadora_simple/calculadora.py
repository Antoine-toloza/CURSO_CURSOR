"""
Calculadora simple: suma, resta, multiplicación y división.
El programa se repite hasta que el usuario escriba "salir".
"""


def suma(a: float, b: float) -> float:
    return a + b


def resta(a: float, b: float) -> float:
    return a - b


def multiplicacion(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float | None:
    """Devuelve None si b es cero (división por cero)."""
    if b == 0:
        return None
    return a / b


# Diccionario de operaciones: nombre -> función
OPERACIONES = {
    "suma": suma,
    "resta": resta,
    "multiplicación": multiplicacion,
    "multiplicacion": multiplicacion,  # alias sin tilde
    "división": division,
    "division": division,  # alias sin tilde
}


def pedir_numero(mensaje: str) -> float | None:
    """Pide un número al usuario. Devuelve None si no es válido."""
    try:
        return float(input(mensaje).strip().replace(",", "."))
    except ValueError:
        return None


def main() -> None:
    print("Calculadora. Operaciones: suma, resta, multiplicación, división.")
    print('Escribe "salir" como operación para terminar.\n')

    while True:
        # 1. Pedir operación
        op = input("Operación: ").strip().lower()
        if op == "salir":
            print("Hasta luego.")
            break

        if op not in OPERACIONES:
            print(f'Operación no válida. Usa: suma, resta, multiplicación, división.\n')
            continue

        # 2. Pedir números
        a = pedir_numero("Primer número: ")
        if a is None:
            print("Debes escribir un número válido.\n")
            continue

        b = pedir_numero("Segundo número: ")
        if b is None:
            print("Debes escribir un número válido.\n")
            continue

        # 3. Ejecutar y mostrar resultado
        fn = OPERACIONES[op]
        resultado = fn(a, b)

        if resultado is None:
            # Solo división puede devolver None (división por cero)
            print("Error: no se puede dividir por cero.\n")
            continue

        print(f"Resultado: {resultado}\n")


if __name__ == "__main__":
    main()
