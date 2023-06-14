import random
import os



continuarJogo = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vitoria = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    os.system("cls")
    print("    0   1   2")
    print("0:   " + velha[0][0] + " I " + velha[0][1] + " I " + velha[0][2])
    print("   -----------")
    print("1:   " + velha[1][0] + " I " + velha[1][1] + " I " + velha[1][2])
    print("   -----------")
    print("2:   " + velha[2][0] + " I " + velha[2][1] + " I " + velha[2][2])
    print("Jogadas: " )

def jogadorJoga():
    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Escolha a linha que vai jogar: "))
        c = int(input("Escolha a coluna que vai jogar: "))
        while velha[l][c] != " ":
            l = int(input("Escolha a linha que vai jogar: "))
            c = int(input("Escolha a coluna que vai jogar: "))
        try:
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha e ou coluna inválida")


def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l=random.randrange(0, 3)
        c=random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        jogadas += 1
        quemJoga = 2
        ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == "O":
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = "O"
                break
            ic += 1

def verifvit():
    global velha
    global vitoria
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        #verificarlinhas
        il = ic = 0
        while il <3:
            soma = 0
            ic = 0
            while ic <3:
                if(velha[il][ic]==s):
                    soma += 1
                ic +=1
            if(soma == 3):
                vitoria = s
                break
            il += 1
        if(vitoria != "n"):
            break
        #verificar coluna
        il = ic = 0
        while ic<3:
            soma = 0
            il = 0
            while il <3:
                if(velha[il][ic]==s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
                ic += 1
        if (vitoria != "n"):
            break
            #Verifica diagonal 1
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc>=0:
            if(velha[idiagl][idiagc]==s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if(soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vitoria
    global continuarJogo
    continuarJogo = "s"
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vitoria = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while(continuarJogo == "s"):
    while True:
        if vitoria != "n" or jogadas >= maxJogadas:
            break
        tela()
        jogadorJoga()
        cpuJoga()
        vitoria = verifvit()
    print("Fim de Jogo")
    if vitoria != "n":
        print("Resultado: " + vitoria + "venceu")
    else:
        print("Resultado: Empate")
        continuarJogo = input("Jogar novamente? [s/n]:")
        redefinir()






            
