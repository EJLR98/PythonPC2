def calcular_factorial(numero):
    # Verificar si el número es negativo
    if numero < 0:
        return "Error: El factorial no está definido para números negativos."
    # Inicializar el factorial a 1
    factorial = 1
    # Calcular el factorial multiplicando cada número desde 1 hasta el número dado
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Ejemplo de uso de la función
numero_ingresado = int(input("Ingrese un número entero no negativo para calcular su factorial: "))

resultado = calcular_factorial(numero_ingresado)

if type(resultado) == int:
    print(f"El factorial de {numero_ingresado} es {resultado}.")
else:
    print(resultado)