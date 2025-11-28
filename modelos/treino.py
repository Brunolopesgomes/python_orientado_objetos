class Musica :

    musicas = []

    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():

        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


m1 = Musica('Arde outra vez','Thales Roberto',180)
m2 = Musica('imperfeito','seilaf', 160)
