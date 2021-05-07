#importando a biblioteca pandas
import pandas as pd

#Carregando o arquivo CSV e aplicando a formatação para visualização da tabela
df = pd.read_csv("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Gapminder.csv",error_bad_lines=False, sep=";")

#Visualizando as 5 primeiras linhas
print("Visualizando as 5 primeiras linhas\n", df.head())

#Renomear os nomes das colunas
df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})

print("\nVisualizando as 10 primeiras linhas\n", df.head(10))
print("")

#Total de linhas e colunas
print("\nTotal de linhas e colunas: ", df.shape)

print("\nNome das colunas: ", df.columns)

print("\nTipo dos dados de cada coluna:\n", df.dtypes)

print("\nVisualizando as 15 últimas linhas\n", df.tail(15))

print("\nDados estatísticos da planilha:\n", df.describe())

print("\nRetornar dados únicos de uma coluna: ", df["continente"].unique())

Oceania = df.loc[df["continente"] == "Oceania"]
print("\nRetornar os dados conforme o filtro:\n", Oceania.head())
print(Oceania["continente"].unique())

print("\nRetornar a quantidade de registros por cada continente:\n", df.groupby("continente")["Pais"].nunique())
print("\nRetornar a média de expectativa de vida por ano:\n", df.groupby("Ano")["Expectativa de vida"].mean())

print("\nRetornar a média do PIB: ", df["PIB"].mean())
print("\nRetornar a soma do PIB: ", df["PIB"].sum())
