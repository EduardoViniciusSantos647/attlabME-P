temperaturas = []
for i in range(5):
    temperatura = float(input("Digite a temperatura: "))
    temperaturas.append(temperatura)

soma = 0
for temperatura in temperaturas:
    soma = soma + temperatura

media = soma / 5
print("Media das temperaturas:", media)

if media >= 18 and media <= 28:
    print("A media esta dentro da faixa ideal.")
else:
    print("A media esta fora da faixa ideal.")

print("Temperaturas cadastradas:")
for temperatura in temperaturas:
    print(temperatura)