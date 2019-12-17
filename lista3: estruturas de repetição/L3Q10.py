#Dados o centro (x,y,z) (x, y, z) (x,y,z) e o raio R R R de uma esfera, calcule a quantidade N N N de coordenadas inteiras (xi,yi,zi) (x_i, y_i, z_i) (xi​,yi​,zi​) - onde os valores de xi x_i xi​, yi y_i yi​ e zi z_i zi​ são números inteiros - que ocorrem no interior (incluindo superfície) da esfera.

a, b, c, r = input().split()
a, b, c, r = int(a), int(b), int(c), int(r)

P = [k for k in range(a-r,a+r+1)]
Q = [k for k in range(b-r,b+r+1)]
R = [k for k in range(c-r,c+r+1)]
ç=0
for x in P:
    for y in Q:
        for z in R:
            if (x-a)**2+(y-b)**2+(z-c)**2<=r**2:
                ç+=1
print(ç)
