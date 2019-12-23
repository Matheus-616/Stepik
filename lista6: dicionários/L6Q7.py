'''

[1 ponto] Escreva um programa que conte quantas palavras diferentes, quantas palavras repetidas e quantas frases existem em um texto.

Uma frase é delimitada por um ponto final, ponto de exclamação ou ponto de interrogação.

Para palavras repetidas, considerar o número de repetições. Uma palavra que aparece:

    1 vez é considerada repetida 0 vezes;
    2 vezes é considerada repetida 1 vez;
    3 vezes é considerada repetida 2 vezes;
    4 vezes é considerada repetida 3 vezes;
    E assim sucessivamente.

'''

frase = input().split()
nf = 0
dif = []
rep = []
for i in range(len(frase)):
    frase[i] = [j for j in frase[i]]
    if '.' in frase[i] or '!' in frase[i] or '?' in frase[i] or ',' in frase[i]:
        if ',' not in frase[i]:
            nf += 1
        del frase[i][-1]
    frase[i] = ' '.join(frase[i]).lower()
    if frase[i] not in dif:
        dif.append(frase[i])
    elif frase[i] not in rep:
        rep.append(frase[i])
print(len(dif), len(rep), nf)
