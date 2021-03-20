"""
leitura de arquivos

para arquivos em pthon, utilizamos a funcao open()

open()-> passamos um parametro de entrada (não é seu unico parametro, apenas o OBRIGATÓRIO), que é o caminho do arquivo
a ser lido. essa funcao tem como retorno isso:
__io.TextIOWrapper e é com ele que trabalhamos o arquivo. 

por padrão, a funcção open() abre o arquivo para leitura.
este arquivo DEVE existir senão gera "FileNotFoundError"

mode='r' é modo de leitura. r-> read() siginfica que só está lendo o arquivo
modo default do open é LEITURA.

o python utuliza um recurso para trabalhar com arquivos cahamado 'cursor', aquela coisa
que pisca enquanto digita

"""

arquivo = open('texto.txt')


ret = arquivo.read()
reta = ret.split('\n') #arruma o texto para quando há quebra de linha n aparecer o \n
#transforma em uma lista de string. 
print(arquivo)

print(type(arquivo))

#para ler o conteudo de um arquivo, depois do open, devemos utilizar read()

print(arquivo.read()) #é possível limitar o numero de caracteres por padrão que serao lindo