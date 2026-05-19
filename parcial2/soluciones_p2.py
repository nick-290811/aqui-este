def f2(func):
    error_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal error_count
        if error_count >= 3:
            print("> Leer la documentacion")
            return None
        
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_count += 1
            print(f"> Ha cometido {error_count} error(es): {type(e).__name__}")
            return None
            
    return wrapper

def f3i(n):
    n = abs(n)
    while n >= 10:
        n //= 10
    return n

def f3r(n):
    n = abs(n)
    if n < 10:
        return n
    return f3r(n // 10)


#Ejercicio 1 Los tres primeros números de la sucesión TresFibonacci son 1, 1, 1 y cada término siguientees la suma de los tres anteriores.
#Por ejemplo,los primeros ocho n´umeros de la sucesi´on son:
#1, 1, 1, 3, 5, 9, 17, 31, . . .
#1. Escriba en python un generador llamado G1() que genere todos los números de TresFibonacci.
#2. Escriba en Python un generador llamado tresfibonacci(n) que produzca (uno por uno) los primeros n números de la sucesión TresFibonacci.

# 1. Generador infinito de TresFibonacci
def G1():

    a, b, c = 1, 1, 1

    while True:
        yield a
        a, b, c = b, c, a + b + c


# 2. Generador de los primeros n números
def tresfibonacci(n):

    a, b, c = 1, 1, 1

    for i in range(n):

        yield a

        a, b, c = b, c, a + b + c


# Prueba
# Ge, Ge1 = G1(), tresfibonacci(5)
# for i in range(6):
# print(next(Ge), end=' ')

# Salida:
# 1 1 1 3 5 9
# print()

#Prueba
# for i in Ge1:
# print(i, end=' ')

# Salida:
# 1 1 1 3 5

#Ejercicio 3 Escribir un función iterativa f3i(n) y una función recursiva f3r(n) que recibe un número
#natural diferente de 0 y retorna él  ultimo dígito del núumero. Nota: No se puede usar str :(

# Ejercicio 3

# Función iterativa
def f3i(n):

    while n >= 10:
        n = n // 10

    return n


# Función recursiva
def f3r(n):

    if n < 10:
        return n

    return f3r(n // 10)


# Prueba
# L = [4, 23, 189]
# for i in L:
# print(f3i(i), end=' ')

# Salida:
# 4 2 1

