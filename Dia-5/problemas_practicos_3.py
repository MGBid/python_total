'''EJERCICIO 3
Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True si en algún momento se ha ingresado al número cero repetido dos veces consecutivas.
'''
def numeros_consecutivos(*args):
    contador = 0

    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1

    return False


print(numeros_consecutivos(1, 2, 3, 0, 5, 6, 0))
print(numeros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5))
print(numeros_consecutivos(6, 0, 5, 1, 0, 3, 0, 1))