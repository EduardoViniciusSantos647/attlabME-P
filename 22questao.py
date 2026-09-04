notas = []

quantidade = int(input("Digite a quantidade de notas: "))

for i in range(quantidade):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

maior = max(notas)

print("Notas:", notas)
print("Maior nota:", maior)