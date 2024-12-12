'''Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).'''

def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg ** 2
    return total

print(suma_cuadrados(2, 3, 4, 5))

# 4+9+16+25=54