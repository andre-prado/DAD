import requests

cep = "06418-010"
url = f"http://viacep.com.br/ws/{cep}/json"
retorno = requests.get(url).json()

logradouro = retorno['logradouro']
cidade = retorno['localidade']
estado = retorno['uf']
print(f'{logradouro} - {cidade} - {estado}')
