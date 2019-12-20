#Escreva um programa que receba um vetor com n n n valores reais e calcule a soma e multiplicação prefixas dos valores do vetor. A saída deve exibir o valor da soma e multiplicação prefixas para cada índice.

vetor = [float(i) for i in input().split()]
for i in range(len(vetor)):
    s = 0
    p = 1
    for k in range(i+1):
        s += vetor[k]
        p *= vetor[k]
    print('%.2f %.2f' % (s, p))
