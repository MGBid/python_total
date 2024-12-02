'''Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
'''
lista_numeros = [5, 45, 98, 12, 932, 126]

def cantidad_pares(lista):
    contador = 0

    for numero in lista:
        if numero % 2 == 0:
            contador += 1

    return contador

print(cantidad_pares(lista_numeros))