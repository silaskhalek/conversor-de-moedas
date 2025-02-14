import requests

# URL da API de câmbio
url = "https://api.exchangerate-api.com/v4/latest/USD"

# Fazendo a requisição para a API
response = requests.get(url)

# Convertendo a resposta para JSON
dados = response.json()

# Pegando a cotação do dólar para o real
cotacao_brl = dados["rates"]["BRL"]

print(f"Cotação do dólar hoje: USD 1 = BRL {cotacao_brl:.2f}")
