import sympy as sp  # Importamos la librería sympy para álgebra simbólica

# Función para ingresar una matriz desde el teclado
def ingresar_matriz():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    print(f"Ingrese los {columnas} elementos fila por fila separados por espacios:")

    matriz = []
    for i in range(filas):
        # Se leen los elementos de cada fila como una lista de números flotantes
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        if len(fila) != columnas:
            print("Error: número incorrecto de elementos.")
            return None
        matriz.append(fila)

    return sp.Matrix(matriz)  # Se devuelve como una matriz de SymPy

# Función para obtener la forma escalonada por filas (eliminación de Gauss)
def forma_escalonada_por_gauss(A):
    print("\nForma escalonada por filas (Gauss):")
    E = A.echelon_form()  # Obtiene la forma escalonada
    sp.pprint(E)  # Imprime la matriz de forma bonita

# Función para obtener la forma escalonada reducida por filas (Gauss-Jordan)
def forma_escalonada_reducida(A):
    print("\nForma escalonada reducida (Gauss-Jordan):")
    RREF, _ = A.rref()  # rref() devuelve la forma escalonada reducida
    sp.pprint(RREF)

# Función para aplicar una operación fila mediante una matriz elemental
def aplicar_matriz_elemental(A):
    n = A.rows  # Número de filas
    print("\nCreando una matriz elemental...")

    # Opciones para construir la matriz elemental
    print("1. Intercambiar dos filas")
    print("2. Multiplicar una fila por un escalar")
    print("3. Sumar un múltiplo de una fila a otra")

    opcion = input("Seleccione una opción: ")

    E = sp.eye(n)  # Matriz identidad del mismo tamaño que A

    if opcion == "1":
        # Intercambio de filas
        f1 = int(input("Fila 1 a intercambiar (comenzando en 1): ")) - 1
        f2 = int(input("Fila 2 a intercambiar (comenzando en 1): ")) - 1
        E.row_swap(f1, f2)
    elif opcion == "2":
        # Multiplicación de fila por un escalar
        f = int(input("Fila a multiplicar (comenzando en 1): ")) - 1
        k = float(input("Escalar: "))
        E.row_op(f, lambda v, _: k * v)
    elif opcion == "3":
        # Suma de un múltiplo de una fila a otra
        f_dest = int(input("Fila destino (comenzando en 1): ")) - 1
        f_origen = int(input("Fila origen (comenzando en 1): ")) - 1
        k = float(input("Escalar: "))
        # row_op aplica una función sobre cada entrada de la fila destino
        E.row_op(f_dest, lambda v, j: v + k * A[f_origen, j])
    else:
        print("Opción no válida.")
        return

    print("\nMatriz elemental:")
    sp.pprint(E)

    # Se aplica la matriz elemental a la matriz original
    print("\nMatriz resultante E * A:")
    sp.pprint(E * A)

# Función para calcular la inversa de una matriz usando eliminación gaussiana
def calcular_inversa(A):
    if A.rows != A.cols:
        print("La matriz no es cuadrada. No tiene inversa.")
        return

    if A.det() == 0:
        print("La matriz es singular. No tiene inversa.")
        return

    print("\nMatriz aumentada [A | I]:")
    A_aug = A.row_join(sp.eye(A.rows))  # Se concatena A con la identidad
    sp.pprint(A_aug)

    # Se reduce la matriz aumentada a su forma escalonada reducida
    A_inv_aug = A_aug.rref()[0]

    print("\nMatriz reducida [I | A^-1]:")
    sp.pprint(A_inv_aug)

    # Se extrae la parte derecha de la matriz reducida, que es A^-1
    A_inv = A_inv_aug[:, A.cols:]
    print("\nMatriz inversa A^-1:")
    sp.pprint(A_inv)

    # Verificación: A * A^-1 = I
    print("\nVerificación A * A^-1:")
    sp.pprint(A * A_inv)

# ---------------------------
# Menú principal interactivo
# ---------------------------
def menu():
    while True:
        # Opciones que el usuario puede seleccionar
        print("\n==== MENÚ ====")
        print("1. Forma escalonada (Gauss)")
        print("2. Forma escalonada reducida (Gauss-Jordan)")
        print("3. Aplicar matriz elemental")
        print("4. Calcular inversa de una matriz")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        # Se solicita la matriz al usuario
        A = ingresar_matriz()
        if A is None:
            continue

        # Se llama a la función correspondiente según la opción elegida
        if opcion == "1":
            forma_escalonada_por_gauss(A)
        elif opcion == "2":
            forma_escalonada_reducida(A)
        elif opcion == "3":
            aplicar_matriz_elemental(A)
        elif opcion == "4":
            calcular_inversa(A)
        else:
            print("Opción inválida.")

# Punto de entrada principal del programa
if __name__ == "__main__":
    menu()  # Llama al menú principal para comenzar la interacción
