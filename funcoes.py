"""
def nome_da_funcao(parametros):
    bloco_da_funcao

palavra reservada 'def' que significa que é uma função e abre 
o código com : (4 espaços depois do bloco)

obs: quando uma função n retorna nenhum valor em python
o tipo do valor é None

obs: funcoes pithons que retornam vlaores, devem retornar valores
com a palavra reservada return 

obs: return finaliza a função. sai da execução da função
obs: podemos ter em uma função, diferentes 'returns', mas só 
vai executar um deles
obs: podemos em uma função ,retornar qualquer tipo de dado e 
até multiplos valores

"""
#declarando funcao
def diz_oi():
    print('oi')

#refaforacao

def diz_oi_ref():
    return "oi"
#chamando funcao
diz_oi()

"""funcoes c retorno"""

def quadrado_de_7():
    return 7 * 7


#exemplo1: 

def diz_oi():
    return 'oi'
    return ('estou sendo executado apos o retorno')


#exemplo2:

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        reutrn 3.2
    return 'b'

#exemplo3:

def outra_funcao():
    return 2,3,4,5


num1, num2, num3, num4 = outra_funcao()
#output = 2,3,4,5 tupla

from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False

# funcoes com parametro

def quadrado(num):
    return num * num
    return num ** 2 #msm coisa 

#funcoes podem ter n parametros, separada por virgula

#exemplo

def soma(a,b):
    return a + b

def mult(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg #replica o numero de x a string


#nomeando parametros

def nome_completo(nome, sobrenome):
    return f'seunome completo é {nome} {sobrenome}

print(nome_completo{'angelina', 'jolie'}) 

#parametros sao variaveis declaradas na definicaçca o da funcao
#argumentos sao dados passados durante a execução


def soma_impar(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [ 1,2,3,4,5,6,7]

print(soma_impar(lista))