'''

[1 ponto] Escreva uma função print_dict_rec que recebe um dicionário e imprime o seu conteúdo de forma tabulada e hierárquica.

 

 

    Se um valor no dicionário não é outro dicionário, imprima a chave e o valor de forma direta;
    Se um valor no dicionário é outro dicionário, imprima a chave e os seus conteúdos (também de forma tabulada e hierárquica) adicionando um nível de indentação;
    O primeiro nível de indentação é o nível zero;
    O caractere de tabulação (\t) deve ser usado para espaçar cada nível de indentação: nível 0 = 0 tab, nível 1 = 1 tab, nível n = n tabs .

Cabeçalho da função:

def print_dict_rec(D, level=0):


Não se preocupe com a chamada das funções, ou impressão dos resultados, isso será feito automaticamente.  
Escreva apenas as funções solicitadas.

'''

def print_dict_rec(D, level=0):
    printar = ''
    L = list(D.keys())
    for i in range(len(D)):
        for j in range(level):
                printar += '\t'
        if type(D[L[i]]) != dict:
            printar += '%s: %s\n' %(L[i], D[L[i]])
        elif D[L[i]] == {}:
            printar += '%s: {\n' %L[i]
            for j in range(level):
                printar += '\t'
            printar += '}\n'
        else:
            printar += '%s: {\n' %L[i]
            '''for j in range(level):
                printar += '\t' '''
            printar += str(print_dict_rec(D[L[i]], level+1))
            for j in range(level):
                printar += '\t'
            printar += '}\n'
    if level == 0:
        print(printar)
    return printar
