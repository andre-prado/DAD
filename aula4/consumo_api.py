import requests as r #alias
# python.pythonpath verifica path do python
url = 'https://google.com.br?q=impacta' # procura impacta no google
retorno = r.get(url)
print(retorno)
