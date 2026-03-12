soma = 0
print("Digite 3 notas")
for i in range(3):
  nota = float(input())
  soma = soma + nota
media = soma/3
print("A média é:", media)
if media >= 7:
  print("Aprovado")
elif media >= 5:
  print("Recuperacao")
else:
  print("Reprovado")