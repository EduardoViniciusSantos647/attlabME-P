

manha = float(input("Digite a temperatura média da manhã: "))
tarde = float(input("Digite a temperatura média da tarde: "))
noite = float(input("Digite a temperatura média da noite: "))
madrugada = float(input("Digite a temperatura média da madrugada: "))

temperaturas = (manha, tarde, noite, madrugada)

soma = sum(temperaturas)

print(f"\nTemperaturas registradas: {temperaturas}")
print(f"A soma das temperaturas foi de {soma}°C")