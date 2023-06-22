def f(x):
    # Función original
    return x**3 - 2*x**2 + x - 1

def df(x):
    # Derivada de la función original
    return 3*x**2 - 4*x + 1

def ddf(x):
    # Segunda derivada de la función original
    return 6*x - 4

x0 = 1  # Valor inicial
precision = 0.0001  # Precisión deseada
max_iter = 100  # Número máximo de iteraciones

# Llamar a la función del método de raíces múltiples
raiz = metodo_raices_multiples(f, df, ddf, x0, precision, max_iter)
print("La raíz encontrada es:", raiz)
