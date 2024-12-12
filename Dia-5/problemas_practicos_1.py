from statistics import mean
'''EJERCICIO 1
Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
Si la suma de los 3 números es mayor a 15, va a devolver el número mayor
Si la suma de los 3 números es menor a 10, va a devolver el número menor
Si la suma de los 3 números es un valor entre 10 y 15 (incluídos) va a devolver el número de valor intermedio.'''

def devolver_distintos(num1, num2, num3):
    total = num1 + num2 + num3
    lista = [num1, num2, num3]

    if total > 15:
        return max(lista)
    elif total < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


print(devolver_distintos(2, 1, 5))
print(devolver_distintos(20, 1, 5))
print(devolver_distintos(2, 6, 5))
