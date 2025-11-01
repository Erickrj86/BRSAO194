#Atividade Prática 4
#Exercício 3 - Slide 8

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    # Verifica se a senha tem pelo menos 8 caracteres e contém pelo menos um número
    if len(senha) >= 8 and any(char.isdigit() for char in senha): #verifica se existe ao menos um número na senha
        print("Senha forte!")
        break
    else:
        print("Senha fraca! A senha deve ter pelo menos 8 caracteres e conter ao menos um número.\n")