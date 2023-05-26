class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} está comendo")

    def emitirSom(self):
        print(f"{self.nome} emitiu som")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} está miando")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def emitirSom(self):
        print(f"{self.nome} está latindo")

class Vaca(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)



g1 = Gato("Juninho","frajola")
g1.comer()
g1.emitirSom()

c2 = Cachorro("Robe", "Cinza")
c2.comer()
c2.emitirSom()

v3 = Vaca("Mari", "Branca")
v3.comer()
v3.emitirSom()
