# Una función de nombre f1 recibe una función y dos números enteros a, b. 
# Retorna la sumatoria f(i)*i para los números enteros i entre a y b (inclusive).
def f1(func, a, b):
    total = 0
    for i in range(a, b + 1):
        total += func(i) * i
    return total

# f1(lambda x: x**2, 1, 3)  # Ejemplo de uso: sumatoria de 1^2 * 1 + 2^2 * 2 + 3^2 * 3 para i entre 1 y 3

# Una función `f2(L)` recibe una lista de números y retorna una función `f(x)` 
# que representa el polinomio con coeficientes en `L` evaluado en `x`.
def f2(L):
    def f(x):
        total = 0
        for i in range(len(L)):
            total += L[i] * (x ** i)
        return total
    return f

# Ejemplo de uso: si L = [1, 2, 3], entonces f(x) = 1 + 2*x + 3*x^2
# polinomio = f2([1, 2, 3])
# print(polinomio(2))  # Evaluar el polinomio en x=2, debería retornar 1 + 2*2 + 3*2^2 = 1 + 4 + 12 = 17
