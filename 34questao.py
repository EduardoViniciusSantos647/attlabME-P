

notas = {
    "Ana": 8.5,
    "Bruno": 7.2,
    "Carla": 9.0,
    "Diego": 6.8
}

nome = input("Digite o nome do estudante que deseja consultar: ")

if nome in notas:
    print(f"A nota de {nome} é {notas[nome]}.")
else:
    print(f"O estudante {nome} não foi encontrado no cadastro.")