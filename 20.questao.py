total = 0

nota = float(input("Digite a nota (0 para encerrar): "))

while nota != 0:
    total = total + nota
    nota = float(input("Digite a nota (0 para encerrar): "))

print("Soma total das notas:", total)