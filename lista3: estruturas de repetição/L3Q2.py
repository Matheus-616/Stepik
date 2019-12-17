#Faça um programa que dado o limite superior do somatório n n n , calcule uma aproximação de π \pi π usando a fórmula Bailey-Borwein-Plouffe (BBP). 
#Neste problema em específico, use 48 casas decimais.

n = int(input())
F = 0
for i in range(n+1):
    F += (1/16**i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print('%.48f'%F)
