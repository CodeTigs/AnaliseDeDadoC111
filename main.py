import pandas as pd
import numpy as np

# Carregando o conjunto de dados
df = pd.read_csv('space.csv')
df = pd.read_csv('space.csv', delimiter=';')
df = pd.read_csv('space.csv', skiprows=4)
# Problema 1: Porcentagem de missões bem-sucedidas
total_missoes = len(df)
missoes_bem_sucedidas = len(df[df['Status Rocket'] == 'StatusActive'])
porcentagem_bem_sucedidas = (missoes_bem_sucedidas / total_missoes) * 100
print(f'1. Porcentagem de missões bem-sucedidas: {porcentagem_bem_sucedidas:.2f}%')

# Problema 2: Média de gastos em missões espaciais com valores disponíveis (>0)
media_gastos = np.mean(df[df[' Rocket'] > 0][' Rocket'])
print(f'2. Média de gastos em missões espaciais: ${media_gastos:.2f}')

# Problema 3: Quantidade de missões realizadas pelos Estados Unidos
missions_by_us = len(df[df['Country of Launch'] == 'USA'])
print(f'3. Quantidade de missões realizadas pelos Estados Unidos: {missions_by_us}')

# Problema 4: Missão mais cara realizada pela SpaceX
max_cost_spacex = df[df['Company Name'] == 'SpaceX'][' Rocket'].max()
most_expensive_spacex_mission = df[(df['Company Name'] == 'SpaceX') & (df[' Rocket'] == max_cost_spacex)]['Detail'].values[0]
print(f'4. Missão mais cara realizada pela SpaceX: {most_expensive_spacex_mission} (${max_cost_spacex:.2f})')

# Problema 5: Empresas que realizaram missões espaciais e quantidades de missões
unique_companies = df['Company Name'].unique()
for company in unique_companies:
    missions_count = len(df[df['Company Name'] == company])
    print(f'Empresa: {company}, Missões realizadas: {missions_count}')
