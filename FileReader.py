__author__ = 'Ludus'

import re
file = open('READ THIS PLS.txt', 'r')
arquivo = open('Tabela de Tokens.txt', 'w')
arquivo2 = open ('Tabela de Simbolos.txt', 'w')
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
comentario = '[^//]'
nome_variavel = '_' + '['+digito + letra+']+'
valor_inteiro = '['+digito+']' + '+'
valor_real = '['+digito+']' + '+' + '.' + '['+digito+']' + '+'
operador_mat = '[\*\+-/]'
operador_log = '[<>=][=]?'
tab = '\t\t\t\t\t'

words = []
tokens = []
lista = []
flag = False

for linha in file:
    if re.match(comentario, linha):
        words += linha.split()
index = 0
cont = 0
for i in words:
    index += 1
    if re.fullmatch(nome_variavel, i):
        for j in lista:
            if i == j:
               flag = True
        if not flag:
            lista.insert(len(lista),i)
        for k in range(0,len(lista)):
            if i == lista[k]:
                cont = k+1
        flag = False
        arquivo.writelines(i + tab + DEFINE_ID + '\n')
        cont = 0
    elif re.fullmatch(valor_inteiro, i):
        arquivo.writelines(i + tab + DEFINE_NUM + '\n')
    elif re.fullmatch(valor_real, i):
        arquivo.writelines(i + tab + DEFINE_NUM + '\n')
    elif re.fullmatch(operador_mat, i):
        arquivo.writelines(i + tab + DEFINE_OPMAT + '\n')
    elif re.fullmatch(operador_log, i):
        arquivo.writelines(i + tab + DEFINE_OPLOG + '\n')
    elif re.fullmatch(DEFINE_ENQUANTO, i):
        arquivo.writelines(i + tab + DEFINE_ENQUANTO+ '\n')
    elif re.fullmatch(DEFINE_FACA, i):
        arquivo.writelines(i + tab + DEFINE_FACA + '\n')
    elif re.fullmatch(DEFINE_SE, i):
        arquivo.writelines(i + tab + DEFINE_SE + '\n')
    elif re.fullmatch(DEFINE_ENTAO, i):
        arquivo.writelines(i + tab + DEFINE_ENTAO + '\n')
    elif re.fullmatch(DEFINE_SENAO, i):
        arquivo.writelines(i + tab + DEFINE_SENAO + '\n')
    elif re.fullmatch(DEFINE_EM, i):
        arquivo.writelines(i + tab + DEFINE_EM + '\n')
    elif re.fullmatch(DEFINE_PARA, i):
        arquivo.writelines(i + tab + DEFINE_PARA + '\n')
    elif re.fullmatch(DEFINE_CARACTERE, i):
        arquivo.writelines(i + tab + DEFINE_CARACTERE + '\n')
    elif re.fullmatch(DEFINE_INTEIRO, i):
        arquivo.writelines(i + tab + DEFINE_INTEIRO + '\n')
    elif re.fullmatch(DEFINE_FIM, i):
        arquivo.writelines(i + tab + DEFINE_FIM + '\n')
    elif re.fullmatch(DEFINE_REAL, i):
        arquivo.writelines(i + tab + DEFINE_REAL + '\n')
    elif re.fullmatch(DEFINE_INICIO, i):
        arquivo.writelines(i + tab + DEFINE_INICIO + '\n')
    else:
        print(i + tab + 'Erro Sintaxe nao Aceita' + '\n')

for k in range(0,len(lista)):
    arquivo2.writelines(lista[k]+ tab + str(k+1) + '\n')
arquivo2.close()
arquivo.close()