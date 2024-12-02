'''Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.'''
lista_numeros = [65, -599, 9009, 123, 32455, 100, 2, 9876, -345]

def suma_menores(lista):
    acumulador = 0
    for numero in lista:
        if numero in range(1, 1000):
            acumulador += numero
    
    return acumulador

print(suma_menores(lista_numeros))
