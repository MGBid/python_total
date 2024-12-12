from random import choice
'''
funciones pedir letra, validar letra, chequear letra, ver si ganó
luego implementar'''

def palabra_random():
    palabras = ['CASA', 'ARBOL', 'SOGA']
    random_choice = choice(palabras)
    return random_choice

def pedir_letra():
    letra = input('Ingresa una letra:\n')
    return letra

def validar_letra(letra, letras_palabra, letras_adivinadas):
    if letra in letras_palabra:
        print('Bien hecho!')
        letras_adivinadas.add(letra)

def ver_si_gano(vidas, letras_adivinadas, letras_palabra):
    if vidas > 0 and letras_adivinadas == letras_palabra:
        return True
    else:
        return False      

def jugar():
    vidas = 3
    palabra = palabra_random()
    letras_adivinadas = []
    while vidas > 0:
        letra_ingresada = pedir_letra()
        vidas -= 1
        validar_letra(letra_ingresada)
    print(palabra)  
    print(letras_adivinadas) 

jugar()
