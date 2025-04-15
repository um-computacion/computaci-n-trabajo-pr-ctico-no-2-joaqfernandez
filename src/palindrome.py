
def is_palindrome(texto):

    texto_limpio = limpiar_texto(texto)

    return comparar(texto_limpio) 

def limpiar_texto(texto):
    
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter.isalnum():
            limpio += caracter
    return limpio

def comparar(texto_limpio):
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    try:
        print("Verificador de palindromos")
        print("Ctrl+C para salir")
        while True:
            entrada = input("Ingresa una palabra o frase: ")
            if is_palindrome(entrada):
                print("Es un palíndromo")
            else:
                print("No es un palíndromo")
    except KeyboardInterrupt:
        print("Programa terminado. ¡Hasta luego!")
