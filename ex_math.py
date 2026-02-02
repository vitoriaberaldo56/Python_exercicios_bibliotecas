from math import sqrt, pow, ceil, floor

#5. Cálculo de hipotenusa Peça ao usuário os valores dos catetos de um triângulo retângulo e calcule a hipotenusa.
#
# catetoB = int(input('informe o Cateto B: '))
# catetoC = int(input('informe o 2° Cateto C: '))
#
# hipotenusaA = pow(catetoB,2) + pow(catetoC,2)
# hipotenusa = sqrt(hipotenusaA)
#
# print(hipotenusa)


# 6.Arredondamentos Peça um número decimal ao usuário e mostre: o valor arredondado para cima o valor arredondado para baixo o valor arredondado normalmente


n = float(input('Digite um número decimal: ' ))

print(f'O valor arrendondado para cima é: {ceil(n)}')
print(f'O valor arrendondado para baixo é: {floor(n)}')
print(f'Valor arredondado normalmente: {round(n,2)}')