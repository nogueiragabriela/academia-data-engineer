import pandas as pd

# Lendo os arquivos .csv
df = pd.read_csv('C:/academia_accenture/exercicios_python/powerbi-python/dados-brutos/SP_poluicao_dados.csv', encoding='utf-8')
df_grupos = pd.read_csv('C:/academia_accenture/exercicios_python/powerbi-python/dados-brutos/SP_estacoes_grupos.csv', encoding='utf-8')

# Criando uma nova coluna para armazenar os dados de data e hora e trabsformando para o tipo datetime
df['Data_hora'] = df['Data'].astype(str) +' '+ df['Hora']
df['Data_hora'] = pd.to_datetime(df['Data_hora'], format='%Y/%m/%d %H:%M:%S')

# Excluindo as colunas que não serão necessárias na análise
df.drop(['Unnamed: 0', 'ID', 'Data', 'Hora', 'Unidade', 'Tipo'], axis=1, inplace=True)

# Filtrando o dataframe para analisar os dados a partir do ano de 2019
df_2019_2021 = df.loc[(df['Data_hora'] >= '2019-01-01')]

# Unindo os dataframes de acordo com as estações para referenciar os grupos de localizações
df_2019_grupos = df_2019_2021.merge(df_grupos, how='inner', on='Estacao')

# Criando uma nova coluna ID para o dataframe filtrado 
df_2019_grupos.insert(0, 'ID', range(0, len(df_2019_grupos)))

print(df_2019_grupos.head(25))



