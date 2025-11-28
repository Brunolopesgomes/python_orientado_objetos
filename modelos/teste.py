class Pessoa():

    lista_pessoas = []

    def __init__(self,nome,idade,cpf):

        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        Pessoa.lista_pessoas.append(self)

    def __str__(self):
        return f'{self.nome} {self.idade} {self.cpf}'

    def listar_pessoas():
        for pessoa in Pessoa.lista_pessoas:
            print(f'{pessoa.nome} | {pessoa.idade} | {pessoa.cpf}')

    
p01 = Pessoa('Bruno',22,12345678910)
p02 = Pessoa('Rafa',22,10987654321)

Pessoa.listar_pessoas()