#Atividade Prática 5
#Exercício 1 - Slide 9

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
total_com_gorjeta = valor_conta + valor_gorjeta

print(f"\nValor da gorjeta: R$ {valor_gorjeta:.2f}")
print(f"Total a pagar (conta + gorjeta): R$ {total_com_gorjeta:.2f}")