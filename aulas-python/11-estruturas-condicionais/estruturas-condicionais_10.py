# 10 - if

nota = 5
resultado = ""

if nota >= 7 and nota <= 10:
  resultado = "Aprovado"

if nota < 7 and nota >= 0:
  resultado = "Reprovado"
  
print(f"Sua nota é {nota} você foi {resultado}")