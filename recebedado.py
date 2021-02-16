print("qual seu nome?")
nome = input()  # -> todo dado recevbido via input é do tipo STRING
#em python, tudo que estiver entre aspas é STRING
#aspas simples, aspas duplas, aspas simples trilplas e aspas duplas triplas
#'angelina'
#"angelina"
'''angelina'''
"""angelina"""


print('seja bem vindo %s' % nome)

print('qual sua idade')
idade = input()
#formas antigas de print
print(' a %s tem %s anos', % (nome, idade))



#formas novas de print, python 3.x

print('seja bemvindo {0}' .format(nome))

print('seja bemvindo {0}, voce temo {1} anos' .format(nome, idade))


#forma mais atual (python 3.7)

print(f'seja bem vindo {nome}') #f antes é formatar
print(f'seja vem vindo {nome} tem {idade} anos')


idade = int(input('qual sua idade?')) #já fazendo o casting e tirnado a operaçao do final
print(f'a {nome} nasceu em (2018 - {idade}'))


type(variavel) #retorna o tipo da variável 1_000 retorna 1000
#o comando dir(variavel) retorna as operações que é possível fazer com a variavel