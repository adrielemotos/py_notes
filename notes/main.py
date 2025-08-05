# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))

# pessoa = {
#     "nome": nome,
#     "idade": idade,
#     "altura": altura
# }

# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")

pessoa = {
    "nome": "Dri",
    "idade": 21,
    "altura": 1.63
}

cidade = input("Digite sua cidade: ")
pessoa["cidade"] = cidade

for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")