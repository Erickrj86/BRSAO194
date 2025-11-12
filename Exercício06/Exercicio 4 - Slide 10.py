import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    chave = f"{moeda}BRL"

    if chave in dados:
        cotacao = dados[chave]

        nome = cotacao.get("name", "Desconhecido")
        valor_atual = cotacao.get("bid", "N/A")
        valor_maximo = cotacao.get("high", "N/A")
        valor_minimo = cotacao.get("low", "N/A")
        data_atualizacao = cotacao.get("create_date", "N/A")

        print(f"\n=== Cotação de {nome} ===")
        print(f"Valor atual: R$ {valor_atual}")
        print(f"Valor máximo do dia: R$ {valor_maximo}")
        print(f"Valor mínimo do dia: R$ {valor_minimo}")
        print(f"Última atualização: {data_atualizacao}")
    else:
        print("Moeda não encontrada. Verifique o código informado.")
else:
    print("Erro ao acessar a API. Código de status:", resposta.status_code)