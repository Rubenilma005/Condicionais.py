# Pede a nota
nota = float(input("Digite sua nota (0 a 10): "))

# Verifica o resultado
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")