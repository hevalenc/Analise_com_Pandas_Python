#Importando as bibliotecas
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("seaborn")

#Criando nosso DataFrame
df = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/AdventureWorks.xlsx")

#Visualizando as 5 primeiras linhas
print("Visualizando as 5 primeiras linhas\n", df.head())

#Quantidade de linhas e colunas
print("\nTotal de linhas e colunas: ", df.shape)

print("\nTipo dos dados de cada coluna:\n", df.dtypes)

#Qual a Receita total?
print("\nRetornar o valor total do campo 'Valor Venda': ", df["Valor Venda"].sum())
print("")

#Qual o custo Total?
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo
print(df.head(1))

#Qual o custo Total?
print("\nRetornar o valor total da coluna 'Custo' com duas casas decimais: ", round(df["Custo"].sum(), 2))
print("")

#Agora que temos a receita e custo e o total, podemos achar o Lucro total
#Vamos criar uma coluna de Lucro que será Receita - Custo
df["Lucro"] = df["Valor Venda"] - df["Custo"]
print(df.head(1))

#Total Lucro
print("\nRetornar o valor total do campo 'Lucro': ", round(df["Lucro"].sum(), 2))
print("")

#Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
print(df.head(1))
print("")

#Agora, queremos saber a média do tempo de envio para cada Marca e para isso precisamos transformar a coluna Tempo_envio em númerica
#Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print(df.head(1))

#Verificando o tipo da coluna Tempo_envio
print("\nRetornar o tipo da coluna 'Tempo_envio': ", df["Tempo_envio"].dtype)

#Média do tempo de envio por Marca
print("\nMédia do tempo de envio por Marca:\n", df.groupby("Marca")["Tempo_envio"].mean())

#Missing Values
#Verificando se temos dados faltantes
print("\nVerificando se temos dados faltantes:\n", df.isnull().sum())

#E se a gente quiser saber o Lucro por Ano e Por Marca?
#Vamos Agrupar por ano e marca
print("\nLucro por Ano e Por Marca:\n", df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum())

#Formatando o valor
pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
print("\nLucro por Ano e Por Marca, formatado:\n", lucro_ano)

#Qual o total de produtos vendidos?
print("\nQual o total de produtos vendidos?\n", df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

"""
#Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");
"""

print("\nTotal do lucro por ano:\n", df.groupby(df["Data Venda"].dt.year)["Lucro"].sum())

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
print("\nTotal das vendas do ano de 2009: ", df_2009.head())

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

print("\nDados estatíticos:\n", df["Tempo_envio"].describe())

#Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);

#Histograma
plt.hist(df["Tempo_envio"]);

#Tempo mínimo de envio
print("\nTempo mínimo de envio: ", df["Tempo_envio"].min())

#Tempo máximo de envio
print("\nTempo máximo de envio: ", df['Tempo_envio'].max())

#Identificando o Outlier
print("\nIdentificando o Outlier:\n", df[df["Tempo_envio"] == 20])

df.to_csv("df_vendas_novo.csv", index=False)
