from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gugu', 10)
restaurante_praca.receber_avaliacao('Gaby', 7)
restaurante_praca.receber_avaliacao('AAAAA', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()