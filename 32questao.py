
paciente = {
    "nome": input("Digite o nome do paciente: ")
}

print(f"\nCadastro inicial: {paciente}")

paciente["idade"] = int(input("Digite a idade do paciente: "))

print(f"Cadastro atualizado: {paciente}")