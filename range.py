for valor in range(1,5):
    print(valor)
    
#O Valor printado na tela  será de 1 a 4, a função range faz python 
# começar a contar no primeiro valor informado e parar ao alcançar 
# o segundo, como se fosse < a 5.

numeros = list(range(1,5))
print(numeros)
#a função lista serve para os valores de range sejam armazenados em uma lista

even_numeros = list(range(2,11,2))
print(even_numeros)
#nesse caso range(2,11,2) o inicio será em 2 o final em 11 e o valor, 
# o terceiro número informado representa o valor a ser somado,
# ou seja 2 + 2 = 4, +2 = 6... até o 11, como 10 + 2 é 12 o 11 não será apresentado
# e metodo irá parar no 10.
