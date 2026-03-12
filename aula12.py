alimento = 0
bebida = 0
limpeza = 0
print("Digite a quantidade de vendas feitas no dia")
qtd = int(input())
for i in range(qtd):
  print("Digite o codigo do produto vendido")
  print("1 - Alimento, 2 - Bebida, 3 - Produto de limpeza")
  codigo = int(input())
  print("Digite a quantidade vendida")
  qtdVendida = int(input())
  if codigo == 1:
    alimento += qtdVendida
  elif codigo == 2:
    bebida += qtdVendida
  elif codigo == 3:
    limpeza += qtdVendida
print("A quantidade de alimentos vendidos foi", alimento)
print("A quantidade de bebidas vendidas foi", bebida)
print("A quantidade de produtos de limpeza vendidos foi", limpeza)
total = alimento + bebida + limpeza
print("O total de produtos vendidos foi", total)