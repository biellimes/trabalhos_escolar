genericos = 0
referencia = 0
manipulados = 0
print("Digite o numero de vendas realizadas no dia")
qtd = int(input())
for i in range(qtd):
  print("Digite o código do tipo do remédio vendido")
  print("1 - genérico, 2 - referência, 3 - manipulado")
  tipo = int(input())
  print("Digite a quantidade vendida")
  qtdVendida = int(input())
  if tipo == 1:
    genericos += qtdVendida
  elif tipo == 2:
    referencia += qtdVendida
  elif tipo == 3:
    manipulados += qtdVendida
print("Foram vendidos", genericos, "medicamentos genéricos")
print("Foram vendidos", referencia, "medicamentos referência")
print("Foram vendidos", manipulados, "medicamentos manipulados")
total = genericos + referencia + manipulados
print("O total de medicamentos vendidos foi", total)