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

def piramide(n):
    for x in range(1, 6):
        print(str(x)*x)

def coluna(num):
    num = int(input("Digite um número: "))
    for x in range(1,num +1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()

def vogal(t):
    cont = 0
    vogais = "aeiouAEIOU"
    for x in t:
        if x in vogais:
            cont += 1
    print("O número de vogais é: ", cont)

def estoque(produto, quantidade, valor):
    total = quantidade * valor
    return produto, total

def soma(*numeros):
    soma = 0
    for x in numeros:
        soma = soma + x
    return soma

def texto(frase):
    cont = 0
    textoi = ""
    for x in frase:
        if x != " ":
            cont += 1
    print(f"A quantidade de letras na frase é: {cont}")
    for y in range(len(frase)-1, -1, -1):
        textoi += frase[y]
    print(textoi)

def lista(numeros):
    nova_lista = []
    for x in numeros:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)
