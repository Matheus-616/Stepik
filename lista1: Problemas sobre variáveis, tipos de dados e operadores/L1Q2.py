#(Questão 2) Transforma as letars de uma palavra em minúsculas, exceto a letra 'a' que sempre ocorre três vezes:

pal = input().lower()
saida = ''
for i in range(len(pal)):
 a = pal[i]
 if a == 'a':
  a = 'A'
 saida = saida+a
print(saida)
