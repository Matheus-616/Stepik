'''Faça um programa que leia dois pontos em R3 \mathbb{R}^3 R3 e calcule a norma ℓ1 \ell_1 ℓ1​ e ℓ2 \ell_2 ℓ2​entre esses pontos.

A norma ℓ1  \ell_1  ℓ1​ também é conhecida como distância Manhattan, ou métrica do táxi: Wikipedia.

A norma ℓ2  \ell_2  ℓ2​ também é conhecida como norma ou distância Euclidiana: Wikipedia.'''

import math as mt
x1, y1, z1 = (float(i) for i in input().split())
x2, y2, z2 = (float(i) for i in input().split())
d1 = abs(x2-x1)+abs(y2-y1)+abs(z2-z1)
d2 = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**(1/2)
print('%.2f %.2f'%(d1,d2))
