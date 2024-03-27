import pandas as pd

# Carregar dados de um arquivo CSV
dados = pd.read_csv('Titanic-Dataset.csv')

# Exibir as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(dados.head())

# Exibir informações sobre o DataFrame
print("\nInformações sobre o DataFrame:")
print(dados.info())

# Exibir estatísticas descritivas dos dados numéricos
print("\nEstatísticas descritivas:")
print(dados.describe())

# Selecionar uma coluna específica
print("\nValores da coluna 'idade':")
print(dados['idade'])

# Filtrar dados com base em uma condição
print("\nPessoas com idade superior a 30 anos:")
print(dados[dados['idade'] > 30])

# Agrupar e calcular estatísticas agregadas
print("\nMédia de idade por sexo:")
print(dados.groupby('sexo')['idade'].mean())
