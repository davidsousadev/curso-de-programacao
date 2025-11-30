# 14 - Imprimir com flush para atualização imediata na tela

import time

for i in range(101):
    print(f"Carregando {i}/100%", end="\r", flush=False)
    time.sleep(0.05)
print()

largura = 30

for progresso in range(101):
    preenchido = int((progresso / 100) * largura)
    vazio = largura - preenchido
    barra = "[" + "#" * preenchido + "-" * vazio + f"] {progresso:3d}%"
    
    print(barra, end="\r")
    time.sleep(0.03)

print()