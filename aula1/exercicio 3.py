def coluna(num):
    num = int(input("Digite um número: "))
    for x in range(1,num +1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()
coluna(5)
