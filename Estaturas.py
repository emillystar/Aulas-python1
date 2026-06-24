if estatura1 == estatura2 or estatura1 == estatura3 or estatura2 == estatura3:
print("Há, pelo menos, 2 pessoas com a mesma estatura")
else:
maior = max(estatura1, estatura2, estatura3)
print("Maior estatura:", maior)