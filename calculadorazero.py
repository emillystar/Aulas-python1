esc = -1

while esc != 0:
    print('''*** Calculadora de Números Reais ***
0. Sair
1. Soma
2. Subtração
3. Multiplicação
4. Divisão''')
    print("*" * 30)

    esc = int(input("Escolha a opção desejada: "))

    if esc == 0:
        print("Programa encerrado.")

    if esc == 1 or esc == 2 or esc == 3 or esc == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if esc == 1:
            print(f"Resultado: {n1} + {n2} = {n1+n2}")

        elif esc == 2:
            print(f"Resultado: {n1} - {n2} = {n1-n2}")

        elif esc == 3:
            print(f"Resultado: {n1} * {n2} = {n1*n2}")

        elif esc == 4:
            if n2 != 0:
                print(f"Resultado: {n1} / {n2} = {n1/n2:.2f}")
            else:
                print("Erro. Divisão por zero!")

    else:
        print("Operação inválida.")