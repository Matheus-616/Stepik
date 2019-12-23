'''

[2 pontos] Faça um programa que gerencie uma agenda de telefones.  O seu programa deve iniciar com uma agenda vazia e ler uma lista de operações a serem realizadas nessa agenda.
As operações são dadas em formas de tuplas:

    ('InserirPessoa', nome): Insere uma entrada na agenda para a pessoa com nome nome, sem telefones. Se a pessoa já existir, ignorar o comando;
    ('InserirTelefone', nome, telefone): Insere um telefone telefone para a pessoa nome. Se a pessoa nome não existir, adicionar a pessoa e o telefone; 
    ('ExcluirTelefone', nome, telefone): Exclui o telefone telefone da pessoa nome. Se a pessoa ou o telefone não existirem, ignorar o comando;
    ('ExcluirPessoa', nome): exclui a pessoa e todos os seus telefones. Se a pessoa não existir, ignorar o comando;
    ('Encerrar',): encerra as  operações.


Ao final imprimir o dicionário diretamente.

Dica: use eval() para converter a string com a tupla do comando para uma tupla de verdade:

comando = eval(input())

'''

comando = [1]
agenda = {}
while comando[0] != 'Encerrar':
    comando = eval(input())
    if comando[0] == 'InserirPessoa' and comando[1] not in agenda:
        agenda[comando[1]] = []
    if comando[0] == 'InserirTelefone':
        if comando[1] not in agenda:
            agenda[comando[1]] = []
        agenda[comando[1]].append(comando[2])
    if (comando[0] == 'ExcluirTelefone') and (comando[1] in agenda):
        if comando[2] in agenda[comando[1]]:
            for i in range(len(agenda[comando[1]])):
                if agenda[comando[1]][i] == comando[2]:
                    del(agenda[comando[1]][i])
                    break
    if comando[0] ==  'ExcluirPessoa' and comando[1] in agenda:
        del agenda[comando[1]]
print(agenda)
