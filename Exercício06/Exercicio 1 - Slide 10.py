import random
import string

tamanho = int(input("Digite o número de caracteres da senha: "))

letras = string.ascii_letters  # Letras maiúsculas e minúsculas
numeros = string.digits        # Dígitos de 0 a 9
simbolos = string.punctuation  # Caracteres especiais

todos_caracteres = letras + numeros + simbolos

senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))

print(f"\nSenha gerada: {senha}")