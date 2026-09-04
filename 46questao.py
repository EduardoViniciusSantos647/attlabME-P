

n = int(input("Digite a ordem da matriz (n x n): "))

matriz = []
print("Digite os elementos da matriz linha por linha (separados por espaço):")
for i in range(n):
    linha = list(map(int, input(f"Linha {i+1}: ").split()))
    matriz.append(linha)

soma = 0
for i in range(n):
    soma += matriz[i][i]

print("A soma da diagonal principal é:", soma)