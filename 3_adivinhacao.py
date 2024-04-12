import random

numero_secreto = random.randint(1, 10)
# cheat code print(numero_secreto)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    elif palpite > numero_secreto:
        print("Quase! Tente um valor menor!")
        tentativas -= 1
    else:
#       palpite < numero_secreto:
        print("Quase! Tente um valor maior!")
        tentativas -= 1
print("Fim do jogo.")