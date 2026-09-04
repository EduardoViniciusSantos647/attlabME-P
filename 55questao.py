

disciplinas = ("Matemática", "Português")

alunos = {}

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nCadastro do aluno {i+1}:")
    nome = input("Digite o nome do aluno: ")
    nota_mat = float(input("Digite a nota de Matemática: "))
    nota_port = float(input("Digite a nota de Português: "))
    
    alunos[nome] = {"Matemática": nota_mat, "Português": nota_port}

print("\n--- Disciplinas cadastradas ---")
for disciplina in disciplinas:
    print(disciplina)

print("\n--- Situação dos alunos ---")
for nome, notas in alunos.items():
    media = (notas["Matemática"] + notas["Português"]) / 2
    
    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    print(f"\nAluno: {nome}")
    print(f"Nota de Matemática: {notas['Matemática']}")
    print(f"Nota de Português: {notas['Português']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")