'''

[1 ponto] Escreva uma função caixa_eletronico que dado um valor em Reais, retorne um dicionário contendo o valor e quantidade de cada cédula para realizar um saque com o menor número possível de cédulas.

Considere que o caixa tem um número infinito das cédulas de 100, 50, 20, 10, 5 e 2.

Cabeçalhos da função:

def caixa_eletronico(valor):

Não se preocupe com a leitura dos dados, chamada da função, ou impressão dos resultados, isso já está feito no template.
Escreva apenas as funções solicitadas.

'''

def caixa_eletronico(valor):
        dic = {}
        a = 0
    #if valor%2 == 0 or (valor%10 != 3 and valor%10 != 1) :
        if valor%10 == 1:
            valor -= 2
            a = 1
        if valor%10 == 3:
            valor -= 4
            a = 2
        if valor // 100 !=0:
            dic[100] = valor//100
        valor %= 100
        if valor // 50 !=0 and valor >53:
            dic[50] = valor//50
        valor %= 50
        if valor // 20 !=0:
            dic[20] = valor//20
        valor %= 20
        if valor // 10 !=0:
            dic[10] = valor//10
        valor %= 10
        for i in range(3):     
            if valor%10 == (5 + 2*i):
                dic[5] = 1
                if i != 0:
                    dic[2] = i
        if valor // 2 !=0 and valor%10 != 7 and valor%10 != 5 and valor%10 != 9:
            dic[2] = valor//2
        if a == 1:
            dic[2] = dic[2] + 1
        if a == 2:
            dic[2] = dic[2] + 2
        return dic
