import random

print(""" ///// Jogo de Adivinhação /////
Escolha o nível de dificuldade:
1- Fácil (1 a 10)
2- Médio (1 a 20)
3- Difícil (1 a 30) """)

num = int(input(": "))

if num == 1:
    limite = 10
elif num == 2:
    limite = 20
elif num == 3:
    limite = 30
else:
    print("Opção inválida!")

if num == 1 or num == 2 or num == 3:

    tent = int(input("""
||Quer incluir tentativas limitadas?
Digite 1 se sim e 0 para não.||
: """))

    numsort = random.randint(1, limite)
    nump = 0

    if tent == 1:
        cont = 0

        while nump != numsort and cont < 3:
            nump = int(input("Digite um número: "))
            cont += 1

            if numsort > nump:
                print("Errou! Tente um número maior.")
            elif numsort < nump:
                print("Errou! Tente um número menor.")
            else:
                print("Parabéns! Você acertou o número.")

        if nump != numsort:
            print("Suas tentativas acabaram!")
            print("O número era:", numsort)

    elif tent == 0:

        while nump != numsort:
            nump = int(input("Digite um número: "))

            if numsort > nump:
                print("Errou! Tente um número maior.")
            elif numsort < nump:
                print("Errou! Tente um número menor.")
            else:
                print("Parabéns! Você acertou o número.")

    else:
        print("Opção inválida:(")