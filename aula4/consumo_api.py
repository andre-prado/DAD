import requests as r #alias

url = 'https://google.com.br?q=impacta'
retorno = r.get(url)
print(retorno)
