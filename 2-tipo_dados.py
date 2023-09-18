"""

Tipos de dados

O que é? e Porque dados no plural?
Primeiramente vamos definir o que é dado. Dado é um valor "crú"


"""

# string: tudo que tiver entre aspas simples, duplas ou triplas. e a função input() sempre retorna um dado do tipo string
nome = input()
print(type(nome))

# int: valor inteiro
valor = 10
print(type(valor))

# float: valor flutuante, decimal, sendo seus separadores não ',' e sim '.'
valor2 = 1.5
print(type(valor2))

# boolean: sempre escreve True and False, com as inicias maiúsculas


# Converter tipos de dados: cast
int(input()) # Converte a entrada de dados do tipo string em um valor do tipo inteiro
float(input()) # O mesmo só que em valor do tipo float
float(int()) # Converte float em int, lembrando que esse método pode deixar o resultado impreciso
int(float()) # Converte int em float, lembrando que esse método pode deixar o resultado impreciso
