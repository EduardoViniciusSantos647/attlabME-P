

alunos = {}

for i in range(5):
    print(f"\nCadastro do aluno {i+1}:")
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

print("\n--- Registros de todos os alunos ---")
for nome, nota in alunos.items():
    print(f"Nome: {nome} | Nota: {nota}")