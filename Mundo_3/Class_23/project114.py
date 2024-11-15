import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'O site Pudim não está disponível!')
else:
    print(f'Consegui acessar o site pudim!')