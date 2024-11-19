menor = min(58, 96, 72, 64, 12, 35)
mayor = min(58, 96, 72, 64, 12, 35)
print(menor)
print(mayor)

print('* Otra forma de trabajarlo *')
lista = [58, 96, 72, 64, 35]
print(max(lista))
print(f'El valor mínimo dentro de la lista es: {min(lista)} y el máximo: {max(lista)}')

print('* Ahora probamos con strings *')
nombres = ['juan', 'pablo', 'alicia', 'carlos']
print(min(nombres))
print(max(nombres))

print('* Trabajando solo con un string *')
nombre = 'Carlos'
print(min(nombre)) # Primero va a buscar en las letras mayúsculas y luego en las minúsculas
print(min(nombre.lower())) # Para evitar errores, pasamos todo a minúscula

print('* Ahora veamos cómo se comporta con los diccionarios *')
diccionario = {'Clave1': 45, 'Clave2': 11, 'Clave3': 7, 'Clave4': 15}
print(min(diccionario))
print(max(diccionario))

print('Si queremos que trabaje sobre los valores... usamos diccionario.values()')
print(min(diccionario.values()))
print(max(diccionario.values()))
