class ContaBancaria():
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'{self.titular} | {self.saldo} | {self.ativo}'
    
    def ativar_conta(self):
        self.ativo = not self.ativo
    

p01 = ContaBancaria('Bruno',2000)
p02 = ContaBancaria('Rafa',1500)


p02.ativar_conta()
print(p01)
print(p02)