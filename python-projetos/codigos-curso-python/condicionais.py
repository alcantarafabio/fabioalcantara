# Simples, Composto ou Aninhado (encadeado)

n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))

# Calcular a média aritmética das notas
media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif media >= 5 and media < 7:
    print("Você está de recuperação!")
else:
    print("Resultado: Reprovado!")

print('Sua média é {}'.format(media))
