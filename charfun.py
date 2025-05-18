# charfun.py

def esPalindromo(cadena):
    # Eliminamos los espacios, convertimos a minúsculas y filtramos solo los caracteres alfanuméricos
    cadena = ''.join(c for c in cadena if c.isalnum()).lower()

    # Comparamos la cadena con su reverso
    return cadena == cadena[::-1]

def main():
    # Pedir al usuario una frase
    frase = input("Introduce una frase para su comprobación: ")

    # Llamar a la función esPalindromo y mostrar el resultado
    if esPalindromo(frase):
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")

if __name__ == "__main__":
    main()
