def contar_digitos(numero, digito):
    # Convierte el dígito a string para facilitar la comparación
    digito_str = str(digito)

    # Convierte el número a string para iterar sobre cada dígito
    numero_str = str(numero)

    # Inicializa el contador de ocurrencias
    contador_ocurrencias = 0

    # Itera sobre cada dígito en el número y cuenta las ocurrencias
    for d in numero_str:
        if d == digito_str:
            contador_ocurrencias += 1

    return contador_ocurrencias

# Ejemplo de uso de la función
numero_ingresado = int(input("Ingrese un número entero: "))
digito_ingresado = int(input("Ingrese un dígito: "))

ocurrencias = contar_digitos(numero_ingresado, digito_ingresado)

print(f"El dígito {digito_ingresado} aparece {ocurrencias} veces en el número {numero_ingresado}.")