
import random

lista = []

n = int(input("Quantas pessoas compraram a rifa? "))

for i in range(n):
    nome = input("Digite o nome do comprador: ")
    lista.append(nome)

sorteado = random.choice(lista)

print("O ganhador foi:", sorteado)