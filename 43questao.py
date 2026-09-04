linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(float(input("Valor: ")))
    matriz.append(linha)

maior = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

print(matriz)
print(maior)
