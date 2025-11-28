pessoas = []

class Pessoa():
    
    def __init__(self,nome,idade,profissao):
    
        self.nome = nome
        self.idade = idade
        self._profissao = profissao
        pessoas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
        print(f'Idade nova: {self.idade}')

    @property
    def profissao(self):
        return f'Saudações meu caro {self._profissao}'

    def listar_pessoas():
        for pessoa in pessoas :
            print(f'{pessoa.nome} | {pessoa.idade} | {pessoa.profissao}')
                

Bruno = Pessoa('Bruno',25,'Desenvolvedor')
Rafa = Pessoa('Rafa',22,'Administradora')

Pessoa.listar_pessoas()




