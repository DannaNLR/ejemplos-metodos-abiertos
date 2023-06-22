def metodo_punto_fijo(g, x0, precision, max_iter):
    # Implementación del método de punto fijo
    iteracion = 0
    x = x0
    while abs(x - g(x)) > precision and iteracion < max_iter:
        x = g(x)
        iteracion += 1
    return x

def g(x):
    # Función auxiliar
    return x**2 + 3

x0 = 1  # Valor inicial
precision = 0.0001  # Precisión deseada
max_iter = 100  # Número máximo de iteraciones

# Llamar a la función del método de punto fijo
punto_fijo = metodo_punto_fijo(g, x0, precision, max_iter)
print("El punto fijo encontrado es:", punto_fijo)