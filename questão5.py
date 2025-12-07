cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ").lower()
if cor == "verde":
    print("Pode passar")
elif cor == "amarelo":
    print("Atenção!")
elif cor == "vermelho":
    print("Pare")
else:
    print("Cor inválida")