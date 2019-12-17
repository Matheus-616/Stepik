#Faça um programa para listar todos os divisores de um número n≥2 ou dizer que o número é primo caso não existam divisores além de 1 e n. 

n = int(input())
c = 0
lista = []
for i in range(2,n):
	if 0 == n%i:
		lista.append(i)
		c += 1
if c == 0:
	print('primo')
else:
	for i in lista:
		print(i)
