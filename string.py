
'aula sobre strings'

nome = 'fredeus'
print(nome)
print(type(nome))


nome = "ginas's bar"
print(nome)
print(type(nome))

nome = 'angelina /n jolie'
print(nome)
print(type(nome))
### aspas duplas triplas serve como o /n também
### conforme o exemplo abaixo.
### utilizar \ permite o uso de strings como " '"
nome = """Angelina
JOlie"""
print(nome)
print(type(nome))

#aumenta tudo pra maiusculo
print(nome.upper())

#aumenta tudo pra minusculo
print(nome.lower())

#separa uma palavra a cada espaço, criando uma lista
# transforma em uma lista de strigns
print(nome.split())
#printa o que está de 0 até 3, ou seja "geek"
print(nome[0:4]) #operacao chamada de slice de string
#inverte a string no seu total, começa do primeiro
# ao último e DEPOIS inverte ela. 
print(nome[::-1])

#metodo pra trocar letras
print(nome.replace('G', 'P'))

