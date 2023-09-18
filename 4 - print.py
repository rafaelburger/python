"""

print(): é uma função para imprimir no console a informação desejada

"""

print("Insira seu nome: ")
nome=input()

#or

nome=input("Insira seu nome: ")

print("Insira sua idade: ")
idade=input()

#or

idade=int(input("Insira sua idade: "))

# print sintaxe antiga (Python 2.x)
print("Seja bem vindo %s" % nome)
print("Seja bem vindo %s, sua idade é %s" % (nome, idade))

# print sintaxe moderna (Python 3.x)
print("Seja bem vindo {0}".format(nome))
print("Seja bem vindo {0}, sua idade é {1}".format(nome, idade))

# print sintaxe atual (Python 3.11)
print(f"Seja bem vindo {nome}")
print(f"Seja bem vindo {nome}, sua idade é {idade} e você nasceu em {2023 - int(idade)}") #caso não haver tido o cast anteriormente(conversão do tipo de dado)
print(f"Seja bem vindo {nome}, sua idade é {idade} e você nasceu em {2023 - idade}") #caso haver o cast anteriormente(conversão do tipo de dado)