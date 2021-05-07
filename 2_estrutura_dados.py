print("\nListas\n")
#Criando uma lista chamada animais
animais = [1,2,3]
print(animais)

animais = ["cachorro", "gato", 12345, 6.5]
print(animais)

#Imprimindo o primeiro elemento da lista
print(animais[0])

#Imprimindo o 4 elemento da lista
print(animais[3])

#Substituindo o primeiro elemento da lista
animais[0] = "papagaio"
print(animais)

#Removendo gato da lista
animais.remove("gato")
print(animais)

print(len(animais))

print("gato" in animais)

print("")
lista = [500, 30, 300, 80, 10]
print(max(lista))
print(min(lista))

animais.append(["leão", "Cachorro"])
print("")
print(animais)
animais.extend(["cobra", 6])
print(animais)
print(animais.count("leão"))

lista.sort()
print("")
print(lista)

print("\nTuplas\n")
#As tuplas usam parênteses como sintaxe
tp = ("Banana", "Maçã", 10, 50)
print(tp[0])

#Diferente das listas as tuplas são imutáveis, o que quer dizer que não podemos alterar os seus elementos
#tp[0] = "Laranja" - este tipo de alteração gera erro

print(tp.count("Maçã"))
print(tp[0:2])

print("\nDicionários\n")
#Para criar um dicionário utilizamos as {}
dc = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5} #Dicionários trabalham com o condeito chave e valor
print(dc)

#Acessando o valor de um dicionário através da chave
print(dc["Maçã"])

#Atualizando o valor da Maçã
dc["Maçã"] = 25
print(dc)

#Retornando todas as chaves do dicionário
print(dc.keys())

#Retornando os valores do dicionário
print(dc.values())

#Verificando se já existe uma chave no dicionário e caso não exista inserir
print(dc.setdefault("Limão", 22))
print(dc)
