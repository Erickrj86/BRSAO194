#Atividade Prática 2
#6-Calculadora de Salário por Horas Trabalhadas

matricula = int(input("Digite sua matrícula: "))
horas_trabalhadas = float(input("Horas trabalhadas no mês: "))
valor_por_hora = float(input("Digite seu salário por hora: "))

salario = horas_trabalhadas * valor_por_hora

print("Dados do funcionário")
print(f"Matrícula = {matricula}")
print(f"Salário Total = R$ {salario:.2f}")