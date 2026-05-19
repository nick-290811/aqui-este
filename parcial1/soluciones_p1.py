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



#Ejercicio 3. Escribir una función f3(x0, y0) que recibe dos números y retorna dos funciones recta(x) y paralela(x).
# La función recta(x) representa la recta que pasa por (x0, y0) y tiene pendiente 2.
#  La función paralela(x) representala recta de pendiente 2 que pasa por (1, 1).


def f3(x0, y0):

    def recta(x):
        return 2 * (x - x0) + y0

    def paralela(x):
        return 2 * (x - 1) + 1

    return recta, paralela

# Ejemplo de uso recta, paralela = f3(2, 2)
# recta(3), paralela(3)
# > (4, 5)

#Ejercicio 4. Escribir una función f4(L) que retorna la suma de los elementos en L que son mayores que 10 y la 
# suma de su primer y  ultimo dígito es par.          

def f4(L):
    suma = 0

    for num in L:
        if num > 10:

            texto = str(num)

            primero = int(texto[0])
            ultimo = int(texto[-1])

            if (primero + ultimo) % 2 == 0:
                suma += num

    return suma
#Ejemplo de uso 
# f4([12, 15, 23, 34, 45, 56, 11])
# 15 (1+5=6) + 11 (1+1=2) = 26
# > 26
# 