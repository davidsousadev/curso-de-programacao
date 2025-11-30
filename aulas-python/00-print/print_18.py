# 18 - Imprime uma barra de carregamento simples

import time

for i in range(1, 11):
    print("*" * i, end="\r")
    time.sleep(0.1)

print("Carregado!")