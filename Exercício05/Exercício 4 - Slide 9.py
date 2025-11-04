#Atividade Prática 5
#Exercício 4 - Slide 9

from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:

    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação (sem considerar anos bissextos)
    return idade_dias

ano = int(input("Digite o ano de nascimento: "))
dias = calcular_idade_em_dias(ano)
print(f"Você tem aproximadamente {dias} dias de idade.")