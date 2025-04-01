# criar um arquivo csv com os dados de dados de vendas

import pandas as pd

# Criar um DataFrame com dados de vendas

data = {
    'produto': ['Produto A', 'Produto B', 'Produto C'],
    'quantidade': [10, 20, 15],
    'preco': [100, 150, 200]
}

df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_vendas.csv', index=False)

print("Arquivo CSV salvo com sucesso!")
