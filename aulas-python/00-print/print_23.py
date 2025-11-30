# 23 - Imprimi um contador regressivo

import time

for i in range(5, -1, -1):
    print(f"Contagem regressiva: {i}", end="\r")
    time.sleep(1)

print("\nFim!")