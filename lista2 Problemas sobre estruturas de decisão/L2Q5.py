#Escreva um programa que recebe como entrada a data de nascimento do usuário, e informa qual o seu signo.

d, m = input().split('/')
d = int(d)
if (m == '01' and d >= 19) or (m == '02' and d < 16):
	print('Capricórnio')
if (m == '02' and d >= 16) or (m == '03' and d < 12):
	print('Aquário')  
if (m == '03' and d >= 12) or (m == '04' and d < 19):
	print('Peixes')  
if (m == '04' and d >= 19) or (m == '05' and d < 14):
	print('Áries')  
if (m == '05' and d >= 14) or (m == '06' and d < 20):
	print('Touro')  
if (m == '06' and d >= 20) or (m == '07' and d < 21):
 	print('Gêmeos')  
if (m == '07' and d >= 21) or (m == '08' and d < 10):
 	print('Câncer')  
if (m == '08' and d >= 10) or (m == '09' and d < 16):
 	print('Leão')  
if (m == '09' and d >= 16) or (m == '10' and d < 31):
 	print('Virgem')  
if (m == '10' and d >= 31) or (m == '11' and d < 23):
 	print('Libra')  
if (m == '11' and 30 > d >= 23):
 	print('Escorpião')  
if (m == '11' and d >= 30) or (m == '12' and d < 18):
 	print('Serpentário')  
if (m == '12' and d >= 18) or (m == '01' and d < 19):
 	print('Sagitário')  
