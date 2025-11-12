import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    usuario = dados["results"][0]  

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("\n=== Perfil de Usuário Gerado ===")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

else:
    print("Erro ao acessar a API. Código de status:", response.status_code)