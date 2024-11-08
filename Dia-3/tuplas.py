mi_tupla = (1, 2, 3, 4, 2, 6, 2, 8, 2)
tupla = ('Perro', 33, 3.1415, [10, 20, 30], {'clave1': 'uno', 'clave2': 'dos'}, ('Juan', 'Pedro'))
print(type(mi_tupla))
print(mi_tupla[2])

print('LAS TUPLAS SON INMUTABLES')
print(tupla[3][2])

print('LAS TUPLAS SE PUEDEN CASTEAR Y SOBREESCRIBIRLAS')
print(type(tupla))
tupla = list(tupla)

print('POST CASTEO')
print(type(tupla))

print('VUELVO A CASTEARLA, AHORA A TUPLA')
tupla = tuple(tupla)
print(type(tupla))

print('PODEMOS ASIGNAR EL CONTENIDO DE LAS TUPLAS A VARIABLES, PRECONDICIÓN => MISMA CANTIDAD DE VALORES')
print('TAMBIÉN SE PUEDE HACER CON LAS LISTAS Y LOS DICCIONARIOS, SIEMPRE QUE COINCIDAN LA CANTIDAD DE VALORES')
otra_tupla = (1, 2, 3, 4, 5, 6, 7)
lunes, martes, miercoles, jueves, viernes, sabado, domingo = otra_tupla
print(lunes, martes, miercoles, jueves, viernes)
print(sabado, domingo)
print(len(otra_tupla))

print('Contar cuántas veces aparece el elemento pasado por parámetro')
print(mi_tupla.count(2))

print('Consultar el número de Índice de un elemento')
print(mi_tupla.index(2))

