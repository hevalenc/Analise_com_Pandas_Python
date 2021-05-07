#Importando a biblioteca
import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Aracaju.xlsx")
df2 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Natal.xlsx")
df4 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Recife.xlsx")
df5 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Salvador.xlsx")

print("Visualizando as 5 primeiras linhas da planilha Salvador:\n", df5.head())

#juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

#Exibindo as 5 primeiras linhas
print("\nVisualizando as 5 primeiras linhas\n", df.head())

#Exibindo as 5 últimas linhas
print("\nVisualizando as 5 últimas linhas\n", df.head())

print("\nVisualizando as 5 amostras da tabela\n", df.sample(5))

#Verificando o tipo de dado de cada coluna
print("\nTipo dos dados de cada coluna:\n", df.dtypes)

#Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")
print("\nTipo dos dados de cada coluna:\n", df.dtypes)
print("\nVisualizando as 5 primeiras linhas\n", df.head())

#Tratando valores faltantes
#Consultando linhas com valores faltantes
print("\nConsultando linhas com valores faltantes:\n", df.isnull().sum())

#Substituindo os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

print("\nRetornar o valor médio das vendas: ", df["Vendas"].mean())

print("\nVisualizando as 15 amostras da tabela\n", df.sample(15))

#Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

#Apagando as linhas com valores nulos
df.dropna(inplace=True)

#Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

#Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

#Criando colunas novas
#Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])
print("\nRetornando a taela com a nova coluna:\n", df.head())

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
print("\nRetornando a taela com a nova coluna:\n", df.head())

#Retornando a maior receita
print("\nRetornando a maior receita: ", df["Receita"].max())

#Retornando a menor receita
print("\nRetornando a menor receita: ", df["Receita"].min())

#nlargest
print("\nRetornando o maior valor na coluna Receita:\n", df.nlargest(3, "Receita"))

#nsamllest
print("\nRetornando o menor valor na coluna Receita:\n", df.nsmallest(3, "Receita"))

#Agrupamento por cidade
print("\nValor da receita por cidade:\n", df.groupby("Cidade")["Receita"].sum())

#Ordenando o conjunto de dados
print("\nOrdenando o conjunto de dados:\n", df.sort_values("Receita", ascending=False).head(10))

#Trabalhando com datas
#Trasnformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

#Verificando o tipo de dado de cada coluna
print("\nTipo dos dados de cada coluna:\n", df.dtypes)

#Transformando coluna data de int para data
df["Data"] = pd.to_datetime(df["Data"])
print("\nTipo dos dados de cada coluna após a conversão do tipo da coluna 'Data':\n", df.dtypes)

#Agrupamento por ano
print("\nValor da receita por ano:\n", df.groupby(df["Data"].dt.year)["Receita"].sum())

#Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year
print("\nVisualizando as 5 amostras da tabela com a nova coluna:\n", df.sample(5))

#Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
print("\nVisualizando as 5 amostras da tabela com a nova coluna:\n", df.sample(5))

#Retornando a data mais antiga
print("\nRetornando a data mais antiga: ", df["Data"].min())

#Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
print("\nVisualizando as 5 amostras da tabela com a nova coluna:\n", df.sample(5))

#Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter
print("\nVisualizando as 5 amostras da tabela com a nova coluna:\n", df.sample(5))

#Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print("\nFiltrando as vendas de 2019 do mês de março:\n", vendas_marco_19.sample(20))
