#Dados os n vértices em sentido anti-horario de um poligono convexo P e m pontos x_i. Escreva um programa que verifica se cada ponto x_i​ se encontra no interior P (incluindo as arestas) ou nao.

lista = [float(i) for i in input().split()]
ps = [float(i) for i in input().split()]
i = 0
poligono = []
while i < len(lista):
    poligono.append([lista[i],lista[i+1]])
    i += 2
pontos = []
i = 0
while i < len(ps):
    pontos.append([ps[i], ps[i+1]])
    i += 2
for i in pontos:
    verifica = True
    for j in range(len(poligono)):
        if j == len(poligono)-1:
            det = (poligono[0][0] * i[1]) + (poligono[j][0] * poligono[0][1]) + (poligono[j][1] * i[0]) - (poligono[j][1] * poligono[0][0]) - (poligono[0][1] * i[0]) - (i[1] * poligono[j][0])
            if (det) < 0:
                verifica = False
                break
        else:
            det = (poligono[j+1][0] * i[1]) + (poligono[j][0] * poligono[j+1][1]) + (poligono[j][1] * i[0]) - (poligono[j][1] * poligono[j+1][0]) - (poligono[j+1][1] * i[0]) - (i[1] * poligono[j][0])
            if det < 0:
                verifica = False
                break
    if verifica:
        print('S')
    else:
        print('N')


