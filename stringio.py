"""
StringIO:
para ler ou escrever dados em arquivos do sistema operacional
o software precisa ter permissão:
permissão de leitura -> ler o arquivo
permissão de escrita -> escrever o arquivo

StringIO -> utilizado paara ler e criar arquivos em memória

"""

#primeiro fazemos import
from io import StringIO

mensagem = 'esta é uma string normal'

#podemos criar um arquivo em memória já com string inserida
#ou vazai para inserir texto depois

arquivo = StringIO(mensagem)
#equivale ao arquivo = (arquivo.txt, 'w')
#com o arquivo criado, podemos utilizar tudo que vimos
#anrteriormente
print(arquivo.read())

#escrever outro texto
arquivo.write('touro texto')

#moviemntar cursors
arquivo.seek(0)

print(arquivo.read())