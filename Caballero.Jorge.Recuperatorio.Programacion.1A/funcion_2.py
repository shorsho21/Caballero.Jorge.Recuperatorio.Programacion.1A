def reemplazarCaracteres(cadena:str,caracter1:str,caracter2:str)->int:

    cadena = list(cadena)
    cadena_final = ""
    contador = 0

    for caracteres in range(len(cadena)):

        if cadena[caracteres] == caracter1:
            cadena[caracteres] = caracter2
            contador = contador + 1


    for caracteres in cadena:
        cadena_final += caracteres
    
    print(cadena_final)

    return contador


cantidad_reemplazada = reemplazarCaracteres("hola todo bien","a","O")

print(cantidad_reemplazada)
