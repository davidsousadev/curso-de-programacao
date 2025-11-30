# 16 - Imprimir um dicionário “bonito” com json.dumps

import json

dados = {"nome": "David", "idade": 29, "curso": "Python"}
print(json.dumps(dados, indent=4, ensure_ascii=False))