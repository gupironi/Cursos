from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Monster', 6.9, 'Gigrande')
bebida_suco.aplicar_desconto()
prato_teste = Prato('Burgao', 27.8, 'O burgao paulistao')
prato_teste.aplicar_desconto()
sobremesa_torta = Sobremesa('Torta Holandesa',7.9,'Bem doce','Médio','A melhor torta do mundo')
sobremesa_torta.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_teste)
restaurante_praca.adicionar_no_cardapio(sobremesa_torta)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()