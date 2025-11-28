class Restaurante :

    def __init__(self,nome,categoria):
        
        self.nome = nome
        self.categoria = categoria
        self.ativo = False


    def __str__(self):
        return f'{self.nome.ljust(10)} | {self.categoria.ljust(10)} | {self.ativo}'
    


t1 = Restaurante('Nome','Categoria')
r1 = Restaurante('tati','Marmita')

print(t1)
print(r1)