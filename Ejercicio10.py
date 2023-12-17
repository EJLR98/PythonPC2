meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

def obtener_fecha_en_formato_iso(fecha):
    # Dividir la fecha en componentes
    partes_fecha = fecha.split()

    if len(partes_fecha) == 3:
        # Formato: mes día, año
        mes_str, dia_str, anio_str = partes_fecha
    else:
        # Formato: mes/día/año
        dia_str, mes_str, anio_str = fecha.split('/')

    # Obtener el número del mes
    num_mes = meses.index(mes_str) + 1

    # Formatear la fecha en el formato AAAA-MM-DD
    fecha_iso = f"{anio_str}-{num_mes:02d}-{int(dia_str):02d}"

    return fecha_iso

# Solicitar al usuario una fecha
fecha_usuario = input("Ingrese una fecha (en formato mes-día-año o mes día, año): ")

# Obtener la fecha en formato AAAA-MM-DD
fecha_iso = obtener_fecha_en_formato_iso(fecha_usuario)

# Mostrar el resultado
print(f"Fecha en formato AAAA-MM-DD: {fecha_iso}")