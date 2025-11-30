# 13 - Impressão formatada tipo tabela

dados = [
    {"Nome": "David", "Idade": 29}
]

print(f"{'Nome':<10} {'Idade':^5}")
print("-"*16)

for p in dados:
    print(f"{p['Nome']:<10} {p['Idade']:^5}")