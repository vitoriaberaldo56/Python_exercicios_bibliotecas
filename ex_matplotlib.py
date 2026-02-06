import matplotlib.pyplot as plt
from random import randint

#10. Gráfico de linha: crie uma lista com valores de vendas de uma loja ao longo de 7 dias.Gere um gráfico de linha mostrando a evolução das vendas.

dias = ['seg','ter','qua','qui','sex','sab','dom']
vendas = [1550.44,2200.00,1793,3567.57,4874,5024,3145]

plt.plot(dias, vendas)
plt.title('Vendas em 7 dias')
plt.xlabel('Dias da Semana')
plt.ylabel('Valor')
plt.show()

#11. Gráfico de barras. Crie duas listas: nomes de produtos e quantidade vendida. Gere um gráfico de barras comparando as vendas.

produtos = ['Maçã','Banana','Melancia','Morango','Uva']
vendas = [15,33,9,22,18]

plt.bar(x=produtos,height=vendas,color='green')
plt.title('Vendas no mês de Abril')
plt.xlabel('FRT ',fontsize=11)
plt.ylabel('Quantidade vendida',fontsize=11)
plt.show()


#12. Gráfico de números aleatórios. Gere 20 números aleatórios entre 1 e 100 e crie um gráfico de linha exibindo esses valores.

numeros = []

for i in range(20):
    n = randint(1,100)
    numeros.append(n)

plt.plot(numeros)
plt.title('Números gerados')
plt.show()

