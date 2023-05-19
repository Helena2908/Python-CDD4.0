import random

palavras = ["escola", "sapato", "carro", "sonhar", "gentil", "amor", "mulher", "amizade", "jogos", "flor"]

palavra_secreta = random.choice(palavras)

print(f'A palavra tem {len(palavra_secreta)} letras.')
letras_certas = []
letras_erradas = []
erros = 0

while True:
    letra = input("Escolha uma letra: ").lower()

    if len(letra) == len(palavra_secreta):
        if letra == palavra_secreta:
            print("Parabéns, essa é a palavra secreta:", palavra_secreta)
            break
        else:
            print("A palvra secreta está erada.")
            letras_erradas.append(letra)

    if letra in letras_certas or letra in letras_erradas:
        print('Você já tentou essa letra.')
    elif letra in palavra_secreta:
        print('Acertou!')
        letras_certas.append(letra)
    else:
        print(f'Errou. A palavra não contém a letra "{letra}".')
        letras_erradas.append(letra)
        erros += 1

        if erros == 5:
            print('Fim de jogo!')
            print(f'A palavra secreta era "{palavra_secreta}".')
            break

    palavra_para_mostrar = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_para_mostrar += letra_secreta
        else:
            palavra_para_mostrar += '_'

    print(palavra_para_mostrar)

    if palavra_para_mostrar == palavra_secreta:
        print('Parabéns! Você ganhou!')
        break