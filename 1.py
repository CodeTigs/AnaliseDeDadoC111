import pandas as pd
import numpy as np

# Carregando o conjunto de dados
df = pd.read_csv('space.csv', delimiter=';')

# Problema 1: Porcentagem de missões bem-sucedidas
total_missoes = len(df)
missoes_bem_sucedidas = len(df[df['Status Rocket'] == 'StatusActive'])
porcentagem_bem_sucedidas = (missoes_bem_sucedidas / total_missoes) * 100
print(f'1. Porcentagem de missões bem-sucedidas: {porcentagem_bem_sucedidas:.2f}%')