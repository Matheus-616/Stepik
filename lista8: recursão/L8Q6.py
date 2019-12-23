'''

[1 ponto] Escreva uma função soma_list_rec que recebe uma lista e retorna a soma os valores, feita de forma recursiva. Os valores da lista podem ser números inteiros e/ou outras listas do mesmo tipo.

    Se um valor na lista é inteiro, adicione-o à soma;
    Se um valor na lista é outra lista, some os valores dessa lista recursivamente e adicione o resultado à soma.

Cabeçalho da função:

def soma_lista_rec(L):


Não se preocupe com a chamada das funções, ou impressão dos resultados, isso será feito automaticamente.  
Escreva apenas as funções solicitadas.

'''

def soma_lista_rec(L):
    soma = 0
    for i in range(len(L)):
        if type(L[i]) == int:
            soma += L[i]
        else: 
            soma += soma_lista_rec(L[i])
    return soma
