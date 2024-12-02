'''Práctica sobre Interacción entre Funciones 2
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.'''

lista_numeros = [1,2,15,7,2]
def reducir_lista(lista):
    lista_reducida = list(set(lista))
    lista_reducida.pop()    

    return lista_reducida

def promedio(lista):
    acumulador = 0
    cantidad = len(lista)

    for numero in lista:
        acumulador += numero
        print(acumulador)
    
    
    promedio = acumulador/cantidad

    return promedio

milista = [1,2,15,7,2]
milista2 = reducir_lista(milista)
print(milista2)
print(promedio(reducir_lista(milista)))
