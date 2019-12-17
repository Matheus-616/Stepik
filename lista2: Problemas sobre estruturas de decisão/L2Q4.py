#Faça um programa que leia três coordenadas em R2 \mathbb{R}^2 R2 e indique se formam um triângulo, juntamente com o seu tipo: equilátero, isósceles ou escaleno.

x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()
x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
x3, y3 = float(x3), float(y3)
l1 = ((x1-x2)**2+(y1-y2)**2)**(1/2)
l2 = ((x1-x3)**2+(y1-y3)**2)**(1/2)
l3 = ((x2-x3)**2+(y2-y3)**2)**(1/2)
if l1 + l2 == l3 or l1 + l3 == l2 or l2 + l3 == l1:
 	print('não triângulo')
elif l1 == l2 == l3:
 	print('triângulo\nequilátero')
elif l1 != l2 and l1 != l3 and l2 != l3:
 	print('triângulo\nescaleno')
else:
	print('triângulo\nisósceles')

