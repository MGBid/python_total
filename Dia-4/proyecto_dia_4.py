from random import randint

'''Pregunta el nombre y da 8 oportunidades para adivinar el número
si el número es menor a 1 o superior a 100 le dice que no es un número permitido
Si el número que eligió el usuario es menor al número pensado por el programa, le dirá que es incorrecta y 
que eligió un número menor al número secreto, lo mismo para el caso de que el número es mayor
y si el usuario acertó el número se le informa que ha Ganado y cuántos intentos le ha tomado
Es hasta que gane o que se agoten los 8 intentos'''
adivinado = False
intentos = 0
numero_secreto = randint(1, 100)


nombre = input('Dime tu nombre: \n')

print(f'{nombre} Bienvenido a "ADIVINA EL NÚMERO SECRETO"')


while  not adivinado and intentos < 8:
    numero_ingresado = int(input('Piensa bien e ingresa un número: \n'))
    intentos += 1
    if numero_ingresado not in range(1, 101):
        print('Ingresaste un número NO VÁLIDO')
    elif numero_ingresado > numero_secreto:
        print(f'{numero_ingresado} Es Mayor que el Número Secreto')
    elif numero_ingresado < numero_secreto:
        print(f'{numero_ingresado} Es Menor que el Número Secreto')
    else:
        adivinado = True
        print(f'FELICITACIONES!!! ADIVINASTE EL NÚMERO {numero_secreto}\nLo lograste en {intentos} intentos')

    
    print('\n\n\n\n\n\n\n\n')

if numero_ingresado != numero_secreto:
    print(f'Lo siento, se agotaron los intentos.\nEl número secreto es: {numero_secreto}')

