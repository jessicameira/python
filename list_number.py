for value in range(1,5):
    print (value)
    
#Pode ser colocado o range com uma lista
valores = list(range(1,20))
print (valores)

#Colocando informação de valores pares:
valor_par = list(range(2,11,2))
print(valor_par)
#é impresso na tela 2,4,6,8 e 10 pois o primeiro definido foi o 2, apartir disse o python irá até o número 11 
# contando de 2 e 2, como 12 que viria depois é maior que 11, não é apresentado.

squares = []
for valor in range(1,11):
    squares.append(valor**2)
    print(squares)
minimo = min(squares) #funcao min traz o menor valor da lista numerica
maximo = max(squares) #max traz o maior valor da lista numerica
soma = sum(squares) #sum traz a soma de todos os itens da lista numerica
print(str(minimo) + ', ' + str(maximo) + ', '+ str(soma))