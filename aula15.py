carros = 0
motos = 0
caminhoes = 0
print("Digite a quantidade de veículos que entraram no estacionamento")
qtd = int(input())
for i in range(qtd):
  print("Digite o tipo do veículo (1 – Carro, 2 – Moto, 3 – Caminhão)")
  tipo = int(input())
  if tipo == 1:
    carros += 1
  elif tipo == 2:
    motos += 1
  elif tipo == 3:
    caminhoes += 1
print("A quantidade de carros foi", carros)
print("A quantidade de motos foi", motos)
print("A quantidade de caminhões foi", caminhoes)