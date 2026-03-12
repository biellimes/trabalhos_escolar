print("Digite o valor do litro da gasolina")
gasolina = float(input())
print("Digite o valor do litro do etanol")
etanol = float(input())
if etanol <= gasolina * 0.7:
  print("Melhor abastecer com etanol")
else:
  print("Melhor abastecer com gasolina")