print("Digite sua idade")
idade = int(input())
if idade <= 10:
  print("Infantil")
elif idade >= 11 and idade <= 14:
  print("Juvenil")
elif idade >= 15 and idade <= 18:
  print("Junior")
else:
  print("Senior")