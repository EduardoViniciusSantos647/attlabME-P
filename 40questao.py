

import random

numero_sorteado = random.randint(1, 100)
tentativa = 0

print("Tente adivinhar o número sorteado (entre 1 e 100)!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativa += 1

    if palpite == numero_sorteado:
        print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativa} tentativa(s).")
        break
    elif palpite < numero_sorteado:
        print("O número procurado é MAIOR. Tente novamente.")
    else:
        print("O número procurado é MENOR. Tente novamente.")