'''(Questão 6) Faça um programa que leia:

    O nome de um produto;
    A quantidade comprada;
    O valor unitário;
    E o percentual de desconto a ser aplicado para o pagamento.

Imprima na tela o nome do produto e o valor total da venda.    :'''

produto = input()
quantidade = float(input())
valor_un = float(input())
desconto = float(input())
total = (valor_un*quantidade)*(1-desconto/100)
print("%s: R$ %.2f" % (produto, total))
