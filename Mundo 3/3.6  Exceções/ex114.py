#  Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
    
except urllib.error.URLError:
    print('O site ou o usuário está offline')
    
else:
    print('o site ta on ta ligado irmao')
    
    
    
# ta dando errado e eu n sei porque