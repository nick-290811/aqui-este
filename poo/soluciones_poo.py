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
