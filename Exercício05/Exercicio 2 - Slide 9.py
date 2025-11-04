#Atividade Prática 5
#Exercício 2 - Slide 9

import string

def verificar_palindromo(texto: str) -> str:

    texto_limpo = ''.join(
        char.lower() for char in texto if char.isalnum()
    )
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


frase = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(frase)
print(f"É palíndromo? {resultado}")