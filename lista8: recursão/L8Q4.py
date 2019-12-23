'''

[1 ponto] Assuma que f(n) denote a soma dos dígitos de n. É fácil perceber que se a sequencia de números f(n),f(f(n)),f(f(f(n))),... vai eventualmente se tornar um único numero que se repete infinitamente.

Por exemplo, para n=1234567892 
	f(n)=1+2+3+4+5+6+7+8+9+2=47
 	f(f(n))=4+7=11 
 	f(f(f(n)))=1+1=2 
 	f(f(f(f(n))))=2 ... 
Note que apos chegar em 2 jamais teremos outro numero na sequencia. Assuma agora que g(n) representa este único dígito que surge e se repete infinitamente na sequencia, então g(1234567892)=2.

Escreva  g(n).

Cabeçalho da função:

def g(N):


Não se preocupe com a chamada das funções, ou impressão dos resultados, isso será feito automaticamente.  
Escreva apenas as funções solicitadas.


'''

def g(N):
    if 0<=N<=9:
        return N
    else:
        N = str(N)
        soma = 0
        for i in range(len(N)):
            soma += int(N[i])
        return g(soma)
