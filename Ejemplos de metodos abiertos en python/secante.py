def metodo_secante(f, x0, x1, precision, max_iter):
    # Implementación del método de la secante
    iteracion = 0
    while abs(f(x1)) > precision and iteracion < max_iter:
        x_next = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x_next
        iteracion += 1
    return x1

def f(x):
    # Función original
    return x**2 - 4

x0 = 1  # Primer punto inicial
x1 = 2  # Segundo punto inicial
precision = 0.0001  # Precisión deseada
max_iter = 100  # Número máximo de iteraciones

# Llamar a la función del método de la secante
raiz = metodo_secante(f, x0, x1, precision, max_iter)
print("La raíz encontrada es:", raiz)