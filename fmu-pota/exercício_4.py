# Exercício 4 - Faça um programa que leia 15 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

v_numeros = []
par = []
impar = []

for i in range(15):
    numero = int(input("Digite um número: "))
    v_numeros.append(numero)


    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Lista de números totais:", v_numeros)
print("Lista de números pares:", par)
print("Lista de números ímpares:", impar)