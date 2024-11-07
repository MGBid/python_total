texto = 'Este es el texto de Federico'
letra_upper = texto[5].upper()
print(letra_upper)
print(texto)

resultado_upper = texto.upper()
print(resultado_upper)

letra_lower = texto[5].lower()
print(letra_lower)
print(texto)

resultado_lower = texto.lower()
print(resultado_lower)

print('Método Split - Separar en elementos y los guarda en una lista - Por defecto los separa por el espacio')
resultado_split = texto.split()
print(resultado_split)

print('Paso por parámetro otro separador')
resultado_split_separador = texto.split('t')
print(resultado_split_separador)

print('Método JOIN')
a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = ' '.join([a, b, c, d])
f = '-'.join([a, b, c, d])
print(e)
print(f)

print('Método FIND')
# Es muy similar a index()
# Busca un determinado caracter dentro de un string
# La única diferencia con index() es que cuando no encuentra lo que se busca, no da error, devuelve -1
resultado_find = texto.find('s')
print(resultado_find)

resultado_find = texto.find('texto')
print(resultado_find)

resultado_find = texto.find('teXto')
print(resultado_find)

print('Método REPLACE')
# Requiere 2 parámetros, el texto anterior y el nuevo que va a reemplazarlo
resultado_replace = texto.replace('Federico', 'todos')
print(resultado_replace)

resultado_replace = texto.replace('e', 'x')
print(resultado_replace)

print('IMPORTANTE LEER LAS NOTAS DEL PDF SOBRE MÉTODOS DE STRINGS')
