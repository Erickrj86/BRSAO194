#Atividade Prática 5
#Exercício 3 - Slide 9

preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco_original * (percentual_desconto / 100)

preco_final = preco_original - valor_desconto

print(f"\nValor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final do produto: R$ {preco_final:.2f}")