#Escreva um programa que nos mostre o maior e o menor número dentre 5 números reais fornecidos.

lista = [float(i) for i in input().split()]
for i in range(len(lista)):
 if i == 0:
  M = lista[0]
  m = lista[0]
 if M < lista[i]:
  M = lista[i]
 if m > lista[i]:
  m = lista[i]
print('%.2f %.2f' %(M, m))
