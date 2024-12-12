def suma(**kwargs):
    total = 0

    print(type(kwargs))
    print(total)

    for clave,valor in kwargs.items():
        total += valor
        print(f'{clave} = {valor}')
        

print(suma(x=3, y=5, z=2))

def prueba_printeo(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

prueba_printeo(15, 50, 100, 200, 45, 76, 89, 123, a="uno", b="dos", c="tres")

# Podemos usar los * (asteriscos) de los args o kwargs para desempacar tuplas, listas o diccionarios
args = [100, 200, 300, 400, 500, 600, 700, 800]
kwargs = {'x':'equis', 'y':'y griega', 'z':'zeta'}
prueba_printeo(15, 50, *args, **kwargs)


