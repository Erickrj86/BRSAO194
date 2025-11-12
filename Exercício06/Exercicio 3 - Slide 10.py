import requests

cep = input("Digite o CEP (somente números): ").strip()

if len(cep) != 8 or not cep.isdigit():
    print("CEP inválido! O CEP deve conter exatamente 8 números.")
else:

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("\n=== Endereço encontrado ===")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")
    else:
        print("Erro ao acessar a API. Código de status:", resposta.status_code)