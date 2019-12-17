#Faça um programa que verifica se um número inteiro positivo 0<N≤100 é um número perfeito (True como saída) ou não (False como saída). 

N = input()
N = int(N)
c = 0
for i in range(1, int(N/2)+1):
	if 0 == N%i:
		c += i
print(c == N)
