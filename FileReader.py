__author__ = 'Ludus'

import re
file = open('READ THIS PLS.txt', 'r')
DEFINE_ID = 'Identificador'
DEFINE_NUM = 'Numero'
DEFINE_RES = 'Reservada'
DEFINE_OPLOG = 'Operador Logico'
DEFINE_OPMAT = 'Operador Matematico'
DEFINE_OUTRO = 'Outros'


ws = '[\t\n]'
letra = '[a-zA-z]'
digito = '[0-9]'
nome_variavel = '^[_]' + letra + '|' + digito + '+$'
valor_inteiro = digito + '+'
valor_real = '[' + valor_inteiro + ']+[.][' + valor_inteiro + ']+'
operador_mat = '[*+-/]'
operador_log = '[">""<"">=""<=""=="]'

words = []
tokens = []

for linha in file:
    words += linha.split()
index = 0

for i in words:
    index += 1
    if re.match(ws, i):
        print()
    elif re.match(nome_variavel, i):
        print('token ' + DEFINE_ID + ' #' + str(index) + ': ' + i)
    elif re.match(valor_inteiro, i):
        print('token ' + DEFINE_NUM + ' #' + str(index) + ': ' + i)
    elif re.match(valor_real, i):
        print('token ' + DEFINE_NUM + ' #' + str(index) + ': ' + i)
    elif re.match(operador_mat, i):
        print('token ' + DEFINE_OPMAT + ' #' + str(index) + ': ' + i)
    elif re.match(operador_log, i):
        print('token ' + DEFINE_OPLOG + ' #' + str(index) + ': ' + i)
    else:
        print('token ' + DEFINE_OUTRO + ' #' + str(index) + ': ' + i)