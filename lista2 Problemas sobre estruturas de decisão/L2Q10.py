#Dados os comprimentos dos lados AB e BC e sabendo-se que se trata de um triangulo retangulo com o angulo reto em B, calcule o valor em graus do angulo marcado na figura abaixo: (Fiquei com preguiça de adicionar a figura)

import math as mt
AB = float(input())/2
BC = float(input())/2
ang = round(mt.degrees((mt.atan(AB/BC))))
print(ang)
