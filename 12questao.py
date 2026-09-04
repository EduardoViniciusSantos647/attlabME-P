

velocidade = float(input("Digite a velocidade registrada do veículo (km/h): "))

if velocidade > 80:
    print(f"O veículo ultrapassou o limite permitido! Velocidade registrada: {velocidade} km/h.")
else:
    print(f"O veículo está dentro do limite permitido. Velocidade registrada: {velocidade} km/h.")