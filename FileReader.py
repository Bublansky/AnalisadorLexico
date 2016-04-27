__author__ = 'Ludus'

import re
file = open('READ THIS PLS.txt', 'r')
DEFINE_ID = 'Identificador'
DEFINE_NUM = 'Numero'
DEFINE_RES = 'Reservada'
DEFINE_OPLOG = 'Operador Logico'
DEFINE_OPMAT = 'Operador Matematico'
DEFINE_OUTRO = 'Outros'
DEFINE_ENQUANTO = 'enquanto'
DEFINE_FACA = 'faca'
DEFINE_SE = 'se'
DEFINE_ENTAO = 'entao'
DEFINE_SENAO = 'senao'
DEFINE_EM = 'em'
DEFINE_PARA = 'para'
DEFINE_CARACTERE = 'caractere'
DEFINE_INTEIRO = 'inteiro'
DEFINE_FIM = 'fim'
DEFINE_REAL = 'real'
DEFINE_INICIO = 'inicio'



ws = '[\t\n]'
letra = 'a-zA-Z'
digito = '0-9'
nome_variavel = '_' + '['+digito + letra+']+'
valor_inteiro = '['+digito+']' + '+'
valor_real = '['+digito+']' + '+' + '.' + '['+digito+']' + '+'
operador_mat = '[\*\+-/]'
operador_log = '[<>=][=]?'

words = []
tokens = []

for linha in file:
    words += linha.split()
index = 0
print(words)
for i in words:
    index += 1
    if re.fullmatch(nome_variavel, i):
        print('token ' + DEFINE_ID + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(valor_inteiro, i):
        print('token ' + DEFINE_NUM + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(valor_real, i):
        print('token ' + DEFINE_NUM + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(operador_mat, i):
        print('token ' + DEFINE_OPMAT + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(operador_log, i):
        print('token ' + DEFINE_OPLOG + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_ENQUANTO, i):
        print('token ' + DEFINE_ENQUANTO + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_FACA, i):
        print('token ' + DEFINE_FACA + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_SE, i):
        print('token ' + DEFINE_SE + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_ENTAO, i):
        print('token ' + DEFINE_ENTAO + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_SENAO, i):
        print('token ' + DEFINE_SENAO + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_EM, i):
        print('token ' + DEFINE_EM + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_PARA, i):
        print('token ' + DEFINE_PARA + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_CARACTERE, i):
        print('token ' + DEFINE_CARACTERE + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_INTEIRO, i):
        print('token ' + DEFINE_INTEIRO + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_FIM, i):
        print('token ' + DEFINE_FIM + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_REAL, i):
        print('token ' + DEFINE_REAL + ' #' + str(index) + ': ' + i)
    elif re.fullmatch(DEFINE_INICIO, i):
        print('token ' + DEFINE_INICIO + ' #' + str(index) + ': ' + i)
    else:
        print('token ' + DEFINE_OUTRO + ' #' + str(index) + ': ' + i)