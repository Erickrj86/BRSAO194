#Atividade Prática 3
#6-Calculadora de Comissão

nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o total vendido no mês em R$: "))

comissao = vendas * 0.15
total = salario_fixo + comissao

print(f"TOTAL = R$ {total:.2f}")