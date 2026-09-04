

matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        aluno = input(f"Digite o nome do aluno na posição [{i}][{j}]: ")
        linha.append(aluno)
    matriz.append(linha)

print("\nMatriz de alunos (2x2):")
for linha in matriz:
    print(linha)