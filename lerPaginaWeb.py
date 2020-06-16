# coding: latin-1
# versao python 3
import urllib.request, urllib.error, urllib.parse
import base64

request = urllib.request.Request('http://www.ismai.pt')
result = urllib.request.urlopen(request)
listaLinhas = result.readlines()
frase = 'ISMAI Instituto'
totalPalavra = 0


for indiceLinha in range(len(listaLinhas)):
    umaLinha = listaLinhas[indiceLinha]
    if umaLinha.find(frase.encode()) != -1:
        totalPalavra = totalPalavra + 1
        print('Encontrado na linha {}' .format(indiceLinha))


print('Encontrados {} palavras {}' .format(totalPalavra, frase))



