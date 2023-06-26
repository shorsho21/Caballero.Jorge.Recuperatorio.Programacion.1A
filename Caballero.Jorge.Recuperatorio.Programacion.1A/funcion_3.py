def ordenarCaracteres(lista:str)->str:
    lista = list(lista)
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if lista[i] > lista[j]: #criterio de ordenamiento
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
    lista_ordenada = ""
    for letras in lista:
        lista_ordenada += letras

    return lista_ordenada

palabra_ordenada = ordenarCaracteres("algoritmo")

print(palabra_ordenada)
