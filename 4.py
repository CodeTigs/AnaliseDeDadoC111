import pandas as pd
import numpy as np

# Carregando o conjunto de dados
df = pd.read_csv('space.csv', delimiter=';')

# Problema 4: Missão mais cara realizada pela SpaceX
max_cost_spacex = df[df['Company Name'] == 'SpaceX'][' Rocket'].max()
most_expensive_spacex_mission = df[(df['Company Name'] == 'SpaceX') & (df[' Rocket'] == max_cost_spacex)]['Detail'].values[0]
print(f'4. Missão mais cara realizada pela SpaceX: {most_expensive_spacex_mission} (${max_cost_spacex:.2f})')
