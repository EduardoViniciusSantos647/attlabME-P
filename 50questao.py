alunos = {}

for i in range(5):
    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota: "))

    alunos[nome] = nota

soma = 0

for nome in alunos:
    soma = soma + alunos[nome]

media = soma / 5

print("Media da turma:", media)

print("Alunos aprovados:")

for nome in alunos:
    if alunos[nome] >= 7:
        print(nome, alunos[nome])
