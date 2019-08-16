convidados = ['Ana', 'Regi', 'Giglio']
mensagem = ', vai fazer algo hoje a noite? que tal um jantar?'
print(convidados[0] + mensagem)
print(convidados[1] + mensagem)
print(convidados[2] + mensagem)

popped_convidado = convidados.pop(1)
print('É uma pena, mas fica pra proxima então ' + popped_convidado)

convidados.append('Suelen')

print(convidados[-1] + mensagem)
print(convidados[0] + mensagem)
print(convidados[-2] + mensagem)

convidados.insert(1, 'Ana Maria')
convidados.insert(2, 'Duda')
convidados.append('Samuel')

print ('encontrei uma mesa maior')

print(convidados[0] + mensagem)
print(convidados[1] + mensagem)
print(convidados[2] + mensagem)
print(convidados[3] + mensagem)
print(convidados[4] + mensagem)
print(convidados[5] + mensagem)

popped_convidado = convidados.pop(1)
print ("Sinto muito " + popped_convidado.title() + ", Fica pra proxima")
popped_convidado = convidados.pop(1)
print ("Sinto muito " + popped_convidado.title() + ", Fica pra proxima")
popped_convidado = convidados.pop(1)
print ("Sinto muito " + popped_convidado.title() + ", Fica pra proxima")
popped_convidado = convidados.pop(1)
print ("Sinto muito " + popped_convidado.title() + ", Fica pra proxima")

print(convidados[0] + convidados[1] + "Vocês ainda estão convidados")

del convidados[0]
del convidados[0]

print("Lista de convidados: ")
print(convidados)