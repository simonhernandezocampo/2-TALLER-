# Función para calcular el nuevo salario mínimo
def calcular_nuevo_salario(salario_actual, incremento_porcentaje):
    incremento_decimal = incremento_porcentaje / 100
    incremento = salario_actual * incremento_decimal
    nuevo_salario = salario_actual + incremento
    return nuevo_salario

# Solicitar al usuario el salario mínimo actual
salario_actual = float(input("Introduce el salario mínimo actual: "))

# Definir el porcentaje de incremento
incremento_porcentaje = 4.2

# Calcular el nuevo salario mínimo
nuevo_salario = calcular_nuevo_salario(salario_actual, incremento_porcentaje)

# Mostrar el resultado
print(f"El nuevo salario mínimo para el próximo año será: {nuevo_salario:.2f}")