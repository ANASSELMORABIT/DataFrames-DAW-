import pandas as pd

# Crear un DataFrame de ejemplo
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': ['x', 'y', 'z']}
df = pd.DataFrame(data)

# Establecer la columna 'C' como índice
df_con_indice = df.set_index('C')

print("DataFrame con índice:")
print(df_con_indice)
