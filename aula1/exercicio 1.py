def somar(a,b):
    soma = a+b
    print(soma)
def subtrair(a,b):
    sub = a-b
    print(sub)
def multiplicar(a,b):
    mult = a*b
    print(mult)
def dividir(a,b):
    div = a/b
    print(div)
num = 0
print("Essa é uma calculadora digital!")
print("===============================")
while num != 5:
    num = int(input("Escolha uma das seguintes opções: \n"
                    "1 - somar \n"
                    "2- subtrair \n"
                    "3- multiplicar \n"
                    "4- dividir \n"
                    "5- sair \n"))
    if num == 1:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite mais um número: "))
        somar(n1,n2)
    elif num == 2:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite mais um número: "))
        subtrair(n1,n2)
    elif num == 3:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite mais um número: "))
        multiplicar(n1,n2)
    elif num == 4:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite mais um número: "))
        dividir(n1,n2)
    else:
        print("Programa encerrado.")
        break

