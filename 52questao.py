medicamentos = {}

for i in range(5):
    nome = input("Digite o nome do medicamento: ")
    quantidade = int(input("Digite a quantidade: "))

    medicamentos[nome] = quantidade

consulta = input("Digite o nome do medicamento que deseja consultar: ")

if consulta in medicamentos:
    print("Quantidade em estoque:", medicamentos[consulta])
else:
    print("Medicamento não encontrado.")