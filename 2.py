import numpy as np

# Carregando o conjunto de dados
arr = np.loadtxt('space.csv', delimiter=';', dtype=str)

# Problema 2: Média de gastos em missões espaciais com valores disponíveis (>0)
# Certifique-se de converter os valores de 'Rocket' em números antes de calcular a média
rocket_costs = arr[:, -1]  # Última coluna que contém os custos
rocket_costs = np.where(rocket_costs == 'nan', '0', rocket_costs)  # Substitua 'nan' por '0'
rocket_costs = rocket_costs.astype(float)  # Converte para float
media_gastos = np.mean(rocket_costs[rocket_costs > 0])
print(f'2. Média de gastos em missões espaciais: ${media_gastos:.2f}')
