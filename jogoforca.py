palavra = "PYTHON"

letras_descobertas = []
letras_utilizadas = []

erros = 0
limite_erros = 6

print("=" * 35)
print("       JOGO DE ADIVINHACAO")
print("=" * 35)

while erros < limite_erros:

    # Exibe a palavra parcialmente descoberta
    print("\nPalavra: ", end="")

    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nErros: {erros}/{limite_erros}")

    # Verificar se o jogador descobriu a palavra
    ganhou = True
    for letra in palavra:
        if letra not in letras_descobertas:
            ganhou = False

    if ganhou == True:
        break

    # Pedir o palpite e guardar numa string
    palpite = input("Digite uma letra: ")
    palpite = palpite.upper()

    # Validar a entrada (se só tem uma letra e se é letra mesmo, não número). Use a função len e a função isalpha para isso.
    if len(palpite) != 1 or palpite.isalpha() == False:
        print("Entrada inválida! Digite apenas UMA letra.")
        continue

    # Verificar se a letra já foi utilizada
    if palpite in letras_utilizadas:
        print("Você já tentou essa letra! Tente outra.")
        continue

    # Adicionar a letra na lista de utilizadas
    letras_utilizadas.append(palpite)

    # Verificar se a letra existe na palavra. Se sim, adicionar ela na lista de descobertas. Se não, dizer que errou e incrementar os erros.
    if palpite in palavra:
        print("Acertou! A letra", palpite, "existe na palavra!")
        letras_descobertas.append(palpite)
    else:
        print("Errou! A letra", palpite, "não existe na palavra.")
        erros = erros + 1

# Resultado final
print("\n" + "=" * 35)

# Verificar se a pessoa ganhou ou perdeu e imprimir a mensagem correspondente.
if ganhou == True:
    print("PARABÉNS! Você venceu!")
else:
    print("Você perdeu! Acabaram suas tentativas.")

print(f"A palavra secreta era: {palavra}")

print("=" * 35)