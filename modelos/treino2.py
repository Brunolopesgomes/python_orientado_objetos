class Carro :

    carros = []

    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo.ljust(20)} | {self.cor.ljust(20)} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo.ljust(20)} | {carro.cor.ljust(20)} | {carro.ano}')


car1 = Carro('Fiat Uno','Branco',2000)
car2 = Carro('Fiat Idea','vermelho',2019)

Carro.listar_carros()
        