def omitir_vocales(cadena):
    resultado = ""
    for caracter in cadena:
        # Verificar si el caracter es una vocal (mayúscula o minúscula)
        if caracter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += caracter
    return resultado

# Solicitar al usuario una cadena de texto
entrada_usuario = input("Ingrese una cadena de texto: ")

# Obtener el resultado omitiendo las vocales
resultado = omitir_vocales(entrada_usuario)

# Mostrar el resultado
print(f"Resultado: {resultado}")