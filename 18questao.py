total = 0

for i in range(7):
    venda = float(input("Digite o valor das vendas do dia: "))
    total = total + venda

print("Faturamento total da semana: R$", total)