#Faça um programa que calcule as raízes reais de uma equação do segundo grau f(x)=ax2+bx+c f(x) = ax^2 + bx + c f(x)=ax2+bx+c usando a fórmula de Bhaskara.

import math as mt
a,b, c = input().split()
a, b, c = float(a), float(b), float(c)
Delta = b**2-4*a*c
if Delta < 0 :
 print('No real roots.')
if Delta == 0:
 x1 = -b/(2*a)
 print('%.2f' % x1)
if Delta > 0:
 x1 = (-b+mt.sqrt(Delta))/(2*a)
 x2 = (-b-mt.sqrt(Delta))/(2*a)
 print('%.2f\n%.2f' %(x1,x2) ) 
