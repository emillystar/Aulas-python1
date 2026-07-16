soma = 0
quantidade = 0
maior = 0

while True:
numero = int(input("Digite um número inteiro positivo: "))

   if numero < 0:
      break

   soma += numero
   quantidade += 1

   if numero > maior:
    maior = numero

if quantidade > 0:
   media = soma / quantidade

   print("Soma:", soma)
   print("Média:", media)
   print("Maior número:", maior)

else:

print("Nenhum número positivo foi informado.")