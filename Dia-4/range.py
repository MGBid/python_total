print('Versión 1') # No es eficiente
lista = [1, 2, 3, 4]

for numero in lista:
    print(numero)

print('# Versión 2') # Apelamos a un rango que vaya hasta 5
for numero in range(5):
    print(numero)

print('# Versión 2.2') # Le indicamos desde dónde hasta dónde
for numero in range(20, 31):
    print(numero)

print('# Versión 2.3') # Le indicamos con el 3er parámetro los pasos que va a dar
for numero in range(10, 51, 5):
    print(numero)

print('VIP: Range NO RECIBE PARÁMETROS FLOAT, SÓLO INTEGERS')
print('RANGE nos sirve para utilizarlo dentro de los loops y hacerlos más EFICIENTES')
print('Pero también podemos usarlo POR FUERA de los LOOPS\n')

print('Crear una lista que vaya del 1 al 100')
# Creamos una lista con un casting
lista_range = list(range(1, 101))
print(lista_range)

