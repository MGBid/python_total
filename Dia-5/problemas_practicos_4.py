'''EJERCICIO 4
Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va desde cero hasta ese número incluído, y va a devolver la cantidad de números primos que encontró.
Por convención, el 0 y el 1 no se consideran primos.
'''

# NO LO ENTENDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    
    while iteracion <= numero:

        for num in range(3, iteracion, 2):

            if iteracion % num == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(150))
print(contar_primos(50))
print(contar_primos(1))

