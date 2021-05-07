#Importando a biblioteca
import pandas as pd
import matplotlib.pyplot as plt

#Leitura dos arquivos
df1 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Aracaju.xlsx")
df2 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Natal.xlsx")
df4 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Recife.xlsx")
df5 = pd.read_excel("E:/EngSoft/Cursos/Digital Innovation One/Dio Labs/Python/analise_dados_pandas/datasets/Salvador.xlsx")

print("Visualizando as 5 primeiras linhas da planilha Salvador:\n", df5.head())

#preparando os arquivos
df = pd.concat([df1, df2, df3, df4, df5])
df["LojaID"] = df["LojaID"].astype("object")
df["Receita"] = df["Vendas"].mul(df["Qtde"])
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
df["Data"] = pd.to_datetime(df["Data"])
df["Ano_Venda"] = df["Data"].dt.year
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
df["diferenca_dias"] = df["Data"] - df["Data"].min()
df["trimestre_venda"] = df["Data"].dt.quarter

#Visualização de dados
print("\nVisualizando o total de dados por 'LojaID':\n", df["LojaID"].value_counts(ascending=False))

#Gráfico de barras
df["LojaID"].value_counts(ascending=False).plot.bar()

#Gráfico de barras horizontais
df["LojaID"].value_counts().plot.barh()

#Gráfico de barras horizontais
df["LojaID"].value_counts(ascending=True).plot.barh()

#Gráfico de Pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

#Total vendas por cidade
print("\nTotal vendas por cidade\n", df["Cidade"].value_counts())

#Adicionando um título e alterando o nome dos eixos
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

#Alterando a cor
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

#Alterando o estilo
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()

print("")
print(df.groupby(df["mes_venda"])["Qtde"].sum())

#Selecionando apenas as vendas de 2019
df_2019 = df[df["Ano_Venda"] == 2019]

print("")
print(df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum())

#Total produtos vendidos por mês
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()

#Hisograma
plt.hist(df["Qtde"], color="orangered");

plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

#Salvando em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.savefig("grafico QTDE x MES.png")