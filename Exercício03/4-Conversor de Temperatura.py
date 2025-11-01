#Atividade Prática 3
#4-Conversor de Temperatura

temperatura = float(input("Digite a temperatura: "))
escala_inicial = input("Informe a unidade de origem (C, F, K): ").upper()
escala_final = input("Informe a unidade de destino (C, F, K): ").upper()

if escala_inicial == "C":
    resultado = temperatura
elif escala_inicial == "F":
    resultado = (temperatura - 32) * 5/9
elif escala_inicial == "K":
    resultado = temperatura - 273.15
else:
    print("Escala de origem inválida.")
    exit()

# Converte de Celsius para a unidade de destino
if escala_final == "C":
    temp_final = resultado
elif escala_final == "F":
    temp_final = (resultado * 9/5) + 32
elif escala_final == "K":
    temp_final = resultado + 273.15
else:
    print("Escala de destino inválida.")
    exit()

# Exibe o resultado
print(f"{temperatura:.2f}°{escala_inicial} equivalem a {temp_final:.2f}°{escala_final}.")