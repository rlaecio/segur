# coding: utf-8
import sys
import urllib.request, urllib.error, urllib.parse
import hashlib

def calcularSha1DasLinhas(ficheiroOut, listaLinhas, umaUrl):
   print("Processando", len(listaLinhas), "linhas e colocando no ficheiro")
   for numeroLinha in range(len(listaLinhas)):
       aLinha = listaLinhas[numeroLinha]
       oValor = hashlib.sha1()
       oValor.update(aLinha.encode().strip())
       resultadoEmBinario = oValor.digest()
       resultadoEmTxt = "".join("{:02x}".format(c) for c in resultadoEmBinario)
       linhaParaFicheiro = (resultadoEmTxt + "  " + umaUrl + "  " + str(numeroLinha))
       ficheiroOut.write(linhaParaFicheiro + "\n")


if len(sys.argv) < 3:
   print("Erro,utilização: python {} output.txt url1 [url2...]".format(sys.argv[0]))
   print(hashlib.algorithms_available)
   sys.exit(1)

nomeFicheiroOutput = sys.argv[1]
listaUrls = sys.argv[2:]
f = open(nomeFicheiroOutput, "w")


# print(listaUrls)
for umaUrl in listaUrls:
   print("Processando URL", umaUrl)
   try:
       request = urllib.request.Request("http://" + umaUrl)
   except:
       request = urllib.request.Request("https://" + umaUrl)
   result = urllib.request.urlopen(request)
   s = result.read()
   print(len(s), "bytes foram lidos")
   try:
       s = s.decode("utf-8")
   except:
       s = s.decode("iso-8859-1")
   print(len(s), "carateres")
   listaDeLinhas = s.strip().split("\n")
   calcularSha1DasLinhas(f, listaDeLinhas, umaUrl)


f.close()


print("OK, terminado")
