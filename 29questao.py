

vendedor1 = float(input("Digite o valor de vendas do 1º vendedor: "))
vendedor2 = float(input("Digite o valor de vendas do 2º vendedor: "))
vendedor3 = float(input("Digite o valor de vendas do 3º vendedor: "))

vendas = (vendedor1, vendedor2, vendedor3)

maior_venda = max(vendas)

print(f"\nResultados de vendas: {vendas}")
print(f"O maior valor de vendas foi de R$ {maior_venda:.2f}")