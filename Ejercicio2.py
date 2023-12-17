def imprimir_patron(filas):
    # Imprimir la mitad superior del patrón
    for i in range(1, filas + 1):
        print('* ' * i)

    # Imprimir la mitad inferior del patrón
    for i in range(filas - 1, 0, -1):
        print('* ' * i)

# Número de filas del patrón
filas = 5

# Llamar a la función para imprimir el patrón
imprimir_patron(filas)