

funcionario = {
    "nome": input("Digite o nome do funcionário: "),
    "idade": int(input("Digite a idade do funcionário: ")),
    "setor": input("Digite o setor de atuação do funcionário: ")
}

print("\nDados cadastrados do funcionário:")
print(f"Nome: {funcionario['nome']}")
print(f"Idade: {funcionario['idade']}")
print(f"Setor: {funcionario['setor']}")