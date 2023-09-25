""" 

if, else, elif

operadores unários:
not, is

operadores binários:
and, or, is

"""
print('==== IF, ELSE, ELIF ====')
idade = 50

if idade < 18:
    print(f'Sua idade é {idade}, considerado menor de idade')
elif idade > 18 and idade < 30:
    print(f'Sua idade é {idade}, considerado adulto') 
elif idade >= 60:
    print(f'Sua idade é {idade}, considerado idoso')
else:
    print(f'Sua idade é {idade}, considerado adulto')

print('\n==== AND, OR, NOT, IS ====')
ativo = True
logado = True

# os 2 valores devem ser verdadeiros por ser 'and' (satisfazer as 2 condições)
if ativo and logado:
    print('Bem vindo usuário!!')
else:
    print('Você precisa ativar sua conta, por favor cheque seu email...')

# um dos valores deve ser verdadeiro por ser 'or' (satisfazer pelo menos 1 condição)
if ativo or logado:
    print(f'Voce está ativo: {ativo}')
    print(f'Voce está logado: {logado}')

# valor booleano invertido, True >> False and False >> True (negação)
print(not True)
print(not False)

ativo = False
if not ativo: # se não está ativo 
    print('Voce precisa ativar sua conta, favor checar seu email...')
else: # se sim
    print('Bem vindo usuário!!')


print(ativo is False)
if ativo is False:
    print('Entra na conta correta')

nome = 'teste'

if nome.istitle():
    print('Nome está em maiúsculo')
else:
    print('Nome está em minúsculo')

