import pandas as pd
import numpy as np

# Carregando o conjunto de dados
df = pd.read_csv('space.csv', delimiter=';')

# Problema 3: Quantidade de missões realizadas pelos Estados Unidos
missions_by_us = len(df[df['Country of Launch'] == 'USA'])
print(f'3. Quantidade de missões realizadas pelos Estados Unidos: {missions_by_us}')
