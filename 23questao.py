

gastos = []

quantidade = int(input("Digite a quantidade de categorias de gastos: "))

for i in range(1, quantidade + 1):
    valor = float(input(f"Digite o valor gasto na categoria {i}: "))
    gastos.append(valor)

total = sum(gastos)

print(f"\nGastos registrados: {gastos}")
print(f"O total de gastos mensais foi de R$ {total:.2f}")