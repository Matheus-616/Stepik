#Faça um programa que receba um número inteiro e exiba uma mensagem indicando se este número é par ou ímpar, se é positivo ou negativo, ou se é zero.

n = int(input())
p = n%2
if p == 0:
 print('Par')
else:
 print('Impar')
if n < 0:
 print('Negativo')
elif n == 0:
 print('Zero')
else:
 print('Positivo') 
