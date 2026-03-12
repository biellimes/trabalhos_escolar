alimentacao = 0
transporte = 0
lazer = 0
print("Digite a quantidade de despesas")
qtd = int(input())
for i in range(qtd):
  print("Digite o tipo: 1 - alimentação, 2 - transporte, 3 - lazer")
  tipo = int(input())
  print("Digite o valor da despesa")
  valor = float(input())
  if tipo == 1:
    alimentacao += valor
  elif tipo == 2:
    transporte += valor
  elif tipo == 3:
    lazer += valor
print("O total gasto com alimentação foi:", alimentacao)
print("O total gasto com transporte foi:", transporte)
print("O total gasto com lazer foi:", lazer)
total = alimentacao + transporte + lazer
print("O total gasto no mês foi:", total)