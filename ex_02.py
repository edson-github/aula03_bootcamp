### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# - 'Baixa' se a temperatura estiver abaixo de 20 graus
# - 'Normal' se a temperatura estiver entre 20 e 25 graus
# - 'Alta' se a temperatura estiver acima de 25 graus

# criar um arquivo csv com os dados de temperatura

# import pandas as pd

# data = {
#     'temperatura': [15, 22, 28, 18, 24, 30, 20, 26, 22, 28]
# }   

# df = pd.DataFrame(data)

# df.to_csv('data/temperatura.csv', index=False)


# classificar os dados de temperatura

import pandas as pd

df = pd.read_csv('data/temperatura.csv')

for index, row in df.iterrows():
    temperatura = row['temperatura']
    if temperatura < 20:
        print(f"Temperatura {temperatura} graus: Baixa")
    elif temperatura >= 20 and temperatura <= 25:
        print(f"Temperatura {temperatura} graus: Normal")
    else:
        print(f"Temperatura {temperatura} graus: Alta")








