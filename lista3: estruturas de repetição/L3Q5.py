#Faça um programa que calcule a soma apenas dos números ímpares da sequência de inteiros contida no intervalo [x,y] [x,y] [x,y].

a, b = input().split()
a, b = int(a), int(b)
soma = 0
for i in range (a, b+1):
    if 1 == i%2:
        soma += i
print(soma)
