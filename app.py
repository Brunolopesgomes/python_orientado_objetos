from modelos.restaurante import Restaurante


restaurante_bruno = Restaurante('Restaurante do Bruno','Comida Boa')
restaurante_rafa = Restaurante('Restaurante da Rafa','Comida Boa')


def main():
    restaurante_rafa.alternar_estado()
    Restaurante.listar_restaurantes()
   
if __name__ == '__main__':
    main()