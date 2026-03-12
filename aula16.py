animacao = 0
acao = 0
comedia = 0
print("Digite a quantidade de votos")
qtd = int(input())
for i in range(qtd):
  print("Escolha a categoria (1 – Animação, 2 – Ação, 3 – Comédia)")
  voto = int(input())
  if voto == 1:
    print("Você votou em animação")
    animacao += 1
  elif voto == 2:
    print("Você votou em ação")
    acao += 1
  elif voto == 3:
    print("Você votou em comédia")
    comedia += 1
print("A quantidade votos para animação foi", animacao)
print("A quantidade votos para ação foi", acao)
print("A quantidade votos para comédia foi", comedia)
if animacao >= acao and animacao >= comedia:
  print("O mais votado foi animação")
elif acao >= animacao and acao >= comedia:
  print("O mais votado foi ação")
elif comedia >= animacao and comedia >= acao:
  print("O mais votado foi comédia")