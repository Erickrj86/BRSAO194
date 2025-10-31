#Atividade Prática 2
#2-Calculadora de Desconto

print("Boas vindas ao calculador de desconto")

Produto = "Camiseta"
Preco = 50.00
Desconto = 0.2 #20%"

total_desconto = Preco * Desconto
valor_desconto = Preco - total_desconto

print(f"O Valor para {Produto} é de R${Preco:.2f}.\nCom um desconto de 20% equivalente a R${total_desconto:.2f}, o valor final é de R${valor_desconto:.2f}")