# encoding: utf-8
# procurar.py palavra fich1

import sys
import hashlib

progName = sys.argv[0]

if len(sys.argv) < 3:
   print('Erro, utilizacao:  "{} fich1 texto da linha" ' .format(progName))
   print('- procura "palavra" no ficheiro e imprime as linhas com ela')
   sys.exit(1)

umFicheiro = sys.argv[1]
palavra = sys.argv[2]


aPesquisa = hashlib.sha1()
aPesquisa.update(palavra.encode())
resultadoEmBinario = aPesquisa.digest()


resultadoEmTxt = "".join("{:02x}".format(c) for c in resultadoEmBinario)

f = open(umFicheiro, 'r',encoding='UTF-8')
listaLinhas = f.readlines()
f.close()

dict = {}

for indiceLinha in range(len(listaLinhas)):
    umaLinha = listaLinhas[indiceLinha].strip().split()
    chave = umaLinha[0]
    if chave in dict.keys():
        dict[chave].append([[umaLinha[1], umaLinha[2]]])
    else:
        dict[chave] = [[umaLinha[1], umaLinha[2]]]

if resultadoEmTxt in dict.keys():
    print(dict[resultadoEmTxt])
