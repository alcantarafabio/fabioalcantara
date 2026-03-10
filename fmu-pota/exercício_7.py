# Exercício 7 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#  cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# Tratamos os vetores como listas para resolver este exercício e portanto, não precisamos da biblioteca NumPy

vetor1 = [0] * 10
vetor2 = [0] * 10
vetor3 = [0] * 20

print("Digite os 10 números do Vetor 1:")
for i in range(10):
    vetor1[i] = int(input(f"Vetor 1 [{i}]: "))

print("\nDigite os 10 números do Vetor 2:")
for i in range(10):
    vetor2[i] = int(input(f"Vetor 2 [{i}]: "))

contador = 0
for i in range(10):
    vetor3[contador] = vetor1[i]
    contador = contador + 1
    vetor3[contador] = vetor2[i]
    contador = contador + 1

print("\n--- Vetor 3 Intercalado ---")
print(vetor3)

