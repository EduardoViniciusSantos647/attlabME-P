# Programa para encontrar o menor valor (menor custo)
# registrado em uma matriz que representa diferentes setores

linhas = int(input("Digite o número de linhas (setores): "))
colunas = int(input("Digite o número de colunas (períodos): "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input(f"Digite o custo na posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

menor_valor = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor < menor_valor:
            menor_valor = valor

print(f"\nMatriz de custos: {matriz}")
print(f"O menor custo registrado foi: {menor_valor}")