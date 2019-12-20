'''
Faça um programa que preenche um vetor com valores inteiros, fornecidos um por linha atéque seja dado um valor negativo (o valor negativo não deve ser inserido no vetor).
Imprima:

    1. A quantidade de valores maiores do que 5;
    2. A soma dos valores pares que foram armazenados no vetor;
    3. A soma dos valores ímpares que foram armazenados no vetor,
    4. A quantidade total de valores armazenados no vetor;
    5. O vetor, em uma linha;

'''

vetor = [0]
c = 0
sp = 0
si = 0
while int(vetor[-1]) >= 0:
    vetor.append(int(input()))
del(vetor[0])
del(vetor[-1])
for i in range(len(vetor)):
    if vetor[i] > 5:
        c += 1
    if vetor[i]%2 == 0:
        sp += vetor[i]
    else:
        si += vetor[i]
    vetor[i] = str(vetor[i])
print(c)
print(sp)
print(si)
print(len(vetor))
print(' '.join(vetor))
