#Faça um programa que dado um ano a a a, a≥1600 a \geq 1600 a≥1600, imprima se a a a é um ano bissexto ou comum. 

x = int(input())
if (0 == x%4 and 0 != x%100) or 0 == x%400:    
    print('bissexto')
else:
    print('comum')
