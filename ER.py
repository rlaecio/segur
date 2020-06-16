# coding: latin-1
# versao python 3
import urllib.request, urllib.error, urllib.parse, re
import base64

request = urllib.request.Request('http://www.devopsguys.com/blog/')
result = urllib.request.urlopen(request)
s = result.read()
s = s.decode('utf-8')
t = s.split("\n")

filtrarTitulo = re.compile('rel="bookmark">([^<]+)')
filtrarUrl = re.compile('canonical" href="([^ "]+)')
filtrarData = re.compile('datetime="([^\d{4}])')
filtrarAutor = re.compile('"author vcard">')


# captura o titulo ao texto
tituloEmTexto = filtrarTitulo.search(s)
if tituloEmTexto != None:
    titulo = s[tituloEmTexto.start(1):tituloEmTexto.end(1)]
else:
    titulo = '< title is blank >'

# captura a url da pagina
urlEmTexto = filtrarUrl.search(s)
if urlEmTexto != None:
    urlDoSite = s[urlEmTexto.start(1):urlEmTexto.end(1)]
else:
    urlDoSite = '< url not found >'

# captura a data do site
dataEmTexto = filtrarData.search(s)
if dataEmTexto != None:
    dataDoPost = s[dataEmTexto.start(1):dataEmTexto.end(1)]
else:
    dataDoPost = '<  no date >'


# captura o author
authorEmTexto = filtrarAutor.search(s)
if authorEmTexto != None:
    authorDoPost = s[authorEmTexto.start(1):authorEmTexto.end(1)]
else:
    authorEmTexto = '<  nauthor not found >'


print(titulo, urlDoSite, dataDoPost, authorDoPost)
