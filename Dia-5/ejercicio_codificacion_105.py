'''Práctica sobre Argumentos Indefinidos (*args) 3
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"'''

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    print(type(args))
    print(args)

    return f'{nombre}, la suma de tus números es {suma_numeros}'

print(numeros_persona('Mónica', 7, 25, 90, 1, 3, 5, 7, 9)) # 147
