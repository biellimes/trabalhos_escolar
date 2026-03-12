print("Digite 3 notas")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3)/3
print("A média é:", media)
if media >= 7:
  print("Aprovado")
elif media >= 5:
  print("Recuperacao")
else:
  print("Reprovado")