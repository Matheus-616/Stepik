#(Questão 10) Seguindo a ideia da decolagem de um avião inicialmente em repouso. Faça um programa que dada a velocidade mínima para decolagem v v v em m/s m/s m/s e o comprimento da pista d d d em metros, calcule a aceleração constante necessária para que a decolagem seja bem sucedida.:

v, d = input().split()
v, d = float(v), float(d)
a = (v**2)/(2*d)
t = v/a
print("%.2f %.2f" % (a,t))
