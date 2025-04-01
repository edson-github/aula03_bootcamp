import csv
import os

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

def carregar_dados():
    dados = []
    with open('data/dados_vendas.csv', 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append({
                'produto': linha['produto'],
                'quantidade': float(linha['quantidade']),
                'preco': float(linha['preco'])
            })
    return dados

class VerificadorDeDados:
    def __init__(self):
        self.data = carregar_dados()

    def verificar_dados(self):
        for registro in self.data:
            if registro['quantidade'] <= 0 or registro['preco'] <= 0:
                print(f"Dados inválidos para o produto {registro['produto']}")
            else:
                print(f"Dados válidos para o produto {registro['produto']}")

# Exemplo de uso
if __name__ == "__main__":
    verificador = VerificadorDeDados()
    verificador.verificar_dados()







