def MaiorSequencia(lista_numeros):
  '''
  Retorna a maior sequência de números presente em uma lista de uma lista 2D.
  
  :param lista_numeros: Uma lista 2D que contenha outra lista.
  :type lista_numeros: list
  :return: Retorna a maior lista que estava dentro de lista_numeros.
  :rtype: list
  '''
  maior_tamanho = 0
  maior_sequencia = []

  for lista in lista_numeros:
    if len(lista) > maior_tamanho:
      maior_tamanho = len(lista)
      maior_sequencia = lista

  return maior_sequencia