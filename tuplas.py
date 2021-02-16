"""
tuplas

tuplas são bastante parecidas com lista
duas diferenças:

1 - tuplas são representadas por parenteses ()
2 - as tuplas são IMUTÁVEIS: ao se criar uma tupla, ela n muda. 
qualquer operação com uma tupla, gera outra tupla.
"""

#cuidado 1: tuplas são representadas por ()



#cuidado 2: tupla com 1 elemento 

#conclusão lógica : podemos concluir que tupla são definidas pela virgula e não pelo paratênses

#podemos gerar uma tupla dinamicamente no range(inicio, fim, passo)
tupla = tuple(range(11))# 0 a 10

#desempacotamento de tupla

tupla = ('geel university', 'pegraoamao')

escola, curso = tupla

#metodos para adic~ao e removação nas tuplas n existem. tuplas são IMUTAVEIS 



tupla = (1,2,3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice,valor) 


#contando elementos dentro da tupla

tuplaletras('a', 'b', 'c' , 'd', 'a')

print(tupla.count('a')) #retorna 2.

#dicas nas tuplas
#utilizar tupla sempre que não precisar modificar dados contidos em uma coleção



#slice

#tupla[inicio,fim, passo]

print(meses[5:9])#vai do 5 até o 8

#porque usar tuplas:? não temos problema de shallow copy
#tuplas são mais rapidas que lista (sao imutaveis)
#tuplas deixam seu código mais seguro (imutabilidade)
#trabalhra com elementos imutaveis traz segurança ao código 


#copiando uma tupla pra outra 

tupla1= (1,2,3)

nova = tupla
