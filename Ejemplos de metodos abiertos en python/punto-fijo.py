def g(x):
    # Función auxiliar
    return x**2 + 3

x0 = 1  # Valor inicial
precision = 0.0001  # Precisión deseada
max_iter = 100  # Número máximo de iteraciones

# Llamar a la función del método de punto fijo
punto_fijo = metodo_punto_fijo(g, x0, precision, max_iter)
print("El punto fijo encontrado es:", punto_fijo)
