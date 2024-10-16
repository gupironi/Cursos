'''
Exercícios
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.

3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
'''
#1
pessoa = {'nome':'Jose','idade':29,'cidade':'São Paulo'}

#2
pessoa['idade'] = 31
pessoa['profissão'] = 'Professor'
del pessoa['cidade']

#3
num_quad = {x: x**2 for x in range(1,6)}
print(num_quad)

#4
if 'nome' in pessoa:
    print('A chave foi encontrada')

#5
frase = 'O mundo está quase explodindo em 2024, e vai em 2025'

contagem_palavras = {}
palavras = frase.split()

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra,0) + 1
    print(contagem_palavras)