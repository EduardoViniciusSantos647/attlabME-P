

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

matriz = []
print("Digite os elementos da matriz linha por linha (separados por espaço):")
for i in range(linhas):
    linha = list(map(int, input(f"Linha {i+1}: ").split()))
    matriz.append(linha)

contador = 0
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > 0:
            contador += 1

print("Quantidade de valores positivos:", contador)