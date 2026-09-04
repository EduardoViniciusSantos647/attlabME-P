


n = int(input("Digite a ordem da matriz quadrada (n x n): "))

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        valor = float(input(f"Digite o valor na posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nElementos da diagonal principal:")
for i in range(n):
    print(matriz[i][i])