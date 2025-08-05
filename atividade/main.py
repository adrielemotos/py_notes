# 1 - Pegar o nome do usuario e comprimenta-lo. Ex: Ola, Michel
# 2 - Pegar a data, mes e ano de nascimento do usuario.
# 3 - Calcular a idade dele, hoje.

from datetime import datetime

nome = input("Qual seu nome? ")
dt = int(input("Qual a data do seu aniversário? "))
mes = int(input("Qual o mês do seu aniversário (apenas números) "))
ano = int(input("qual o ano de nascimento? "))

dt_now = datetime.now().year
idade = dt_now - ano

print("Olá", nome)
print(f"nasceu em {dt}/{mes}/{ano}")
print(idade, "anos")