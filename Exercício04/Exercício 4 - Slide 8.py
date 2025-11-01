#Atividade Prática 4
#Exercício 4 - Slide 8

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break  # Encerra o programa

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros ou 'fim' para sair.\n")

# Exibe o resumo final
print("\n--- Resultado final ---")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")