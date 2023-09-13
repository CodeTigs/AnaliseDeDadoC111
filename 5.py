import pandas as pd
import numpy as np

# Carregando o conjunto de dados
df = pd.read_csv('space.csv', delimiter=';')


# Problema 5: Empresas que realizaram missões espaciais e quantidades de missões
unique_companies = df['Company Name'].unique()
for company in unique_companies:
    missions_count = len(df[df['Company Name'] == company])
    print(f'Empresa: {company}, Missões realizadas: {missions_count}')
