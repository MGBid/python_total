diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(diccionario))
print(diccionario)

resultado_c1 = diccionario['c1']
print(resultado_c1)

print('----------------------------------')
cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso': 88, 'talla': 1.76}
apellido = cliente['apellido']
talla = cliente['talla']
peso = cliente['peso']
print(f'{apellido}, {talla}, {peso}')

print('----------------------------------')
diccionario_mixto = {'clave1': 55, 'clave2': [10,20,30], 'clave3': {'c1':'rojo', 'c2': 'verde', 'c3': 'azul'}}
print(diccionario_mixto)
print(diccionario_mixto['clave2'][1])
print(diccionario_mixto['clave3'])
print(diccionario_mixto['clave3']['c2'])

print('----------------------------------')
diccionario_listas = {'lista1': ['a', 'b', 'c'], 'lista2': ['d', 'e', 'f']}
print(diccionario_listas)
print(diccionario_listas['lista2'][1].upper())
print(diccionario_listas['lista1'][0].upper())

print('----------------------------------')
print('Agregar Elementos a un Diccionario')
dicc = {1: 'a', 2: 'b'}
print(dicc)

dicc[3] = 'c'
print(dicc)

dicc[2] = 'B'
print(dicc)

print('----------------------------------')
print('Mostrar todas las Claves de un Diccionario')
print(diccionario_mixto.keys())

print('----------------------------------')
print('Mostrar todos los Valores de un Diccionario')
print(diccionario_mixto.values())

print('----------------------------------')
print('Mostrar todos los Items de un Diccionario')
print(diccionario_mixto.items())