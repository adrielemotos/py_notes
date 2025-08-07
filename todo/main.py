import os

ARQUIVO_TAREFAS = "tarefas.txt"
tarefas = []

# Carregar tarefas do arquivo
def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, concluida = linha.strip().split("|")
                tarefas.append({"nome": nome, "concluida": concluida == "True"})

# Salvar tarefas no arquivo
def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            linha = f"{tarefa['nome']}|{tarefa['concluida']}\n"
            arquivo.write(linha)

# Mostrar menu
def mostrar_menu():
    print("\n--- Lista de Tarefas ---")
    print("1. Ver tarefas")
    print("2. Adicionar tarefas")
    print("3. Marcar tarefas como concluídas")
    print("4. Remover tarefa")
    print("5. Sair")

# Ver tarefas
def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada 👎")
    else: 
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            status = "🟢" if tarefa["concluida"] else "🔴"
            print(f"{i + 1}. {tarefa['nome']} [{status}]")

# Adicionar tarefas
def adicionar_tarefa():
    print("Digite uma tarefa por linha. Digite 'fim' para encerrar.")
    while True:
        nome = input("Tarefa: ")
        if nome.lower() == "fim":
            break
        if nome.strip():
            nova_tarefa = {"nome": nome, "concluida": False}
            tarefas.append(nova_tarefa)
    salvar_tarefas()
    print("Tarefa(s) adicionada(s) 😎")

# Marcar múltiplas tarefas como concluídas
def marcar_concluida():
    ver_tarefas()
    entrada = input("Digite os números das tarefas concluídas (separadas por vírgula): ")
    numeros = entrada.split(",")

    marcou_algo = False
    for num_str in numeros:
        num_str = num_str.strip()
        if num_str.isdigit():
            num = int(num_str) - 1
            if 0 <= num < len(tarefas):
                tarefas[num]["concluida"] = True
                print(f"Tarefa {num + 1} marcada como concluída 😎")
                marcou_algo = True
            else:
                print(f"Número {num + 1} inválido 👎")
        else:
            print(f"'{num_str}' não é um número válido 😉")

    if marcou_algo:
        salvar_tarefas()

# Remover tarefa
def remover_tarefas():
    ver_tarefas()
    try:
        num = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas.pop(num)
            salvar_tarefas()
            print("Tarefa removida 😵") 
        else:
            print("Número inválido 👎")
    except ValueError:
        print("Digite um número válido 😉")

# Programa principal
carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        ver_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        remover_tarefas()
    elif opcao == "5":
        print("Saindo... Até mais ✌️")
        break
    else:
        print("Opção inválida. Tente novamente.")