'''
Escreva um programa que receba um vetor com n n n valores inteiros entre 0 0 0 e 20 20 20, com possíveis repetições e imprima os números repetidos e quantas vezes aparecem. Ordene a saída pelos valores repetidos e ignore aqueles que aparecem apenas 1 1 1 vez. Caso não hajam repetições a saída do programa deve ser vazia.

'''

vetor = [float(i) for i in input().split()]
lista = []
c = 0
for i in range(len(vetor)):
    if vetor[i] not in lista:               
        for k in range(len(vetor)):
            if k != i and vetor[i] == vetor[k]:
                lista.append(vetor[i])
lista.sort()
vetor = []
aux = []
for i in range(len(lista)):
    if lista[i] not in vetor:
        vetor.append(lista[i])
        for k in range(len(lista)):
            if lista[k] == lista[i]:
                c += 1
        c+=1
        aux.append(c)
        c = 0
for i in range(0,len(vetor)):
        print("%d %d" %(vetor[i], aux[i]))
