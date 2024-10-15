numero = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Carlos', 'Gustavo', 'Emirhan', 'Erick']
anos = [2003, 2024]

lista = [1,23,2,45,25,99]
for i in lista:
    print(i)

soma_impares = 0
for i in range(1,11,2):
    soma_impares += i
print(soma_impares)

for a in range(10,0,-1):
    print(a)

'''number = int(input('Digite o numero'))
for i in range (1,11,1):
    print(number * i)'''

list = [22,36,15,49]
soma = 0

try:
    for i in list:
        soma += i
    media = soma / len(list)
    print(f'Media dos valores: {media}')
except ZeroDivisionError:
    print('A lista está vazia')
except Exception as e:
    print(f'Ocorreu um erro: {e}')