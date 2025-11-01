#Atividade Prática 4
#Exercício 1 - Slide 8

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use apenas +, -, * ou /.")

        print(f"Resultado: {resultado}")
        break

    except ValueError as valor_invalido:
        print(f"Erro: {valor_invalido}")
        print("Por favor, insira valores numéricos válidos e uma operação correta.\n")
    except ZeroDivisionError as divisao_zero:
        print(f"Erro: {divisao_zero}")
        print("Tente novamente.\n")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        print("Tente novamente.\n")