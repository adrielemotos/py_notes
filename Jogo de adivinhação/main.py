import random
import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt'else 'clear')

def avaliar_tentativas (tentativas):
    if tentativas <= 3:
        return "🌟 Excelente! Você foi muito sortudo!"
    elif tentativas <= 6:
        return "👍 Boa! Você mandou muito bem."
    elif tentativas <= 10:
        return "😅 Razoável! Mas dá pra melhorar."
    else:
        return "🤔 Precisa treinar mais a intuição"

def jogar():
    limpar_tela()
    print("🎲 Bem-Vindo ao Jogo de Adivinhação!")
    print("Você tem até 10 tentativas para acertar o número entre 1 e 100")
    time.sleep(1)

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limite_tentativas = 10

    while tentativas < limite_tentativas:
        try:
            palpite = int(input(f"\ntentativa {tentativas + 1}/{limite_tentativas} - Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("🔻 Muito baixo. Tente um número maior.")
            elif palpite > numero_secreto:
                print("🔺 Muito alto. Tente um número menor.")
            else:
                print(f"\n🎉 Parabéns! Você acertou em {tentativas} tentativas!")
                print (avaliar_tentativas(tentativas))
                break
        except ValueError:
            print("❌ Por favor, digite um número válido.")
        
    else:
        print(f"\n💥 Acabaram as tentativas! O número era {numero_secreto}.")

while True:
    jogar()
    jogar_novamente = input("\n🔁 Deseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        print ("\n👋 Obrigado por jogar! Até a próxima!")
        break
    limpar_tela()

     

