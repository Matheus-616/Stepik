#(Questão 7) conversão de horas minutos e segundos para segundos:

h, m, s = input().split(':')
h = float(h)*3600
m = float(m)*60
s = float(s)
T = h+m+s
print("%.d"%T)
