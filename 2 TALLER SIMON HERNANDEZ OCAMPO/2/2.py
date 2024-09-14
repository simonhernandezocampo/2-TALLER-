# Definir las variables
a = 7
b = 3

# Realizar las comparaciones
resultado_a_diferente_b = a != b
resultado_a_igual_b = a == b
resultado_a_mayor_b = a > b
resultado_a_sumar_b_menor_2 = (a + b) < 2
resultado_a_mayor_7_y_b_igual_3 = (a > 7) and (b == 3)
resultado_a_menor_7_o_b_igual_3 = (a < 7) or (b == 3)
resultado_a_menor_7_o_b_diferente_3 = (a < 7) or (b != 3)

# Imprimir los resultados
print(f"a != b: {resultado_a_diferente_b}")
print(f"a == b: {resultado_a_igual_b}")
print(f"a > b: {resultado_a_mayor_b}")
print(f"(a + b) < 2: {resultado_a_sumar_b_menor_2}")
print(f"(a > 7) and (b == 3): {resultado_a_mayor_7_y_b_igual_3}")
print(f"(a < 7) or (b == 3): {resultado_a_menor_7_o_b_igual_3}")
print(f"(a < 7) or (b != 3): {resultado_a_menor_7_o_b_diferente_3}")
