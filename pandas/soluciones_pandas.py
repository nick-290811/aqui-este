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

def DecilFinal(estudiante):
    """
    Recibe el nombre de un estudiante y retorna el decil de su nota final.
    """
    # Calcular la nota final como el promedio de los 4 parciales
    notas_finales = df[['parcial1', 'parcial2', 'parcial3', 'parcial4']].mean(axis=1)
    
    # Calcular deciles del 1 al 10
    deciles = pd.qcut(notas_finales, q=10, labels=False, duplicates='drop') + 1
    
    if estudiante in deciles.index:
        return deciles[estudiante]
    else:
        return None
