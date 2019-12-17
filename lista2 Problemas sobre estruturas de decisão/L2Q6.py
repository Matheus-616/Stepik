#Faça um programa que simule uma calculadora usando a notação polonesa reversa (Wikipedia). 

a, b, op = input().split()
a,b = float(a), float(b)
if op == '+':
    print('%.2f' % (a + b))
if op == '-': 
    print('%.2f' % (a - b))
if op == '/':
    print('%.2f' % (a/b))
if op == '*':    
    print('%.2f' % (a*b))
