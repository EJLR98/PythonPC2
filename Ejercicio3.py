numeros_ingresados = []

while True:
    desea_ingresar = input("¿Desea ingresar un número? (SI/NO): ")
    
    if desea_ingresar.upper() != 'SI':
        break
    
    try:
        numero = int(input("Ingrese el número: "))
        numeros_ingresados.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")

pares = sum(1 for num in numeros_ingresados if num % 2 == 0)
impares = len(numeros_ingresados) - pares

print(f"\nNúmeros ingresados: {numeros_ingresados}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")