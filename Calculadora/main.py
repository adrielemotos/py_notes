def somar(a, b):
    return a + b

def subtrair(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a,b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a/b

def porcentagem(a, b):
    return(a/100) *b

print("Calculadora no Terminal")

while True:
    print("\nEscolha a operação ou digite 'sair' para encerrar:")
    print("1-Somar")
    print("2-Subtrair")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Porcentagem")

    opcao = input("Digite a opção (1,2,3,4,5) ou 'sair': ").lower()

    if opcao == "sair":
        print("Encerrando a calculadora. Até logo!")
        break

    try:
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))
    except ValueError:
        print("Erro: Digite apenas números válidos.")
        continue

    if opcao == "1":
        resultado = somar(num1, num2)
    elif opcao == "2":
        resultado = subtrair(num1, num2)
    elif opcao == "3":
        resultado = multiplicar(num1, num2)
    elif opcao == "4":
        resultado = dividir(num1, num2)
    elif opcao == "5":
        resultado = porcentagem(num1, num2)
    else:
        resultado = "opção inválida."

    print("Resultado", resultado)