#Atividade Prática 4
#Exercício 2 - Slide 8

#lista para as notas
notas = []

while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break  # Encerra o loop quando o professor digita 'fim'

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite uma nota numérica ou 'fim' para sair.")

# Cálculo e exibição da média
if notas:
    media = sum(notas) / len(notas)
    print(f"\nNotas digitadas: {notas}")
    print(f"\nMédia da turma: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")