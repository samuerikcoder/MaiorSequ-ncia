'''
Escreva um programa no qual o usuário digita uma quantidade arbitrária de números inteiros positivos.
Quando o usuário digitar um número menor ou igual a 0, o programa deve indicar o tamanho da maior
sequência crescente observada. Por exemplo, se os números digitados forem 5, 10, 3, 2, 4, 7, 9, 8, 5, a maior
sequência crescente é 2, 4, 7, 9, então o programa deve mostrar na tela que a maior sequência crescente
tem 4 números. Já a sequência 10, 8, 7, 5, 2 está em ordem decrescente, portanto a maior sequência
crescente observada tem tamanho 1.

'''

from MaiorSequencia import MaiorSequencia

lista_numeros = []
lista = []

maior = 0
while True:
  num = int(input('\nDigite um número para a sequência: '))

  if num <= 0:
    break
  
  if num >= maior:
    maior = num
    lista.append(num)
  else:
    lista_numeros.append(lista[::])
    maior = num
    lista.clear()
    lista.append(num)

maior_sequencia = MaiorSequencia(lista_numeros)
print(f'\nA maior sequência lida teve o tamanho de {len(maior_sequencia)}')
print(maior_sequencia)