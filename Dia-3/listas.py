print('Listas: Secuencia ordenada de Objetos')
mi_lista = ['a', 'b', 'c']
otra_lista = ['hola', 55, 6.1]
resultado = len(mi_lista)
resultado_por_indice = mi_lista[0]
resultado_por_limites_de_indices = mi_lista[0:2]
lista_concatenada = mi_lista + otra_lista

print(type(mi_lista))
print(resultado)
print(resultado_por_indice)
print(resultado_por_limites_de_indices)
print('Concateno listas')
print(mi_lista + otra_lista)
print(lista_concatenada)

lista_concatenada[0] = 'alfa'
print(lista_concatenada)

lista_concatenada.append('G')
print(lista_concatenada)

lista_concatenada.pop() # Elimina el último elemento si no se le especifica el índice
print(lista_concatenada)

eliminado = lista_concatenada.pop(0)
print(lista_concatenada)
print(eliminado)

lista_desordenada = ['g', 't', 'b', 'z', 'o', 'a']
print(lista_desordenada)
lista_desordenada.sort()
print(lista_desordenada)

print('El Método SORT() NO retorna nada!')
lista_ordenada = lista_desordenada.sort()
print(type(lista_ordenada))
print('Non es el resultado de un Objeto que no devuelve nada')

print('REVERSE da vuelta el orden de los elementos')
lista_ordenada = lista_desordenada
lista_ordenada.reverse()
print(lista_ordenada)
