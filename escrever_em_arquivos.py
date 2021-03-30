"""
escrevendo em arquivos

#obs: ao abrir um arquivo para leitura, não podemos realizar
a escrita nele. Apenas ler.
Da mesma fora, se abrimos um arquivo para escrita, não 
podemos lêlo, somente escrever
ao abrir um arquivo para escrita, o arquivo é criado no sistema

para escrevers dados em um arquivo, após abrir um arquivo
utilizamos a função write().
esta função recebe uma STRING como parametro.

abrindo um arquivo para eescrita com o modo 'w', se o arquivo
não exisitr, ele será criado. caso ele JÁ exista, os dados do arquivo
serão apagados e sera crriado um novo dessa forma.
ABSOLUTAMENTE TODO CONTEUDO do arquivo é perdido. 

forma nao tradicional

arquivo = open('texto.txt', 'w')
arquivo.write('texto')
arquivo.close()
"""

#exemplo de escrita
#modo 'w' é write, escrita
with open('novo.txt', 'w') as arquivos:
    arquivo.write('escrever aqui é facil/n')
    arquivo.write('novalinha kek/n')
    arquivo.write('mais dados aqui/n')


with open('input.txt', 'w') as arquivo:
    while True:
        fruta = input('escreve aqui a fruta')
        if fruta != 'sair':
            arquivo.write(fruta + '/n')