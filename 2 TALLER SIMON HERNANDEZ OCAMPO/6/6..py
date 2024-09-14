# Función para convertir pesos colombianos a dólares
def pesos_a_dolares(pesos, tasa_cambio):
    dolares = pesos / tasa_cambio
    return dolares

# Solicitar al usuario el monto en pesos colombianos
pesos = float(input("Introduce la cantidad de pesos colombianos a convertir: "))

# Definir el tipo de cambio (ejemplo: 1 dólar = 4,000 pesos colombianos)
tasa_cambio = 4000

# Realizar la conversión
dolares = pesos_a_dolares(pesos, tasa_cambio)

# Mostrar el resultado
print(f"{pesos} pesos colombianos son aproximadamente {dolares:.2f} dólares.")