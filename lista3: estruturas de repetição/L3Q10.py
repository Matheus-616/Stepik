#Dados o centro (x,y,z) (x, y, z) (x,y,z) e o raio R R R de uma esfera, calcule a quantidade N N N de coordenadas inteiras (xi,yi,zi) (x_i, y_i, z_i) (xi​,yi​,zi​) - onde os valores de xi x_i xi​, yi y_i yi​ e zi z_i zi​ são números inteiros - que ocorrem no interior (incluindo superfície) da esfera.

xe, ye, ze, r = input().split()
r = int(r)
c = 0
for i in range(-r,r+1):
    for j in range(-r,r+1):
        for k in range(-r,r+1):
            if (i**2+j**2+k**2) <= r**2:
                c += 1
print(c)
