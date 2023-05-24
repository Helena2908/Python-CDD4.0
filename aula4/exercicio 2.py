class Banco:

    def __init__(self, numero, saldo, nomeCliente, tipo, status=True):
        self.numero = numero
        self.saldo = saldo
        self.nomeCliente = nomeCliente
        self.tipo = tipo
        self.status = status

    def depositar(self, ):
        if self.status == True:
            print(f"O dinheiro foi depositado!")
            self.status = True
        else:
            print(f'O dinheiro não foi depositado pois a conta está inativa')
            self.status = False

    def sacar(self, saldo):
        self.saldo = saldo
        if self.saldo == 0:
            print(f"Não foi possível sacar o dinheiro pois a conta não tem saldo!")
        else:
            if self.status == False:
                print(f"Não foi possível sacar o dinheiro pois a conta está inativa!")
                self.status = False
            else:
                print(f'O dinheiro foi sacado com sucesso')
                self.status = True

    def verificarSaldo(self, saldo):
        self.saldo = saldo
        if self.status == True:
            print(f'O saldo da conta é {self.saldo}')
            self.status = True
        else:
            print(f'Não é possível ver o saldo pois a conta está inativa')
            self.status = False

    def ativar(self, status):
        if status == False:
            print(f'A conta foi ativada!')
            self.status = True
        else:
            print(f'Não foi possível ativar a conta pois a mesma ja está ativada!')
            self.status = True

    def desativar(self, saldo, status):
        self.saldo = saldo
        if status == False:
            print(f'Não foi possível desativar a conta pois a mesma ja está desativada!')
            self.status = False
        else:
            if saldo != 0:
                print(f'Não foi possível desativar a conta pois é necessario que a conta esteja zerada!')
            else:
                print(f'A conta foi desativada!')
                self.status = False


b1 = Banco(123, 60, "Bruno", "corrente")
b1.desativar(1, status=True)
b1.desativar(0, status=True)
b1.depositar()
b1.ativar(status=True)
b1.depositar()
b1.sacar(1)
b1.sacar(0)
b1.desativar(0, status=True)
b1.sacar(1)
b1.verificarSaldo(60)



