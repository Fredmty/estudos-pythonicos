"""
são matrizes/vetores.
são dinamicos e aceitam qualquer tipo de dado. 
Dinâmico: não possui tamanho fixo. 

listas sao representadas [] 
"""


lista1 = [1,99,29,391,19294,959192,39]

lista2 = ['g', 'h', 'w', 't', 'j']

lista3 = []

lista4 = list(range(11)) #gera uma lista com 10 elementos

lista5 = list('geek university')

#podemos facilmente ordenar uma lista.
lista1.sort()
print(lista1)

#podemos contar o numero de ocorrencias em uma lista
print(lista1.count(1)) #conta o numero de vezes que 1 aparece

#adicionar elementos em lista -> para adicionar elementos/valores em lista,
#adicionamos a função append.
#obs: com append, só add 1 elemento por vez
lista1.append(4111)#acidiona o elemento na lista 1 o valor 4111
lista1.append([1,2,3,4,5])#adiciona uma lista de elementos dentro da lista. é só um tipo aqui

lista1.extend([123,23,34])#adiciona individualmente cada elemento na lista. n aceita valor unico
#apenas iteraveis

#inserir elemento na posicação do indice - não substiti, desloca o valor (posicao, valor)
lista1.insert(2,'new value')

#podemos juntar 2 listas
lista6 = lista1 + lista2 #junta as duas listas por um espaço separado. faz a mesma coisa do extend

#reverter lista
lista1.reverse()
#reverter atual
lista1[::-1]

#copiar list
lista6 = lista2.copy()

#tamanho da lista - contagem de elementos
print(len(lista1))#length

#remover ultimo elemento da lista (retorna o elemento que foi popado)
lista5.pop()
#remover elemento pelo indicie (os elementos a direita deste indiice serão deslocados para a esquerda)
lista.pop(2)
#podemos remover todos os elementos
lista5.clear() #lista fica vazia.

#podemos repertir elelmentos da lista
lista7= [1,2,3]
lista7 = lista * 3 #printa [1,2,3,1,2,3,1,2,3]

#podemos covnerter string para lista
curso = "deeez nuts"
curso = curso.split() #separa os elementos até o espaço entre elas"
curso = curso.split(',')#separador vira o que está aqui. 


#converter uma lista em uma string
#pega a lista6, coloca  espaço em cada elemento e transforma em um elemento. 
curso = ''.join(lista6)
cruso = '$'.join(lista6) #separa a lista por $

#iterando em lista
for elemento in lista:
    print(elemento)

#while
carrinho = []
produto = ''
while produto != "sair":
    produto = input()
    if produto 1= "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


#utiliznado variaveis em listas
lista = [1,2,3]
num1=1
num2=2
num3=3
lista2 = [num1, num2, num3] 
#msm coisa

#adicionar elemento na primeira posicao
lista5.push()
