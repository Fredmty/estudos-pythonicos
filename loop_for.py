"""
loop -> estrutura de repetições
"""

nome = 'aloka'
lista = [1, 3, 5, 7 , 9]
numeros = range(1,10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)


"""
range (valor_inicial, valor_final)
obs: o valor final não é inclusive (valor_final -1)
"""
for numero in range:
    print(numero)
#printa o que ta'escrito no nome
for i, v  in enumerate(nome):
    print(nome[i])
#printa o nome e valor
for valor in enumerate(nome):
    print(valor)

qtd = int(input('quantasvezezs esse loop deve rodar'))
#não vai até o final do loop, digita 5 e vai até 4
for n in range(1, qtd):
    print('imprimindo {n}')
#vai até o final do loop, digita 5 e vai até 5 .
for n in range(1, qtd+1):
    print('imprimindo {n}')


qtd1 = int(input('n de vez q roda'))
soma = 0

for n in range(1, qtd1+1):
    num(int(input('finorm o valor')))
    soma = soma + num
print( 'valor de soma é'{soma})
#printa tudo numa linha 
for letra in nome:
    print(letra, end='')
