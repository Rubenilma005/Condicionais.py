numero = int(input("Digite um número: "))
if numero > 0 and numero % 2 == 0 and numero % 5 == 0:
    print("O número é positivo, par e múltiplo de 5")
else:
    print("O número não atende a todas as condições")