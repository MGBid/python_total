'''Se pueden crear de dos maneras:
set(1,2,3,4,5,6) => El SET admite un solo argumento, por lo que tienen que estar encerrados en paréntesis, corchetes o llaves curvas para que Python los lea como un solo elemento.
{ 1,2,3,4,5,6 } => Python reconoce que no es un diccionario. '''
print('PARTICULARIDAD DE LOS SETS: SÓLO ADMITE ELEMENTOS ÚNICOS!')
print('OTRA CARACTERÍSTICA, NO ESTÁN ORDENADOS, NO SE PUEDEN INDEXAR, REORGANIZAR NI NADA QUE TENGA QUE VER CON SU POSICIÓN INTERNA')
print('SON INMUTABLES')
print('NO SE PUEDEN INCLUIR LISTAS Y DICCIONARIOS DENTRO DE LOS SETS')
mi_set = set([1, 2, 3, 4, 5])
mi_set_2 = set((6, 7, 53, 44, 95))
mi_set_3 = set({12, 20, 33, 47, 51})
print(type(mi_set))
print(mi_set)
print(mi_set_2)
print(mi_set_3)

otro_set = {'Juan', 'Pablo', 'Matias'}
print(type(otro_set))
print(otro_set)

print('ADMITE TUPLES PORQUE SON INMUTABLES')
print(len(otro_set))

print('SABER SI UN ELEMENTO EXISTE EN MI SET')
print('Juan' in otro_set)

print('UNIÓN DE SETS')
uniendo_sets = mi_set.union(otro_set)
print(type(uniendo_sets))
print(uniendo_sets)

print('AGREGAR ELEMENTOS')
print(otro_set)
otro_set.add('Florencia')
print(otro_set)

print('ELIMINAR ELEMENTO')
otro_set.remove('Florencia')
print(otro_set)
print('SI LE PEDIMOS QUE ELIMINE UN ELEMENTO QUE NO EXISTE, DA ERROR')

print('TENEMOS EL MÉTODO DISCARD() QUE ELIMINA EL ELEMENTO INDICADO POR PARÁMETRO, Y EN CASO DE QUE NO EXISTA, NO DA ERROR.')
otro_set.discard('Juan Pablo')
print(otro_set)

print('OTRO MÉTODO DE ELIMINAR ES POP() PERO ELIMINA UN ELEMENTO ALEATORIO, YA QUE NO HAY ORDEN EN LOS ELEMENTOS.')
otro_set.pop()
print(otro_set)

print('TAMBIÉN TENEMOS EL MÉTODO CLEAR() QUE LIMPIA EL SET')
otro_set.clear()
print(otro_set)

print('EXISTEN MUCHOS MÉTODOS MÁS, ESTÁN EN EL PDF')
