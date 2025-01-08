from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Monster', 6.9, 'Gigrande')
prato_teste = Prato('Burgao', 27.8, 'O burgao paulistao')

def main():
    print(bebida_suco)
    print(prato_teste)

if __name__ == '__main__':
    main()