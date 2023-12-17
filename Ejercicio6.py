# Inicializar los dos primeros números de la serie de Fibonacci
a, b = 0, 1

# Imprimir el primer número (0)
print(a)

# Generar y imprimir la serie de Fibonacci hasta 50
while b <= 50:
    print(b)
    a, b = b, a + b