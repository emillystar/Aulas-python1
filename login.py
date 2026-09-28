logado = 0
usuario_logado = ""

while True:
 if logado == 0:
   print("#########################################")
   print("SISTEMA DE CADASTRO DE USUÁRIOS")
   print("#########################################")
   print()
   print("===LOGIN===""")
   login = (input("Digite seu login: "))
   senha = (input("Digite sua senha: "))
   
   if login =="Admin" and senha =="123":
    print("login realizado com sucesso! Bem-vindo, {login}!.")
    print()
    input("ENTER para continuar...")
    logado = 1
    usuario_logado = login 
    
   else:
    print("\nLogin ou senha incorretos! Tente novamente.")
    input("ENTER para tentar novamente...")
    
 if logado == 1:
   print("#########################################")
   print("SISTEMA DE CADASTRO DE USUÁRIOS")
   print("#########################################")
   print()
   print("===MENU PRINCIPAL===""")
   print(f"Usuário logado: {usuario_logado}")
   print("1 - Inserir usuário")
   print("2 - Pesquisar usuário")
   print("3 - Remover usuário")
   print("4 - Listar todos os usuários")
   print("5 - Logout")
   print("6 - Encerrar")
   
   opcao = input("Escolha uma opção: ")

   if opcao == "1":
     
    print("[EM DESENVOLVIMENTO] - Função Inserir usuário ainda não implementada.")
    input("ENTER para continuar...")
    
   elif opcao == "2":
     
     print("[EM DESENVOLVIMENTO] - Função Pesquisar usuário ainda não implementada.")
     input("ENTER para continuar...")
     
   elif opcao == "3":
     
     print("[EM DESENVOLVIMENTO] - Função Remover usuário ainda não implementada.")
     input("ENTER para continuar...")
     
   elif opcao == "4":
     
     print("[EM DESENVOLVIMENTO] - Função Listar usuário ainda não implementada.")
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



