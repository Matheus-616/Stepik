#Dado um inteiro positivo 0<n<10000 , faça um programa que calcula a seguinte soma 

n = int(input())
S = 0
for i in range(1,n+1):
    S += i/(n+1-i)
print('%.48f' % S)
