# La función de enumerate es hacernos la vida más fácil cuando necesitamos acceder a los índices de una colección (Acceder a los objetos de la lista y a su índice)
print('** Enumerador - Enumerate **')
lista = ['a', 'b', 'c', 'd']

for letra in lista:
    print(letra)
    #print(index?)

print('* Usamos enumerate(lista) *')
# Nos lo imprime como tuplas (0, 'a'), (1, 'b'), etc.
for item in enumerate(lista):
    print(item)

print('* Usamos index, item en enumerate(lista) *')
# Nos lo imprime 0 a, 1 b, 2 c, etc.
for index, item in enumerate(lista):
    print(index, item)

print('* No solo trabajamos con strings, podemos usar rangos *')
for index, value in enumerate(range(0, 101, 10)):
    print(index, value)

print('* Otro caso: Usarlo fuera de los loops para crear tuplas con su índice *')
my_tuples = list(enumerate(lista))
print(my_tuples)
print('Acceder a un elemento de la lista')
print(f'Índice: {my_tuples[1][0]} - objeto: {my_tuples[1][1]}')
