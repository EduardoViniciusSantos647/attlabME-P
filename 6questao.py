

codigo = int(input("Digite o código do equipamento: "))

if codigo % 2 == 0:
    print(f"O código {codigo} é PAR - Equipamento do setor administrativo.")
else:
    print(f"O código {codigo} é ÍMPAR - Equipamento do setor operacional.")