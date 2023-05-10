def vogal(t):
    cont = 0
    vogais = "aeiouAEIOU"
    for x in t:
        if x in vogais:
            cont += 1
    print("O número de vogais é: ", cont)
texto = str("O rato roeu a roupa do rei de Roma")
vogal(texto)
