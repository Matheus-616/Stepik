#Faça um programa que imprima a tabuada de multiplicação de um número inteiro positivo n n n fornecido. 

n = int(input())

for i in range(1,11):
    print("%.d * %.d = %.d" %(n,i,n*i))
