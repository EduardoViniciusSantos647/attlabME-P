participantes = []

quantidade = int(input("Digite a quantidade de participantes: "))

for i in range(quantidade):
    nome = input("Digite o nome do participante: ")
    participantes.append(nome)

participantes.reverse()

print("Ordem inversa de chegada:")
print(participantes)