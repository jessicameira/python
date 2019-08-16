carros = ['BMW', 'Ford', 'Fiat', 'Audi', 'Citroen']
print("Lista original:")
print(carros)
print("aqui está a lista com a ordem alterada:")
#ao utilizar o sorted a ordem original é mantida, o metodo altera apenas
#para executar alguma função ou atividade solicitada no momento.
print(sorted(carros))
print("Novamente a lista normal:")
print(carros)
#o metodo reverse altera apenas a ordem da lista não ordenando de maior para menor
#ou ordem alfabetica
carros.reverse()
print(carros)
#utilizando o metodo sort para ordenar por ordem alfabetica
carros.sort()
print(carros)

#também fazer a inversão do sort, ou seja, por ordem alfabética inversa
carros.sort(reverse = True)
print(carros)
#A ordem pode ser dificil de considerar quando as palavras estão com minusculas
#e maiusculas sem uma ordem pre definida, é necessário manter um padrão para que essa ordenação dê certo
