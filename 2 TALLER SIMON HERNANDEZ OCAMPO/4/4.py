# Función para convertir metros a millas
def metros_a_millas(metros):
    metros_por_milla = 1609.34
    millas = metros / metros_por_milla
    return millas

# Solicitar al usuario que ingrese la cantidad de metros
metros = float(input("Introduce la cantidad de metros a convertir: "))

# Realizar la conversión
millas = metros_a_millas(metros)

# Mostrar el resultado
print(f"{metros} metros son aproximadamente {millas} millas.")