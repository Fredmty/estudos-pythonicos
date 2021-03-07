"""
*args é um parametro como qualquer outro. siginifca que dá pra chamar ele de qqualquer nome,desde que use o * na frente

por convenção, chamamos de *args para facilidtar

o *args é utilizado em uma função para colocar os vvalores extras informados como entrada
numa tupla. então já sabemos que as tuplas são IMUTÁVEIS.



"""


#exemplo ruim

def soma_todos_num(num1=1, num2=2, num3=3):
    return num1 + num2 + num3

#exemplo refatorado

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

#exemplo refatorado melhorado

def soma_todos_numeros_att(*args):
    return sum(args) #chamada do metodo sum para utilizar na tupla


print(soma_todos_numeros_att(1, 2, 3, 4, 5))


#outro exemplo

def verifica_info(*args):
    if 'geek' in args and 'university' in args:
        return 'bem vindo kkj'
    return 'numzei'

print(verifica_info())
print(1, True, 'geek', 'university')

#desempactoador

# * serve para que seja informado ao python que é uma coleção de dados e deve ser 'desempacotada' antes de avaliar os dados