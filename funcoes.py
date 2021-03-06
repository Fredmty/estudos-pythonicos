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
        return 3.2
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
    return f'seunome completo é {nome} {sobrenome}'

print(nome_completo({'angelina', 'jolie'}))

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

#funcoes com parametro padroes (também conhecido ocmo parametro opcional)

def exponencial (numero, potencia):
    return numero ** potencia
def exponencialpadrao (numero, potencia=2): #por parametro, o exponecnial é 2, então sempre será ao quadrado.
    return numero ** potencia

print(exponencial(2,3)) # 2 * 2 * 2

print(exponencialpadrao(3)) #por padrão, eleve ao quadrado
print(exponencial(3,5)) #eleva a potencia informada pelo usuario
#caso no def exponencial seja passado 2 parametros o primeiro vai para o numero e o segundo irá para potência.

#em funcoes python ,os parametros com valores default devem sempre estar ao ifnal da declaração
#exemplo acima, onde o potencia é que recebe 2. se fosse o numero, deveria este ser colocado ao final.

#exemplo mais completo

def monstra_informacao(nome='fred', instrutor=False):
    if nome == 'fred' and instrutor:
        return 'bem vindo maluco'
    elif nome == 'fred':
        return 'erro mlk'
    return f'olá {nome}'

print(monstra_informacao())
print(monstra_informacao(instrutor=True))
print(monstra_informacao('ozzy'))

#pq usar parametros default?

#mais flexivel com funcao, evita erros com parametros incorretos, nos permite trabalhar com código mais legitvel
#qual tipo de dados podemos utilizar como default? TODOS, inclusive funções!

"""
escopo

variaveis globais
variaveis locais

instrutor = 'geek' # variavel global

def pepe():
    instrutor = 'python' #variavel local"
    return f'oi {instrutor}
    
se tivermos uama variavel local com o mesom nome de uma global, a variaveil local terá preferencia 
"""

#variveis globais

total = 0

def incremente():
    global total #declaração de como utilizar uma variavel global dentro do método
    total = total + 1
    return total


#podemkos ter funcoes declaradas dentro de outras funcoes

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()