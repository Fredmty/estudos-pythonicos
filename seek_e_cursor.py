"""
seek e cursos

seek() -> utiliada para movimentar o cursor pelo arquivo

#obs: quando abrios um arquivo com a funcao open() é criada uma conexão com o arquivo
e o  disco do computador. essa conexão é chamada de STREAMING. 

ao finalizar os trabalhos ocm o arquivo, devemos fechar essa conexão
para isso, utlizamos a função close()

para se trabalhar com arquivos:
abrir arquivo
trabalhar arquivo
fechar arquivo

"""

arquivo = open('texto.txt')

print(arquivo.read())

#seek()-> é utilizada para movimentação do cursos pelo arquivo, ela recebe como
#parametro que indica onde quremos colocar o cursor
#movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0) #coloca no primeiro string o cursos, para reler o arquivo

arquivo.seek(20) #começa a ler a partir do caracter 20, por exemplo. 

print(arquivo.read()) #devemos printar novamente pq o arquivo já está aberto

#para ler linha a linha
#readLine() -> função que le  o arquivo linha a linha
print(arquivo.readLine())

ret = arquivo.readLine()

print(ret.split('')) # separa por espaços. 


#readLines -> gera uma lista de string
linhas = arquivo.readLines()
print(arquivo.readLines())
#print(len(arquivos.readLines()))
print(linhas) #conta o numero de linhas

#1 - abrir arquivo
arquivo = open('texto.txt')

#2 - trabalhar arquivo
print(arquivo.read())

#veriricar se arquivo está aberto ou fechado. gera um booleano se está aberto (true) e
#false se estive fechado.

print(arquivo.closed)

#3 - fechar arquivo
arquivo.close()