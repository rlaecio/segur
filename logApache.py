# coding: latin-1
# versao python 3
import urllib.request, urllib.error, urllib.parse
import base64

request = urllib.request.Request('https://dev1.portodigital.pt/avs/log/lixo.log')
result = urllib.request.urlopen(request)
os_bytes = result.read()
o_texto = os_bytes.decode('UTF-8')
listaLinhas = o_texto.split('\n')

print('São exatamente {} linhas'.format(len(listaLinhas)))
dict = {}


for indiceLinha in range(len(listaLinhas)):
    if(listaLinhas[indiceLinha] != ""):
        ip = listaLinhas[indiceLinha].split()[0]
        if ip in dict.keys():
            dict[ip] = dict[ip] + 1
        else:
            dict[ip] = 1

key = max(dict, key=dict.get)
value = dict[key]

for umaChave in dict.keys():
    print('O ip {} apresentou {} vezes' .format(umaChave, dict[umaChave]))

print('O Ip que apresentou mais acesso foi o {}. Com {} acessos'.format(key, value))
#print('Os 5  ips com maior numero de acessos foram : \n {} '. format(ipsOrdenados))


busca = key
for indiceLinha in range(len(listaLinhas)):
    umaLinha = listaLinhas[indiceLinha]
    if umaLinha.find(busca) != -1:
        print('Com a URL {}' .format(umaLinha))












