import time

print("🧠 Pense em um número entre 1 e 500, e eu (computador) vou tentar adivinhar! ")
input ("Pressione Enter quando estiver pronta...")

baixo = 1
alto = 500
tentativas = 0

while True:
    palpite = (baixo + alto) // 2
    tentativas += 1

    print(f"\n🤖 Meu palpite é: {palpite}")
    resposta = input("Está certo (c), muito alto (a) ou muito baixo (b) ?").lower()

    if resposta == 'c':
        print(f"\n🎉 Acertei o número em {tentativas} tentativas!")
        break
    elif resposta == 'a':
        alto = palpite - 1
    elif resposta == 'b':
        baixo = palpite + 1
    else:
        print("❌ Resposta inválida. Use apenas 'c', 'a' ou 'b'.")

    time.sleep(0.5)
