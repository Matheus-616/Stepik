'''

[2 pontos] Faça um programa que processe uma sequência de tuplas com origens e destinos de uma companhia aérea, representados pelo código do aeroporto.

O seu programa deve montar um dicionário com os trechos que não possuem volta direta. Nesse dicionário as chaves são a origem, e os valore são listas contendo os destinos que não possuem trecho de volta para a origem.

Uma tupla com apenas uma origem, sem destino indica o final da sequência.

Ao final, imprima o dicionário sem formatação 

'''

comando = (0,0)
dic = {}
aux = []
while 1:
    comando = eval(input())
    if len(comando) == 2:
        aux.append([comando[0],comando[1]])
    else:    
        break
for i in range(len(aux)):
    a = 0
    for j in range(len(aux)):
        if aux[i][1] == aux[j][0] and aux[j][1] == aux[i][0]:
            a = 1
            break
    if a == 0:
        if aux[i][0] in dic:
            if aux[i][1] not in dic[aux[i][0]]:
                dic[aux[i][0]].append(aux[i][1])
        else:
            dic[aux[i][0]] = [aux[i][1]]
print(dic)
