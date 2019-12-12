#(Questão 1) Dado um número x, 1000<=x<=10000, impria x com os números na ordem inversa: 

num = input()
num1 = ''
for i in range(len(num)):
 a = num[-i-1]
 num1 = num1+a  
print(num1)
