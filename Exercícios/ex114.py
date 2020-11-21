import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[7;31mO site PUDIM não está acessível!\033[m')
else:
    print('\033[7;36mConsegui acessar o site PUDIM!\033[m')
