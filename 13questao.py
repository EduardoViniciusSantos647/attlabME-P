setor1 = float(input("Digite o consumo do Setor 1 (kWh): "))
setor2 = float(input("Digite o consumo do Setor 2 (kWh): "))

if setor1 > setor2:
    print(f"O Setor 1 teve o maior consumo, com {setor1} kWh.")
elif setor2 > setor1:
    print(f"O Setor 2 teve o maior consumo, com {setor2} kWh.")
else:
    print(f"Os dois setores tiveram o mesmo consumo: {setor1} kWh.")