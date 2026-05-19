# Una función de nombre f1 recibe una función y dos números enteros a, b. 
# Retorna la sumatoria f(i)*i para los números enteros i entre a y b (inclusive).
def f1(func, a, b):
    total = 0
    for i in range(a, b + 1):
        total += func(i) * i
    return total

# f1(lambda x: x**2, 1, 3)  # Ejemplo de uso: sumatoria de 1^2 * 1 + 2^2 * 2 + 3^2 * 3 para i entre 1 y 3
