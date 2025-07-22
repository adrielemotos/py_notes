import random

print("🎲 Bem-Vindo ao jogo de adivinhção!")
print("Tente adivinhar o número entre 1 e 100.")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        palpite = int(input("Digite seu palpite "))
        tentativas += 1

        if palpite < numero_secreto:
            print("🔻 Muito baixo. Tente um número maior!")
        elif palpite > numero_secreto:
            print("🔺 Muito alto. Tente um número menor!")
        else:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
            break
    except ValueError:
        print("❌ Por favor, digite um número válido.")
