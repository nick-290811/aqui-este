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

