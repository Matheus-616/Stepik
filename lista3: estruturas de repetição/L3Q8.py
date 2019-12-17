#Faça um programa que calcule o MMC (mínimo múltiplo comum) entre dois números.

a, b = input().split()
a, b = int(a), int(b)
a, b = max(a,b), min(a,b)
for i in range (1,b+1):
    if 0 == (a*i)%b:
        m = a*i
        break
print(m)
