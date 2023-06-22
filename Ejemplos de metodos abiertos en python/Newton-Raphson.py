def metodo_newton_raphson(f, df, x0, precision, max_iter):
    # Implementación del método de Newton-Raphson
    iteracion = 0
    x = x0
    while abs(f(x)) > precision and iteracion < max_iter:
        x = x - f(x) / df(x)
        iteracion += 1
    return x

def f(x):
    # Función original
    return x**2 - 4

def df(x):
    # Derivada de la función original
    return 2*x

x0 = 1  # Valor inicial
precision = 0.0001  # Precisión deseada
max_iter = 100  # Número máximo de iteraciones

# Llamar a la función del método de Newton-Raphson
raiz = metodo_newton_raphson(f, df, x0, precision, max_iter)
print("La raíz encontrada es:", raiz)
