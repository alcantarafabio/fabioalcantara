# Simples, Composto ou Aninhado (encadeado)

n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))

print(f"Suas notas são: {n1} e {n2}.");

# Calcular a média aritmética das notas:
media = (n1 + n2) / 2

print(f"Sua é média é: {media}");

if (media >= 7):
    print("Você foi aprovado!");
    print("Parabéns!");
else:
    print("Você está reprovado. Estude mais na próxima!");
