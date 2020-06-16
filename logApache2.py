# coding: latin-1
# versao python 3
import urllib.request, urllib.error, urllib.parse, base64

request = urllib.request.Request('https://dev1.portodigital.pt/avs/log/lixo.log')
result = urllib.request.urlopen(request)
os_bytes = result.read()
o_texto = os_bytes.decode('UTF-8')
listaLinhas = o_texto.split('\n')
dict = {}


#cria m dicionario com os ips
for indiceLinha in range(len(listaLinhas)):
    if(listaLinhas[indiceLinha] != ""):
        aLinhaEmLista = listaLinhas[indiceLinha].split()
        ip = aLinhaEmLista[0]
        codigoErro = aLinhaEmLista[-2]
        if ip in dict.keys():
            if codigoErro in dict[ip].keys():
                dict[ip][codigoErro] = dict[ip][codigoErro] + 1
            else:
                dict[ip][codigoErro] = 1
        else:
            dict[ip] = {}

for umaChave in dict.keys():
    for chaveInterior in dict[umaChave]:
        print('O ip {} apresentou o erro "{}" {} vezes' .format(umaChave, chaveInterior, dict[umaChave][chaveInterior]))






