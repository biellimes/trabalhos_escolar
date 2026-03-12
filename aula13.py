somaNotas = 0
nota5 = 0
nota1 = 0
print("Digite a quantidade de entrevistas que serão feitas")
qtd = int(input())
for i in range(qtd):
  print("Digite a nota dada ao atendimento")
  nota = int(input())
  if nota == 5:
    nota5 += 1
  elif nota == 1:
    nota1 += 1
  somaNotas += nota
mediaNotas = somaNotas / qtd
print("A média das notas foi", mediaNotas)
print("A quantidade de pessoas que deu nota 5 foi", nota5)
print("A quantidade de pessoas que deu nota 1 foi", nota1)