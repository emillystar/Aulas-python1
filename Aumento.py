Print("Lista De Cargos")
Print("Programador de Sistemas - 30% aumento")
Print("Analista de Sistemas - 20% aumento")
Print("Analista de Banco de dados - 15% aumento")

salario = float(input("Digite o salário: "))
cargo = input("Digite o cargo: ")

if cargo == "Programador de Sistemas":
novo_salario = salario * (30/100)
print("Novo salário:", novo_salario)

elif cargo == "Analista de Sistemas":
novo_salario = salario * (20/100)
print("Novo salário:", novo_salario)

elif cargo == "Analista de Banco de Dados":
novo_salario = salario * (15/100)
print("Novo salário:", novo_salario)

else:
print("Cargo inválido")