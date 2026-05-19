import pandas as pd
import os

# Obtener la ruta absoluta del directorio actual para cargar el csv correctamente
dir_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(dir_path, 'notas.csv')

# Cargar el DataFrame
df = pd.read_csv(csv_path, index_col=0)

# ==========================================
# SOLUCIONES DE LOS EJERCICIOS DE PANDAS
# ==========================================

#Punto 3 Escribir una función AprobadosPorParcial(umbral=3.0) que recibe un umbral de aprobación (por defecto 3.0) 
# y retorna una Series de pandas cuyo index son los nombres de los parciales (parcial1, parcial2, parcial3, parcial4) 
# y cuyos valores son la cantidad de estudiantes que obtuvieron una nota mayor o igual al umbral en cada parcial.

import pandas as pd
import numpy as np

df = pd.read_csv('notas.csv', index_col=0)


# Punto 3
def AprobadosPorParcial(umbral=3.0):

    # Cuenta cuántas notas son mayores o iguales al umbral
    aprobados = (df >= umbral).sum()

    return aprobados


# Prueba
# print(AprobadosPorParcial())


#Punto 4 scribir una función TendenciaEstudiante(estudiante) que recibe el nombre de un estudiante y retorna el string 'mejora' si sus notas tienen
# tendencia creciente a lo largo de los 4 parciales, 'desmejora' si tienen tendencia decreciente, o 'estable' en cualquier otro caso.
#  Para determinar la tendencia se debe usar la pendiente de la regresión lineal sobre las 4 notas: pendiente positiva → 'mejora', negativa → 'desmejora', cero → 'estable'. 
# La pendiente se puede calcular con numpy.polyfit.

def TendenciaEstudiante(estudiante):

    # Obtener las notas del estudiante
    notas = df.loc[estudiante].values

    # Eje x -> parciales 1,2,3,4
    x = [1, 2, 3, 4]

    # Calcular pendiente de regresión lineal
    pendiente = np.polyfit(x, notas, 1)[0]

    # Determinar tendencia
    if pendiente > 0:
        return 'mejora'

    elif pendiente < 0:
        return 'desmejora'

    else:
        return 'estable'


# Prueba
# print(TendenciaEstudiante('Estudiante0'))
