class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_piza = Restaurante()

restaurantes = [restaurante_piza, restaurante_praca]

print(vars(restaurante_praca))