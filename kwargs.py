"""
**kwargs
só mais um parametro
porém difere do *args que coloca os valores em uma tupla
o **kwards pede  que os parametros sejam nomeados e transforma eles em um dicionário

"""


#exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', juliana='amarelo', fernando='azul')

#exemplo complexo

def cumprimento_diferente(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'sabe python safado'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek!"
    return 'dunno bro'

print(cumprimento_diferente())
print(cumprimento_diferente(geek='python'))
print(cumprimento_diferente(geek='oi'))
print(cumprimento_diferente(geek='especial'))


"""
dentro das funcoes, podemos ter (nesta ordem):
parametros obrigatorios
*args;
oarametros default( nao obrigatorios);
**kwargs
"""


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

print(minha_funcao(8, 'julia'))

print(minha_funcao(18, 'aloca', 4, 5, 6, solteiro=True))

print(minha_funcao(34, 'frederico', eu='não', voce='vai'))

print(minha_funcao(19, 'sofia', 9, 4, 3, java=False, python=True))

#funcao com a ordem correta de parametros
def mostra_info_correta(a, b, *args, instrutor='geek', **kwargs):
    return[a, b, args, instrutor, kwargs]
#funcao com a ordem incorreta
#def mostra_info_incorreta(a,b, instrutor='geek', **kwargs):
#   return [a,b, args, instrutor, kwargs]


#desempactoar com **kwargs

def desempactoa(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'joao', 'sobrenome': 'dasilva'}


print(desempactoa(**nomes))

def soma_multiplos_num(a,b,c):

    print(a + b + c)

lista = [1, 2 ,3]
tupla = (1, 2, 3)
conjunto = {1, 2 ,3}

soma_multiplos_num(*lista)
soma_multiplos_num(*tupla)
soma_multiplos_num(*conjunto)

dicionario = dict(a=1,b=2,c=3)
soma_multiplos_num(**dicionario)
#obs: os nomes da chave em um dicionário devem ser os mesmos do parametro da funcao!







