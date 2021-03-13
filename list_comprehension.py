"""
lista comprehension

#sintaxe da lista comprehension

[dado for dado in itareval]



"""

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

"""
para entender melhor o que está acontecendo ,dividimos em 2 o que está acontece

- a primeira parte : for numero in numeros
- a segunda parte : numero * 10
"""

res = [numero / 2 for numero in numeros]

print(res)

def funcao(valor):
    return valor*valor

res = [funcao(numero) for numero in numeros]

#list comprehension vs loop


#loop

numeros = [1,2,3,4,5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrado = numeros * 2
    numeros_dobrados.append(numero_dobrado)
print(numeros_dobrados)
#refatorado
for numero in [1,2,3,4,5]:
    numeros_dobrados.append(numero * 2)

#list comprehension
print([numero * 2 for numero in numeros])

#outros exemplos

nome = 'geek university'

print([letra.upper() for letra in nome])

#2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

#3
print([numero * 3 for numero in range(1, 10)])

#4
print([bool(valor) for valor in [0, []. '', True, 1, 3.14]])


#5

print(str[numero] for numero in [1,2,3,4,5])

amigos = ['julia', 'pedro', 'maria', 'vanessa']
print([amigo[0].upper() for amigo in amigos])