usuarios = []

logado = 0
usuario_logado = ""

while True:
    if logado == 0:
        print("#########################################")
        print("SISTEMA DE CADASTRO DE USUÁRIOS")
        print("#########################################")
        print()
        print("===LOGIN===")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == "Admin" and senha == "123":
            print(f"Login realizado com sucesso! Bem-vindo, {login}!.")
            print()
            input("ENTER para continuar...")
            logado = 1
            usuario_logado = login
        else:
            print()
            print("Login ou senha incorretos! Tente novamente.")
            input("ENTER para tentar novamente...")

    if logado == 1:
        print("#########################################")
        print("SISTEMA DE CADASTRO DE USUÁRIOS")
        print("#########################################")
        print()
        print("===MENU PRINCIPAL===")
        print(f"Usuário logado: {usuario_logado}")
        print("1 - Inserir usuário")
        print("2 - Pesquisar usuário")
        print("3 - Remover usuário")
        print("4 - Listar todos os usuários")
        print("5 - Logout")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print()
            print("--- INSERIR USUÁRIO ---")
            nome = input("Digite o nome do usuário: ")

            if nome == "":
                print("Nome não pode ficar vazio!")
            elif nome in usuarios:
                print("Usuário já está cadastrado!")
            else:
                usuarios.append(nome)
                print("Usuário cadastrado com sucesso!")

            input("ENTER para continuar...")

        elif opcao == "2":
            print()
            print("--- PESQUISAR USUÁRIO ---")
            nome = input("Digite o nome para pesquisar: ")

            if nome in usuarios:
                print("Usuário encontrado:", nome)
            else:
                print("Usuário não encontrado.")

            input("ENTER para continuar...")

        elif opcao == "3":
            print()
            print("--- REMOVER USUÁRIO ---")
            nome = input("Digite o nome para remover: ")

            if nome in usuarios:
                usuarios.remove(nome)
                print("Usuário removido com sucesso!")
            else:
                print("Usuário não encontrado.")

            input("ENTER para continuar...")

        elif opcao == "4":
            print()
            print("--- LISTA DE USUÁRIOS ---")
            if usuarios == []:
                print("Nenhum usuário cadastrado.")
            else:
                contador = 1
                for nome in usuarios:
                    print(contador, "-", nome)
                    contador = contador + 1

            input("ENTER para continuar...")

        elif opcao == "5":
            print("Fazendo logout...")
            input("ENTER para continuar...")
            logado = 0

        elif opcao == "6":
            print("Encerrando o sistema... Até logo!")
            break

        else:
            print("Opção inválida!")
            input("ENTER para continuar...")