palavra_secreta = ["a", "m", "o", "r"]
letras_descobertas = []

print("Jogo da forca")

for x in range(0,len(palavra_secreta)):
    letras_descobertas.append("-")

acertou = False

while acertou == False:
    letra = str(input("Digite a letra: "))
    for x in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[x]:
            letras_descobertas[x] = letra
        print(letras_descobertas[x])
    acertou == True
    for y in range(0,len(letras_descobertas)):
        if letras_descobertas[y] == "-":
            acertou = False
    
