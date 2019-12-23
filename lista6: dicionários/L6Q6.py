'''

[1 ponto] Escreva um programa que decodifique mensagens encriptadas. Neste problema, as mensagens serao encriptadas atraves da permutacao das letras no alfabeto, cada letra sera associada a alguma outra letra do alfabeto (incluindo ela mesma). No exemplo abaixo,  associamos cada letra com a terceira letra a sua frente.

Produzindo o seguinte alfabeto criptografado:
Normal:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cifrado: DEFGHIJKLMNOPQRSTUVWXYZABC

Assim, se decodificassemos a seguinte mensagem 'R SURIHVVRU HVWD ROKDQGR.', seguindo a codificacao acima, chegariamos a mensagem:
'O PROFESSOR ESTA OLHANDO.'

A primeira linha da entrada do problema representa o alfabeto cifrado. A primeira letra se refere a letra 'A', a segunda a letra 'B' e assim por diante, como descrito no exemplo.
A segunda linha representa uma mensagem codificada. 

Todos alfabetos e palavras estarao sempre em letras maiusculas, assim como devem ser as respostas. Atencao aos espacos em branco, pontos finais e virgulas.

Imprima a mensagem decodificada.

'''


cod = input()
dic = {cod[0]:'A', cod[1]:'B', cod[2]:'C', cod[3]:'D', cod[4]:'E', cod[5]:'F', cod[6]:'G', cod[7]:'H', cod[8]:'I', cod[9]:'J', cod[10]:'K', cod[11]:'L', cod[12]:'M', cod[13]:'N', cod[14]:'O', cod[15]:'P', cod[16]:'Q', cod[17]:'R', cod[18]:'S', cod[19]:'T', cod[20]:'U', cod[21]:'V', cod[22]:'W', cod[23]:'X', cod[24]:'Y', cod[25]:'Z', '.':'.', ',':',', ' ':' '}
frase = input()
st = ''
for i in frase:
    st += dic[i]
print(st)
