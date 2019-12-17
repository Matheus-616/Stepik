#Faça um programa que verifica se um número inteiro positivo 0<N<10⁹, na base 10, é um número de Armstrong. Imprima True ou False para respostas verdadeiras e falsas, respectivamente.

N = input()
for d in range(1, 10):
    soma = 0
    for i in N:
            i = int(i)
            soma += i**d
           # print(soma)
           # print('a%d'%i)
            if i == int(N[-1]) and soma == int(N):
                print('True')
                soma = 0
                break
    if soma == 0:
        break  
if soma != 0:
    print('False')
