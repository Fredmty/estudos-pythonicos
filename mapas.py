"""
mapas -> conhecidos como dicionarios
dicioario sao {}
"""

receita = {'jan': 100, 'fev': 500, 'mar': 600}

#iterar sobre dicionario

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')



print(receita.keys()) #traz um dicionario de chaves

for chave in receita.keys(): #acessando as chaves
    print[(receita[chave])

print(receita.values())
 #modo pitonico de acesso aos valores
for valor in receita.values():
    print(valor)

#desempacotamento de dicioniários
 for chave, valor in receita.items():
     print(f'chave={chave} e valor={valor}')

#soma, max, min e len tmb se aplica aqui