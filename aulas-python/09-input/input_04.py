# 09 - 04 -  Entrada de múltiplos valores em um mesmo input usando .split()

nome, idade, altura = input("Digite seu nome, idade e altura: ").split("+")

print(f"""
Nome: {nome}
Idade: {idade}
Altura: {altura}
""")