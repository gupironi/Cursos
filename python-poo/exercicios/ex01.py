numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

idade = int(input('Qual a sua idade? '))

if idade >= 0 and idade <= 12:
    print('Criança: 0 a 12 anos')
elif idade >= 13 and idade <= 18:
    print('Adolescente: 13 a 18 anos')
else:
    print('Adulto: acima de 18 anos')

usuario = input('Usuario: ')
senha = input('Senha: ')

if usuario == 'gupironi' and senha == '123456':
    print('Acesso autorizado')
else:
    print('Acesso negado')

x = int(input('Qual o valor de X: '))
y = int(input('Qual o valor de Y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('Está localizado no eixo ou origem')