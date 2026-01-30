from random import randint, sample

#1. Sorteio com repetição
#Crie um programa que sorteie 5 números inteiros entre 1 e 50, podendo repetir valores. Ao final, mostre a lista sorteada.
#

# numeros = []
#
# for i in range(5):
#     n = randint(1, 50)
#     numeros.append(n)
#
# print(numeros)


# 2. Sorteio sem repetição
# Usando a mesma faixa de números (1 a 50), sorteie 5 números diferentes, sem repetir.

# n = sample(range(1,50), 5)
# print(n)


# 3.Simule o lançamento de um dado 10 vezes. Armazene os resultados em uma lista e informe:
# Quantas vezes saiu o número 6 e qual foi o maior valor sorteado

lancamentos = []
contador = 0

for i in range(10):
    n = randint(1,6)
    lancamentos.append(n)


for n in lancamentos:
    if n == 6:
        contador +=1

maior = max(lancamentos)
print(f'Números sorteados: {lancamentos}')
print(f'O número 6 saiu {contador} vezes! ')
print(f'O maior número sorteado foi: {maior}')