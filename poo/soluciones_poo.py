class Polinomio:
    
    def __init__(self, L):
        """
        Inicializa el polinomio con la lista de coeficientes.
        """
        # Limpiar ceros a la derecha para normalizar
        temp_L = list(L)
        while len(temp_L) > 1 and temp_L[-1] == 0:
            temp_L.pop()
        if not temp_L:
            temp_L = [0]
        self.L = temp_L
    
    def __str__(self):
        """
        Retorna una representación legible del polinomio.
        """
        if not self.L or (len(self.L) == 1 and self.L[0] == 0):
            return "0"
            
        terminos = []
        for i, coef in enumerate(self.L):
            if coef == 0:
                continue
                
            termino = ""
            if i == 0:
                termino = str(coef)
            else:
                if coef == -1:
                    termino += "-"
                elif coef != 1:
                    termino += str(coef)
                
                if i == 1:
                    termino += "x"
                else:
                    termino += f"x^{i}"
            
            terminos.append(termino)
            
        # Formatear signos
        resultado = terminos[0]
        for t in terminos[1:]:
            if t.startswith("-"):
                resultado += f" - {t[1:]}"
            else:
                resultado += f" + {t}"
                
        return resultado
    
    def __add__(self, other):
        """
        Retorna la suma de dos polinomios.
        """
        max_len = max(len(self.L), len(other.L))
        L1 = self.L + [0] * (max_len - len(self.L))
        L2 = other.L + [0] * (max_len - len(other.L))
        
        suma = [c1 + c2 for c1, c2 in zip(L1, L2)]
        return Polinomio(suma)
    
    def __sub__(self, other):
        """
        Retorna la resta de dos polinomios.
        """
        max_len = max(len(self.L), len(other.L))
        L1 = self.L + [0] * (max_len - len(self.L))
        L2 = other.L + [0] * (max_len - len(other.L))
        
        resta = [c1 - c2 for c1, c2 in zip(L1, L2)]
        return Polinomio(resta)
    
    def __mul__(self, other):
        """
        Retorna la multiplicación de dos polinomios.
        """
        if (len(self.L) == 1 and self.L[0] == 0) or (len(other.L) == 1 and other.L[0] == 0):
            return Polinomio([0])
            
        resultado = [0] * (len(self.L) + len(other.L) - 1)
        for i, c1 in enumerate(self.L):
            for j, c2 in enumerate(other.L):
                resultado[i + j] += c1 * c2
                
        return Polinomio(resultado)
    
    def evaluar(self, x):
        """
        Evalúa el polinomio en el valor x y lo retorna.
        """
        total = 0
        for i, coef in enumerate(self.L):
            total += coef * (x ** i)
        return total

class PolinomiosDerivables(Polinomio):
    
    def grado(self):
        """
        Retorna el grado del polinomio.
        """
        if len(self.L) == 1 and self.L[0] == 0:
            return 0
        return len(self.L) - 1
        
    def derivada(self):
        """
        Retorna un nuevo PolinomiosDerivables que representa la derivada.
        """
        if self.grado() == 0:
            return PolinomiosDerivables([0])
            
        nueva_L = [self.L[i] * i for i in range(1, len(self.L))]
        return PolinomiosDerivables(nueva_L)
        
    def recta_tangente(self, x_0):
        """
        Retorna la recta tangente en el punto x_0 como un PolinomiosDerivables.
        y - f(x_0) = f'(x_0) * (x - x_0) -> y = f'(x_0)*x + (f(x_0) - f'(x_0)*x_0)
        """
        f_x0 = self.evaluar(x_0)
        deriv = self.derivada()
        fp_x0 = deriv.evaluar(x_0)
        
        m = fp_x0
        b = f_x0 - fp_x0 * x_0
        
        return PolinomiosDerivables([b, m])



# Ejercicio del Cajero

class Cajero():

    def __init__(self, n1, n2, n5):

        # Billetes de 10000, 20000 y 50000
        self.n1 = n1
        self.n2 = n2
        self.n5 = n5


    def retiro(self, x):

        # Verificar múltiplo de 10000
        if x % 10000 != 0:
            return "La cantidad debe ser múltiplo de 10000"

        cantidad = x

        # Cantidad de billetes a entregar
        b5 = min(cantidad // 50000, self.n5)
        cantidad -= b5 * 50000

        b2 = min(cantidad // 20000, self.n2)
        cantidad -= b2 * 20000

        b1 = min(cantidad // 10000, self.n1)
        cantidad -= b1 * 10000

        # Si no pudo entregar exactamente el dinero
        if cantidad != 0:
            return "No es posible realizar el retiro"

        # Actualizar billetes del cajero
        self.n5 -= b5
        self.n2 -= b2
        self.n1 -= b1

        return f"Retiro exitoso: {b5} billetes de 50000, {b2} billetes de 20000 y {b1} billetes de 10000"


    def consignacion(self, n1, n2, n5):

        self.n1 += n1
        self.n2 += n2
        self.n5 += n5

        return "Consignación realizada correctamente"


    def verificar_estado(self):

        return f"""
Billetes de 10000: {self.n1}
Billetes de 20000: {self.n2}
Billetes de 50000: {self.n5}
"""


# Prueba = 
# Cajero(10, 5, 2)
# print(c.verificar_estado())
# print(c.retiro(90000))
# print(c.verificar_estado())
# print(c.consignacion(2, 1, 1))
# print(c.verificar_estado())