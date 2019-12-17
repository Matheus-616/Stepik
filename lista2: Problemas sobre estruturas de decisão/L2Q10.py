#Dados os comprimentos dos lados AB e BC e sabendo-se que se trata de um triangulo retangulo com o angulo reto em B, calcule o valor em graus do angulo marcado na figura abaixo: (A figura está na pasta sobre o título Figura_Q10.png)
#O angulo deve ser aproximado para o inteiro mais proximo (0 se < 0.5, 1 caso contrario).
import math as mt
AB = float(input())/2
BC = float(input())/2
ang = round(mt.degrees((mt.atan(AB/BC))))
print(ang)
