# coding: latin-1
# versao python 3
import urllib.request, urllib.error, urllib.parse, base64

request = urllib.request.Request('http://www.ismai.pt')
result = urllib.request.urlopen(request)
lista = result.read()
listaLinhasDecod = lista.decode()
listaDelinhas = listaLinhasDecod.split('\n')
frase1 = ('ISMAI').lower()
frase2 = ('Instituto').lower()



for indiceLinha in range(len(listaDelinhas)):
    umaLinha = (listaDelinhas[indiceLinha])
    umalinhaFormatada = umaLinha.lower()
    if (umalinhaFormatada.find(frase1) != -1) and (umalinhaFormatada.find(frase2) != -1):
        print('{}' .format(umaLinha))






