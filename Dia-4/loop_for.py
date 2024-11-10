lista = ['pablo', 'laura', 'luis', 'julia', 'fede']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)


numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for valor in numeros:
    mi_valor += valor

print(mi_valor)


for letra in 'Python':
    print(letra)


print('Podemos iterar Tuplas o Listas que contengan listas')
for item in (9, 8, 7, 12, 15):
    print(item)

print('------------')
for elemento in [[2, 4], [8, 70], [11, 22, 33]]:
    print(elemento)   

print('------------')
for elemento1, elemento2 in [[2, 4], [8, 70], [11, 22]]:
    print(elemento1)
    print(elemento2)   

print('------------')
for elemento in [[2, 4], [8, 70], [11, 22, 33]]:
    for item in elemento:
        print(item) 

print('Ya Pasó Fangio')

print('Iterando un diccionario')
diccionario = {'clave_1': 'Juan', 'clave_2': 'Pedro', 'clave_3': 'María'}
for item in diccionario:
    print(item)

print('************')
for item in diccionario.items():
    print(item)

print('************')
for item in diccionario.values():
    print(item)

print('************')
for clave, valor in diccionario.items():
    print(clave, valor)