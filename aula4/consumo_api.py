import requests as r

url = 'https://google.com.br?q=impacta'
retorno = r.get(url)
print(retorno)
