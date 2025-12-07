idade = int(input("Digite sua idade: "))
if idade >= 18:
    habilitacao = input("Você tem habilitação? (sim/não): ").lower()
if habilitacao == "sim":
    print("Você pode dirigir")
else:
    print("Você não pode dirigir")
else:
    print("Você não pode dirigir, pois é menor de idade")