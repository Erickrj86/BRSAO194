#Atividade Prática 3
#7-Calculadora da Média

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

#pesos
media = (n1*2 + n2*3 + n3*4 + n4*1) / 10

print(f"Media: {media:.1f}")

#situação
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    #nota do exame
    exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {exame:.1f}")

    #Recalculo da média final
    media_final = (media + exame) / 2
    print(f"Media final: {media_final:.1f}")

    #Resultado final
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")