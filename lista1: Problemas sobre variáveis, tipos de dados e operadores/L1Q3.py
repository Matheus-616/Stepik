#(Questão 3) Faça um programa que dada a expressão algébrica de uma equação do segundo grau, troque x x x por y y y e
vice versa. :

entrada = input()
entrada = entrada.replace('y','a')
entrada = entrada.replace('x','y')
entrada = entrada.replace('a','x')
print(entrada)

