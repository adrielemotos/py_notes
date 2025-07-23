import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def contagem_regressiva(segundos):
    while segundos:
        minutos, segundos_restantes = divmod(segundos, 60)
        tempo_formatado = f"{minutos:02d}:{segundos_restantes:02d}"
        print(f"⏳ Tempo restante: {tempo_formatado}",end="\r")
        time.sleep(1)
        segundos -= 1
    print("\n✅ Tempo finalizado!")

def pomodoro_timer(ciclos=4):
    for ciclo in range(1, ciclos + 1):
        limpar_tela()
        print(f"🍅 Pomodoro {ciclo} - Foco por 25 minutos")
        contagem_regressiva(25 * 60) # 25 minutos

        if ciclo < ciclos:
            print("\n☕Pausa curta - 5 minutos")
            contagem_regressiva(5 * 60) #5 minutos
        else:
            print("\n🛌 Pausa longa - 15 minutos")
            contagem_regressiva(15 * 60) # 15 minutos
    
    print("\n🎉 Todos os ciclos concluídos! Bom trabalho!")

# Iniciar o Pomodoro
pomodoro_timer()