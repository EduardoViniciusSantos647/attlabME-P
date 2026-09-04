

import random

numero_sorteado = random.randint(1, 10)

palpite = int(input("Tente adivinhar o número sorteado (entre 1 e 10): "))

if palpite == numero_sorteado:
    print("Parabéns! Você acertou o número sorteado.")
else:
    print(f"Você errou! O número sorteado era {numero_sorteado}.")