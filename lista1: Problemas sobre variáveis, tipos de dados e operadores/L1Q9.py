#(Questão 9)Faça um programa que, dada uma aceleração constante em m/s2 m/s^2 m/s2 e o tempo de aceleração em segundos, calcule a distância em metros percorrida em uma pista para que um avião em repouso decole.:

a, t = input().split()
a, t = float(a),float(t)
d = (a/2)*t**2
print("%.2f" % d)
