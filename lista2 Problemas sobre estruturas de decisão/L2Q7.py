#Faça um programa que receba como entrada o comprimento do pêndulo e calcule o seu período.

import math as mt
g = 9.8
l = float(input())
t = 2*mt.pi*(l/g)**(1/2)
print('%.2f' %t)
