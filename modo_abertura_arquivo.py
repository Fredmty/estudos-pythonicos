"""
modos de abertura de arquivo

r -> abre para leitura - padrao
w -> abre para escrita  - sobrescreve caso o arquivo ja exista
x-> abre para escrita - somente se o arquivo n existir
a -> abre para escrita - adicionando no final do arquivo
+ -> abre para o modo de atualização (leitura e escrita)
#abrindo com o modo 'a', sginifica append, se não houver o arquivo
será criado. Senão vai ser escrito no final.
"""

#exemplo x
with open('university.txt', 'x'): as arquivo:
    arquivo.write('texte de conteudo')

#exemplo a
with open ('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('escreve fruta aqui campeão')
        if fruta != 'sair':
            arquivo.write(fruta)
        else:
            break

#exemplo escrita no topo c r+. onde temos o controle do cursor
with open('outro.txt', 'r+') as arquivo:
    arquivo.write('add')
    arquivo.seek(11)
    arquivo.write('nova linha')
    arquivo.seek(12)