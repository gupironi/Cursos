class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

print(vars(restaurante_praca))

if restaurante_praca.ativo == True:
    print('O restaurante está ativo')
else:
    print('O restaurante está inativo')

categoria = restaurante_praca.categoria

print(categoria)

if restaurante_pizza.categoria == 'Fast Food':
    print('Categoria Fast Food')
else:
    print('Categoria não Fast Food')

print(f'O nome do restaurante é {restaurante_praca.nome} e a categoria {restaurante_praca.categoria}')