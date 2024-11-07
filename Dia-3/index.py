mi_texto = 'Esta es una prueba'
resultado = mi_texto[0]

print(resultado)
print(mi_texto[9])
print(mi_texto[-4])

print('Ahora le pasamos el caracter que queremos para que nos diga en qué índice se encuentra')
resultado_2 = mi_texto.index('n')
print(resultado_2)
print(mi_texto.index('prueba'))

print('Si busco una palabra que no existe => Da Error')
print('Es sensible a Mayúsculas')
print('Devuelve la primer ocurrencia, podemos Indicar desde dónde Buscar')

print('Buscamos la letra "a"  ' + str(mi_texto.index('a')) )
print('Buscamos la letra "a" después del índice 5 ' + str(mi_texto.index('a', 5)) )

print('Una alternativa es .rindex() que hace la misma búsqueda pero de derecha a izquierda')

print('Buscamos la letra "a" desde .rindex() ' + str(mi_texto.rindex('a')) )
