def converter_reias_para_dolar(valor):
    taxa = 0.19 #1 real = 0.19 dólar
    return valor * taxa

def converter_reais_para_euro(valor):
    taxa = 0.18 #1 real = 0.18 euro
    return valor * taxa 

def converter_reais_para_peso(valor):
    taxa = 36.5 # 1 real = 36.5 pesos argentinos
    return valor * taxa

print("=== Conversor de Moedas===")

while True:
    print("\nEscolha a moeda para conversao:")
    print("1 - dólar")
    print("2 - euro")
    print("3 - peso argentino")
    print("Digite 'sair' para encerrar.")

    escolha = input("opção: ").lower()

    if escolha == 'sair':
        print("Encerrando o conversor. Até logo!")
        break

    try:
        valor_em_reais = float(input("Digite o valor em reais: R$"))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        continue

    if escolha == '1':
        convertido = converter_reias_para_dolar(valor_em_reais)
        print(f"US$ {convertido:.2f}")
    elif escolha == '2':
        convertido = converter_reais_para_euro(valor_em_reais)
        print(f"€ {convertido:.2f}")
    elif escolha == '3':
        convertido = converter_reais_para_peso(valor_em_reais)
        print(f"${convertido:.2f})(pesos argentinos)")
    else:
        print("Opção inválida. Tente novamente.")

    
        
