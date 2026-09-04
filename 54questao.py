# Programa para analisar a ocupação de um estacionamento (matriz 3x3)
estacionamento = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

ocupadas = 0
livres = 0

for i in range(3):
    for j in range(3):
        if estacionamento[i][j] == 1:
            ocupadas += 1
        else:
            livres += 1

print("Matriz do estacionamento:")
for linha in estacionamento:
    print(linha)

print("\nVagas ocupadas:", ocupadas)
print("Vagas disponíveis:", livres)