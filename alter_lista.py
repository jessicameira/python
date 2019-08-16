motos = ['honda', 'kawasaki', 'yamaha','suzuki']
print(motos)

motos[0] = 'ducati'
print(motos)

#O Metodo append adiciona ao final da lista o valor
motos.append('honda')
print(motos)

#O Metodo insert adiciona no local informado alterando a posição dos outros itens da lista
motos.insert(2, 'BMW')
print(motos)

#del pode deletar valores de uma lista
del motos[5]
print(motos)

#a instrução pop deleta o ultimo registro da lista,
#nesse caso passamos os registro deletado para outra variavel.
popped_motos = motos.pop()
print (motos)
print(popped_motos)

#passando o indice para o pop
popped_motos2 = motos.pop(0)
print ("A primeira moto que eu comprei foi a " + popped_motos2.title())

#remove pode ser usado para remover o valor que seja igual ao que foi passado
motos.remove('kawasaki')
print(motos)

muito_caro = 'BMW'
motos.remove(muito_caro)
print("Removi a " + muito_caro.title() + " Pois é muito caro pra mim" )
# O Metodo remove, apaga apenas o primeiro registro que contenha a 
#informação que encontrar, caso haja outros é necessário utilizar uma
#estrutura de repetição.