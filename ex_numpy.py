#7. Lista para array: crie uma lista com 10 números inteiros digitados pelo usuário e transforme essa lista em um array NumPy. Depois,#mostre: a média, o maior valor, o menor valor

import numpy as np
from random import randint, sample
#
# lista = []
#
#
# for i in range(3):
#     n = int(input('Digite um número: '))
#     lista.append(n)
#
# a_lista = np.array(lista)
#
#
# print(f'Média dos valores: {round(np.mean(a_lista),1)}')
# print(f'O menor valor: {np.min(a_lista)}')
# print(f'O maior valor: {np.max(a_lista)}')


#8. Operações com arrays Crie dois arrays NumPy com 5 números cada. Faça: soma entre eles subtração multiplicação
#
#
# ar1 = np.array([5,8,3,1,0])
# ar2 = np.array([7,9,3,2,4])
#
# soma = np.add(ar1 , ar2)
# sub = np.subtract(ar1 , ar2)
# mult = np.multiply(ar1 , ar2)
#
# print(f'A soma entre os arrays é: {soma}')
# print(f'A subtração entre os arrays é: {sub}')
# print(f'A mult entre os arrays é: {mult}')


#9. Filtro de números: dado um array NumPy com vários números inteiros, crie um novo array apenas com os números pares

numeros = []

for i in range(20):
    n = randint(1,100)
    numeros.append(n)

ar_n = np.array(numeros)

ar_n_par = ar_n[np.where(ar_n % 2 == 0)]

print(f'Todos os números do Array{ar_n}')
print(f'Todos os números pares {ar_n_par}')