caes = 0
gatos = 0
outros = 0
soma = 0
print("Digite a quantidade de atendimentos")
qtd = int(input())
for i in range(qtd):
  print("Digite o nome do animal")
  nome = input()
  print("Digite o tipo: 1 – Cão, 2 – Gato, 3 – Outro")
  tipo = int(input())
  print("Digite o peso")
  peso = float(input())
  soma += peso
  if tipo == 1:
    caes += 1
  elif tipo == 2:
    gatos += 1
  elif tipo == 3:
    outros += 1
pesoMedio = soma/qtd
print("Quantidade de caes atendidos:", caes)
print("Quantidade de gatos atendidos:", gatos)
print("Quantidade de outros atendidos:", outros)
print("Peso médio dos animais atendidos:", pesoMedio)