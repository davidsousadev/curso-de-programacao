# 22 - Imprimi uma mini- tabela alinhada

nomes = ["Ana", "Bruno", "Clara"]
idades = [23, 34, 29]

print("Nome      Idade")
for n, i in zip(nomes, idades):
    print(f"{n:<10}{i:>5}")


