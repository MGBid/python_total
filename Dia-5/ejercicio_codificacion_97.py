'''Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.
'''
def todos_positivos(lista):
    lista_auxiliar = []
    for numero in lista:
        if numero > 0:
            lista_auxiliar.append(numero)
        else:
            pass
    return lista == lista_auxiliar

prueba = todos_positivos([9, 22, 345,17, 500])
print('----------------')
prueba2 = todos_positivos([9, 22, 345, -17, 500])

print(prueba, prueba2)

