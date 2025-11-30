# 25 - Imprime a hora como um relógio 
import time
for i in range(5):
    print(time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)
print(time.strftime("%H:%M:%S"))
    