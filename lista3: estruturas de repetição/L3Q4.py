'''
Faça um programa que imprima os horários de um ônibus, sabendo que ele passa a cada t t t minutos e que as linhas começam a funcionar às 5:00 (primeiro horário) e param às 23:55 (último horário possível).

Para imprimir as horas e minutos sempre com 2 dígitos, incluindo zeros à esquerda, utilize o comando:

print('%02d:%02d' % (horas, minutos))

'''

t = int(input())
horas = 5
minutos = 0
while horas < 24 and ( horas < 23 or minutos <= 55):
    print('%02d:%02d'%(horas, minutos))
    minutos += t
    while minutos >= 60:
        horas += 1
        minutos -= 60 
