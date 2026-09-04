
linhas = int(input("Digite o número de linhas (setores): "))
colunas = int(input("Digite o número de colunas (períodos): "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input(f"Digite o valor de produção na posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor

print(f"\nMatriz de produção: {matriz}")
print(f"A soma total dos valores da matriz é: {soma}")