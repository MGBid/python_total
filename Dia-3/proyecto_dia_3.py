print('ANALIZADOR DE TEXTO - PYTHON')

texto = input('Ingrese el texto a analizar\n').lower()
letras = input('Ingrese 3 letras separadas por coma o espacios\n').lower()
print(type(texto))
print(type(letras))
print(letras)
letras = letras.split(',')


print('COMENZAMOS CON EL ANÁLISIS...')
print(letras)
print(texto)

print('\nANÁLISIS I:\nEsta es la cantidad de veces que aparecen tus letras seleccionadas en el texto:')
letra_1 = texto.count(letras[0])
letra_2 = texto.count(letras[1])
letra_3 = texto.count(letras[2])
print(f'Cantidades:\n{letras[0]} = {letra_1}\n{letras[1]} = {letra_2}\n{letras[2]} = {letra_3}\n')

print('\nANÁLISIS II CUÁNTAS PALABRAS CONTIENE EL TEXTO INGRESADO')
texto_en_palabras = texto.split(' ')
print(f'El texto ingresado contiene:\n{len(texto_en_palabras)} palabras')
print(texto_en_palabras)

print('\nANÁLISIS III INFORMAR LA PRIMERA Y LA ÚLTIMA LETRA DEL TEXTO INGRESADO')
print(f'La Primera letra es: {texto[0].upper()} ')
print(f'La Última letra es: {texto[-1].upper()}')

print('\nANÁLISIS IV INVERTIMOS EL ORDEN DEL TEXTO INGRESADO')
texto_invertido = texto_en_palabras
texto_invertido.reverse()
print(texto_invertido)

lista_a_texto = ' '.join(texto_invertido)
print(lista_a_texto)

print('\nANÁLISIS V INFORMAMOS SI EXISTE LA PALABRA "PYTHON" EN EL TEXTO INGRESADO')
diccionario_existe = {True: 'CONTIENE', False: 'NO CONTIENE'}
existe = str(diccionario_existe['python' in texto])
cadena = f'El texto ingresado {existe} la palabra "PYTHON"'
print(cadena)

