def faixa_etaria(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "idoso"

# Lista para armazenar cadastros
cadastros = []

# Cadastros de 5 pessoas
for i in range(3):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")

    faixa = faixa_etaria(idade)

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade, 
        "faixa_etaria": faixa
    }

    cadastros.append(pessoa)

# Salvar em arquivo
with open("cadastros.txt", "w") as arquivo:
    for p in cadastros:
        linha = f"{p['nome']}, {p['idade']} anos, {p['cidade']} - {p['faixa_etaria']}\n"
        arquivo.write(linha)
print("\nCadastros salvos com sucesso! Confira abaixo:\n")


# Mostrar o conteúdo do arquivo
with open("cadastros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

