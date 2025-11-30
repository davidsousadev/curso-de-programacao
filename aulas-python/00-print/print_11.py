# 11 - Imprime o conteúdo de um arquivo exemplo: .txt

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)