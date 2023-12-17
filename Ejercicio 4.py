# Lista para almacenar los datos de los alumnos
lista_alumnos = []

while True:
    # Solicitar el nombre del alumno
    nombre_alumno = input("Ingrese el nombre del alumno (o escriba 'fin' para terminar): ")

    # Verificar si el usuario desea terminar el ingreso de datos
    if nombre_alumno.lower() == 'fin':
        break

    try:
        # Solicitar las calificaciones del alumno
        calificaciones = [float(input(f"Ingrese la calificación {i + 1} del alumno {nombre_alumno}: ")) for i in range(3)]

        # Agregar los datos del alumno a la lista
        alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}
        lista_alumnos.append(alumno)

    except ValueError:
        print("Por favor, ingrese calificaciones válidas.")

# Mostrar el listado completo de alumnos
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(f"Alumno: {alumno['Alumno']}, Calificaciones: {alumno['Notas']}")