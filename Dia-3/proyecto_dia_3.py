print('ANALIZADOR DE TEXTO - PYTHON')
texto = input('Ingrese el texto a analizar\n').lower()
letras = []

letras.append(input('Ingrese la primer letra\n').lower())
letras.append(input('Ingrese la segunda letra\n').lower())
letras.append(input('Ingrese la tercer letra\n').lower())

print('COMENZAMOS CON EL ANÁLISIS...')

print('\nI - Esta es la cantidad de veces que aparecen tus letras en el texto:')
letra_1 = texto.count(letras[0])
letra_2 = texto.count(letras[1])
letra_3 = texto.count(letras[2])
print(f'\n"{letras[0].upper()}" = {letra_1} veces\n"{letras[1].upper()}" = {letra_2} veces\n"{letras[2].upper()}" = {letra_3} veces')

print('\nII - CUÁNTAS PALABRAS CONTIENE EL TEXTO INGRESADO')
texto_en_palabras = texto.split()# si no pongo ' ' igual las separa por espacios
print(f'El texto ingresado contiene:\n{len(texto_en_palabras)} palabras')


print('\nIII - INFORMAR LA PRIMERA Y LA ÚLTIMA LETRA DEL TEXTO INGRESADO')
print(f'La Primera letra es: {texto[0].upper()}')
print(f'La Última letra es: {texto[-1]}')

print('\nIV - INVERTIMOS EL ORDEN DEL TEXTO INGRESADO')
texto_invertido = texto_en_palabras
texto_invertido.reverse()

lista_a_texto = ' '.join(texto_invertido)
print(lista_a_texto)

print('\nV - INFORMAMOS SI EXISTE LA PALABRA "PYTHON" EN EL TEXTO INGRESADO')
diccionario_existe = {True: 'CONTIENE', False: 'NO CONTIENE'}
existe = str(diccionario_existe['python' in texto])
cadena = f'El texto ingresado {existe} la palabra "PYTHON"\n\n'
print(cadena)

