"""
noutras lingugens de programação, os dicionaríos são conhecidos como mapas. 

dicionários são coleções do tipo chave/valor

dicionáios são representados por {}

obs: sobre dicionários:
 --chave e valor são separados por : "chave" : "valor"
 -- tanto chave e valor podem ser de qualquer tipo de dado
-- podemos misturar tipos de dados
"""

#forma mais comum de criação de dicionários 

paises = { "br:" : "brasil", "eau": "estados unidos"}


#forma mnos comum

paises = dict{br='brasil', eua='Estados unidos', py='paraguay'}

pais = paises.get('py')
pais = paises.get('ru', 'nao ennctrado') #caso a chave n exista, é inseriad com esse valor padrão

#podemos verificar se tal chave está no dificionado
if 'chave' in local:
    variavel = dicionario['valor']

#adicionar elementeos no dicionario

receita = {'jan' :100, 'fev': 120, 'mar':300}
#forma1 mais comum

receita['abr'] = 350
#form2
novo dado = {'maio': 500}

receita.update{novo_dado} #msm coisa que receita.update({'maio:500})

#atualizando dados em dicionário

#forma1

receita['mai'] = 550

#forma2

receita.update({'mai':600})


#remover dados de um dicionario

#forma 1 #mais omum

receita.pop('mar')
ret = receita.pop('mar') #retorna o valor que foi eliminado
#aqui precisamos sempre passar a chave, se n há elemento, keyerror retorna
# ao remover um objeto, o valor desse objeto é sempre retornado

#forma2 mas também ocorre. 

del receita['fev'] #palavra del de deletar. neste caso, o valor removido não é retornado.
print(receita)


#metodos de dicionarios

#limpar o dicionario

d = dict{a=1, b=2, c=3}

d.clear() #zera todos os dados

#copiando

#forma1

novo = d.copy() #deep copy

novo['d']=4

print(d)
print(novo)

#forma2 shallow copy

novo = d

novo['d'] = 4

#forma nao usual de criaçao de dicionarios

outro = {}.fromkeys('a', 'b') #chave, valor

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido') #primeira chave , segunda valor
#fica tudo 'nome' - desconhecido.

#fromkeys recebe dois paramentros, um interavel e outro valor
#para cada valor do iteravel, gerara um valor e atribuira uma chave. 







